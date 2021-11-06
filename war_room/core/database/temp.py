from option import Option, Result

from war_room.core.database.base import UniqueDictionaryLikeDatabase
from war_room.core.types.interfaces import UniqueDataclassDictionaryLike


class TemporaryUniqueDictionaryLikeDatabase(UniqueDictionaryLikeDatabase[UniqueDataclassDictionaryLike]):
    def __init__(self):
        self.items = {}

    def get(self, uid: int) -> Result[Option[UniqueDataclassDictionaryLike], str]:
        if uid in self.items:
            return Result.Ok(Option.Some(self.items[uid]))
        else:
            return Result.Ok(Option.NONE())

    def update(self, udl: UniqueDataclassDictionaryLike) -> Result[None, str]:
        self.items[udl.uid] = udl
        return Result.Ok(None)


class TemporaryUserDatabase(TemporaryUniqueDictionaryLikeDatabase):
    pass


class TemporaryMatchDatabase(TemporaryUniqueDictionaryLikeDatabase):
    pass
