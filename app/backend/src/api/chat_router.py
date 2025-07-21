from fastapi import APIRouter,Depends
from services.chat_services import ChatServices
from services.user_services import UserServices
from services.usertochat_services import UserToChatServices
from models.models import User
from schemas.schemas import ChatAdd
from api.dependencies import chat_service,user_service,usertochat_service
from auth.auth import current_user
from fastapi import HTTPException


router = APIRouter(
    tags=['chat'],
    prefix='/chat'
)

@router.post('/{user_id}')
async def create_chat(
    user_id: int,
    user: User = Depends(current_user),
    chat_service: ChatServices = Depends(chat_service),
    user_service: UserServices = Depends(user_service),
    usertochat_service: UserToChatServices = Depends(usertochat_service),
    
):

    user_id_check = await user_service.get_user_by_id(user_id)
    if not user_id_check:
        return HTTPException(status_code=403,detail='user does not exist')

    chat_id = await chat_service.add_chat()

    first_m2m = await usertochat_service.add(user_id,chat_id)
    second_m2m = await usertochat_service.add(user.id,chat_id)

    if first_m2m and second_m2m:
        return chat_id
    
    else: return HTTPException(status_code=403,detail='Exception')


@router.get('/all')
async def get_all_chat(
    chat_service: ChatServices = Depends(chat_service),
    user: User = Depends(current_user),
):

    chats = await chat_service.get_all()
    return chats


@router.get('/{id}/users')
async def get_all_chat(
    chat_id: int,
    chat_service: ChatServices = Depends(chat_service),
    user: User = Depends(current_user),
):

    users = await chat_service.find_users_in_chat(chat_id)
    return users