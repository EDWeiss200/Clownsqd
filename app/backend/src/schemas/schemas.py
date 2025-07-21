from pydantic import BaseModel,EmailStr,Field,FileUrl
from sqlalchemy import Date
from fastapi import UploadFile
from enum import Enum
from typing import Optional
from datetime import datetime



class UserReadSchema(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True

class UserReadShortSchema(BaseModel):
    id: int
    username: str
   




class ChatRead(BaseModel):

    id: int
    created_on: datetime


class ChatAdd(BaseModel):
    user_id: int



class MessageRead(BaseModel):
    id: int
    chat_id: int
    user_id: int
    text: str
    created_on: datetime

class MessageAdd(BaseModel):
    id: int
    chat_id: int
    text: str


class UserChatsReadSchema(UserReadSchema):

    user_chats: list['ChatRead']

class UsersInChatReadSchema(ChatRead):

    users_in_chat: list['UserReadShortSchema']

