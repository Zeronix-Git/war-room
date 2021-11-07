from dataclasses import dataclass
from typing import Any, Dict

from war_room.core.custom_types.interfaces import DataclassDictionaryLike, UniqueDictionaryLike


class MatchStatus:
    """Utility class for handling match statuses"""

    NOT_STARTED = 'not_started'
    ONGOING = 'ongoing'
    P1_WIN = 'p1_win'
    P2_WIN = 'p2_win'
    DRAW = 'draw'

    @staticmethod
    def is_valid(status: str) -> bool:
        return status in (
            MatchStatus.NOT_STARTED,
            MatchStatus.ONGOING,
            MatchStatus.P1_WIN,
            MatchStatus.P2_WIN,
            MatchStatus.DRAW,
        )

    @staticmethod
    def is_completed(status: str) -> bool:
        return status in (MatchStatus.P1_WIN, MatchStatus.P2_WIN, MatchStatus.DRAW)


@dataclass
class MatchDescription:
    p1_user_id: int
    p2_user_id: int
    map_id: int
    pref_id: int


@dataclass
class Match(UniqueDictionaryLike, DataclassDictionaryLike):
    id: int
    p1_user_id: int
    p1_commander: str
    p2_user_id: int
    p2_commander: str
    map_id: int
    pref_id: int
    game_url: str
    status: str = MatchStatus.NOT_STARTED

    @property
    def uid(self):
        return self.uid

    @staticmethod
    def from_dict(dict: Dict[str, Any]):
        return Match(**dict)
