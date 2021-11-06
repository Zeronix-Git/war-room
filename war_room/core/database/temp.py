from option import Option, Result
from typing import Generic
from war_room.core.types import User, Match
from war_room.core.database.base import UniqueDictionaryLikeDatabase, UniqueDictionaryLike

class TemporaryUniqueDictionaryLikeDatabase(UniqueDictionaryLikeDatabase, Generic[UniqueDictionaryLike]):
    
    def __init__(self):
        self.items = {}

    def get(self, uid: int) -> Result[Option[UniqueDictionaryLike], str]:
        if uid in self.items:
            return Result.Ok(Option.Some(self.items[uid]))
        else:
            return Result.Ok(Option.NONE())

    def update(self, udl: UniqueDictionaryLike) -> Result[None, str]:
        self.items[udl.uid] = udl
        return Result.Ok(None)

class TemporaryUserDatabase(TemporaryUniqueDictionaryLikeDatabase[User]):
    pass

class TemporaryMatchDatabase(TemporaryUniqueDictionaryLikeDatabase[Match]):
    pass