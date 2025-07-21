from services.user_services import UserServices
from repositories.user_repo import UserRepository

from services.message_services import MessageServices
from repositories.message_repo import MessageRepository

from services.chat_services import ChatServices
from repositories.chat_repo import ChatRepository

from services.usertochat_services import UserToChatServices
from repositories.usertochat_repo import UserToChatRepository



def user_service() -> UserServices:
    return UserServices(UserRepository)

def chat_service() -> ChatServices:
    return ChatServices(ChatRepository)

def message_service() -> MessageServices:
    return MessageServices(MessageRepository)

def usertochat_service() -> UserToChatServices:
    return UserToChatServices(UserToChatRepository)