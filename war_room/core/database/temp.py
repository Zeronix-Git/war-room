from option import Option, Result
from war_room.core.types import User
from war_room.core.database.base import UserDatabase

class TemporaryUserDatabase(UserDatabase):
    
    def __init__(self):
        self.users = {}

    def get_user(self, id: int) -> Result[Option[User], str]:
        if id in self.users:
            return Result.Ok(Option.Some(self.users[id]))
        else:
            return Result.Ok(Option.NONE())

    def update_user(self, user: User) -> Result[None, str]:
        self.users[user.id] = user
        return Result.Ok(None)