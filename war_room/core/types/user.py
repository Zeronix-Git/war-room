from dataclasses import dataclass
from typing import Any, Dict

from war_room.core.types.interfaces import UniqueDataclassDictionaryLike


@dataclass
class User(UniqueDataclassDictionaryLike):
    id: int
    game_count: int = 0
    rating: float = 800.0

    @property
    def uid(self):
        return self.id

    @staticmethod
    def from_dict(dict: Dict[str, Any]):
        return User(**dict)
