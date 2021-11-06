from abc import ABC, abstractmethod
from war_room.core.user import User

class UserDatabase(ABC):

    @abstractmethod
    def register_user(self, discord_id: int):
        pass

    @abstractmethod
    def get_user(self, discord_id: int) -> User:
        pass

    @abstractmethod
    def contains_user(self, discord_id: int) -> User:
        pass

    @abstractmethod
    def update_user_information(self, user: User) -> None:
        pass
