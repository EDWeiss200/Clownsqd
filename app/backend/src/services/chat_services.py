from utils.repository import AbstractRepository
from datetime import datetime
from schemas.schemas import UsersInChatReadSchema
from fastapi import HTTPException



class ChatServices:

    def __init__(self,chat_repo: AbstractRepository) -> None:
        self.chat_repo = chat_repo()

    async def get_chat_by_id(self,chat_id):

        filters = [
            self.chat_repo.model.chat_id == chat_id
        ]

        chat_id = await self.chat_repo.find_filter(filters)

        

        return chat_id


    async def add_chat(self):

        chat_dict = {}
        chat_dict['created_on'] = datetime.now()
        chat_id = await self.chat_repo.add_one(chat_dict)

        return chat_id

    async def get_all(self):

        
        chats = await self.chat_repo.find_all()

        return chats

    async def find_users_in_chat(self,chat_id):
        
        relation_ship = self.chat_repo.model.users_in_chat
        users_all = await self.chat_repo.relationship_base_find(relation_ship,chat_id)
        result = [UsersInChatReadSchema.model_validate(row,from_attributes=True) for row in users_all]

        if result:
            for i in result[0]:
                if i[0] == 'users_in_chat':
                    return i[1]
        else:
            raise HTTPException(status_code=403,detail='CHAT does not exist')