from war_room.core.user import User
from war_room.core.database.base import UserDatabase

class TemporaryUserDatabase(UserDatabase):
    
    def __init__(self):
        self.users = {}

    def register_user(self, discord_id: int):
        self.users[discord_id] = User(discord_id = discord_id)

    def contains_user(self, discord_id: int) -> User:
        return discord_id in self.users

    def get_user(self, discord_id: int) -> User:
        return self.users[discord_id]

    def update_user_information(self, user: User) -> None:
        self.users[user.discord_id] = user