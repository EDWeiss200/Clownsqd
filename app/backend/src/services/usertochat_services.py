from utils.repository import AbstractRepository
from fastapi import HTTPException


class UserToChatServices:

    def __init__(self,usertochat_repo: AbstractRepository) -> None:
        self.usertochat_repo = usertochat_repo()

    async def add(self,user_id,chat_id):
        usertochat_add = {
            'user_id': user_id,
            'chat_id': chat_id
        }
        user_to_chat = await self.usertochat_repo.add_one_not_return(usertochat_add)
    
        
        return user_to_chat

        