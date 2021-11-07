from typing import Iterator

from option import Option, Result

from war_room.core.custom_types.interfaces import UniqueDictionaryLike
from war_room.core.database.base import MatchDatabase, UniqueDictionaryLikeDatabase, UserDatabase


class TemporaryUniqueDictionaryLikeDatabase(UniqueDictionaryLikeDatabase[UniqueDictionaryLike]):
    def __init__(self):
        self.items = {}

    def get(self, uid: int) -> Result[Option[UniqueDictionaryLike], str]:
        if uid in self.items:
            return Result.Ok(Option.Some(self.items[uid]))
        else:
            return Result.Ok(Option.NONE())

    def __iter__(self) -> Iterator[Result[UniqueDictionaryLike, str]]:
        for item in self.items.values():
            yield Result.Ok(item)

    def update(self, udl: UniqueDictionaryLike) -> Result[None, str]:
        self.items[udl.uid] = udl
        return Result.Ok(None)


class TemporaryUserDatabase(TemporaryUniqueDictionaryLikeDatabase, UserDatabase):
    pass


class TemporaryMatchDatabase(TemporaryUniqueDictionaryLikeDatabase, MatchDatabase):
    pass
