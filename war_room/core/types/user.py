from dataclasses import dataclass
from typing import Dict, Any
from war_room.core.types.interfaces import DataclassDictionaryLike, Unique

@dataclass
class User(Unique, DataclassDictionaryLike):
    id: int 
    game_count: int = 0
    rating: float = 800.0

    @property
    def uid(self):
        return self.id

    @staticmethod
    def from_dict(dict: Dict[str, Any]):
        return User(**dict)