from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict

from war_room.core.custom_types.interfaces import DataclassDictionaryLike, UniqueDictionaryLike


class Tier(Enum):
    """Enum for deciding tiers"""

    T0 = 'T0'
    T1 = 'T1'
    T2 = 'T2'
    T3 = 'T3'
    T4 = 'T4'


class MatchStatus(Enum):
    """Utility class for handling match statuses"""

    NOT_STARTED = 'not_started'
    ONGOING = 'ongoing'
    P1_WIN = 'p1_win'
    P2_WIN = 'p2_win'
    DRAW = 'draw'

    def is_completed(self) -> bool:
        return self in (MatchStatus.P1_WIN, MatchStatus.P2_WIN, MatchStatus.DRAW)

    def is_p1_win(self) -> bool:
        return self == MatchStatus.P1_WIN

    def is_draw(self) -> bool:
        return self == MatchStatus.DRAW


@dataclass
class MatchDescription:
    p1_user_id: int
    p2_user_id: int
    map_id: int
    tier: Tier
    pref_id: int


@dataclass
class Match(UniqueDictionaryLike, DataclassDictionaryLike):
    id: int
    p1_user_id: int
    p1_commander: str
    p2_user_id: int
    p2_commander: str
    map_id: int
    tier: Tier
    pref_id: int
    game_url: str
    status: MatchStatus = MatchStatus.NOT_STARTED

    @property
    def uid(self):
        return self.uid

    @staticmethod
    def from_dict(dict: Dict[str, Any]):
        return Match(**dict)
