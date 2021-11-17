from dataclasses import dataclass
from typing import Any, Dict, Tuple

from war_room.core.custom_types.interfaces import DataclassDictionaryLike, UniqueDictionaryLike
from war_room.core.custom_types.match import Tier


@dataclass
class Map(UniqueDictionaryLike, DataclassDictionaryLike):
    """An object representing an AWBW map."""

    id: int
    pref_ids: Dict[Tier, int]

    @property
    def uid(self):
        return self.id

    @property
    def tiers(self):
        return self.pref_ids.keys()

    @staticmethod
    def from_dict(dict: Dict[str, Any]):
        return Map(**dict)


@dataclass
class MapPool(UniqueDictionaryLike, DataclassDictionaryLike):
    """An object representing a collection of AWBW maps."""

    id: int
    name: str
    map_ids: Tuple[int]

    @property
    def uid(self):
        return self.id

    @staticmethod
    def from_dict(dict: Dict[str, Any]):
        return MapPool(**dict)
