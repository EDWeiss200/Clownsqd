from typing import Annotated
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Boolean, ForeignKey, Integer, String, Column,MetaData,Date
from schemas.schemas import UserReadSchema,ChatRead,MessageRead
from datetime import datetime
intpk = Annotated[int, mapped_column(index = True,primary_key=True)]


metadata = MetaData()

class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int],Base):
    __tablename__= "users"
    id:Mapped[intpk] = mapped_column(
        index=True
    )
    username: Mapped[str] = mapped_column(
        nullable=False
    )
    email:Mapped[str] = mapped_column(
        nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )

    user_chats: Mapped[list['Chat']] = relationship(
        back_populates="users_in_chat",
        secondary='usertochat'
    )

    def to_read_model(self) -> UserReadSchema:
        return UserReadSchema(
            id = self.id,
            username=self.username,
            email=self.email,
        )


class Chat(Base):
    __tablename__= "chats"
    id:Mapped[intpk] = mapped_column(
        index=True
    )
    created_on: Mapped[datetime] = mapped_column()

    users_in_chat : Mapped[list['User']] = relationship(
        back_populates="user_chats",
        secondary='usertochat'
    )



class Message(Base):
    __tablename__= "messages"
    id:Mapped[intpk] = mapped_column(
        index=True
    )
    chat_id:Mapped[intpk] = mapped_column(
        ForeignKey('chats.id')
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id')
    )
    text: Mapped[str] = mapped_column()
    created_on: Mapped[datetime] = mapped_column()



class UserToChat(Base):
    __tablename__ = 'usertochat'

    user_id: Mapped[intpk] = mapped_column(
        ForeignKey('users.id',ondelete = 'CASCADE'),
        primary_key = True, 
    )
    chat_id: Mapped[intpk] = mapped_column(
        ForeignKey('chats.id',ondelete='CASCADE'),
        primary_key = True, 
    )
