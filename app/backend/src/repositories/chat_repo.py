from utils.repository import SQLAlchemyRepository

from models.models import Chat

class ChatRepository(SQLAlchemyRepository):

    model = Chat