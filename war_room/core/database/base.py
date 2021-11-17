from abc import ABC, abstractmethod
from typing import Generic, Iterator, TypeVar

from option import Option, Result

from war_room.core.custom_types import Match, User

UniqueDictionaryLike = TypeVar('UniqueDictionaryLike')


class UniqueDictionaryLikeDatabase(ABC, Generic[UniqueDictionaryLike]):
    """A database that handles generic objects.

    Objects must implement the interfaces:
    - war_room.core.types.unique.Unique
    - war_room.core.types.dict_like.DictionaryLike
    """

    @abstractmethod
    def get(self, uid: int) -> Result[Option[UniqueDictionaryLike], str]:
        """Get an object by its unique ID."""
        pass

    def contains(self, uid: int) -> Result[bool, str]:
        return self.get(uid).map(lambda maybe_object: maybe_object.is_some)

    @abstractmethod
    def __iter__(self) -> Iterator[Result[UniqueDictionaryLike, str]]:
        pass

    @abstractmethod
    def update(self, udl: UniqueDictionaryLike) -> Result[None, str]:
        """Update an object's data in the database.

        If the object does not already exist, this should create a new object in the DB.
        If the object already exists, this should update that object's information
        without creating a duplicate."""
        pass


class UserDatabase(UniqueDictionaryLikeDatabase[User]):
    pass


class MatchDatabase(UniqueDictionaryLikeDatabase[Match]):
    @abstractmethod
    def get_user_active_game_count(self, user_id: int) -> Result[int, str]:
        pass
