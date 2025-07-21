from utils.repository import AbstractRepository
from datetime import datetime

class MessageServices:

    def __init__(self,messasge_repo: AbstractRepository) -> None:
        self.message_repo = message_repo()

    async def get_message_by_id(self,message_id):

        filters = [
            self.message_repo.model.message_id == message_id
        ]

        message = await self.message_repo.find_filter(filters)

        

        return message

    async def get_messages_all(self,chat_id):

        filters = [
            self.message_repo.model.chat_id == chat_id
        ]

        messages = await self.message_repo.find_all(filters)

        

        return messages

    async def add_message(self,user_id,message,chat_id):

        message_dict = message.model_dump()
        message_dict['chat_id'] = chat_id
        message_dict['user_id'] = user_id
        message_dict['created_on'] = datetime.now()
        message_id = await self.message_repo.add_one(message_dict)

        return message_id

    
        


