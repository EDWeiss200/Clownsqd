from utils.repository import SQLAlchemyRepository

from models.models import UserToChat

class UserToChatRepository(SQLAlchemyRepository):

    model = UserToChat