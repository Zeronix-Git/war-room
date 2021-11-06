from option import Option, Result
from war_room.core.types import User, Match
from war_room.core.database.base import MatchDatabase, UserDatabase

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

class TemporaryMatchDatabase(MatchDatabase):
    
    def __init__(self):
        self.matches = {}

    def get_match(self, id: int) -> Result[Option[Match], str]:
        if id in self.matches:
            return Result.Ok(Option.Some(self.matches[id]))
        else:
            return Result.Ok(Option.NONE())

    def update_match(self, match: Match) -> Result[None, str]:
        self.users[match.id] = match
        return Result.Ok(None)