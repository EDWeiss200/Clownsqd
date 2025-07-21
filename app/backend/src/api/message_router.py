from fastapi import APIRouter,Depends
from services.user_services import UserServices
from models.models import User
from schemas.schemas import UserReadSchema
from api.dependencies import user_service
from auth.auth import current_user


router = APIRouter(
    tags=['message'],
    prefix='/messages'
)