from dataclasses import dataclass
from typing import Any, Dict

from war_room.core.custom_types.interfaces import DataclassDictionaryLike, UniqueDictionaryLike


class MatchStatus:
    """Utility class for handling match statuses"""

    NOT_STARTED = 'not_started'
    ONGOING = 'ongoing'
    COMPLETED = 'completed'

    @staticmethod
    def is_valid(status: str) -> bool:
        return status in (MatchStatus.NOT_STARTED, MatchStatus.ONGOING, MatchStatus.COMPLETED)


@dataclass
class Match(UniqueDictionaryLike, DataclassDictionaryLike):
    id: int
    p1_user_id: int
    p2_user_id: int
    tier: int
    status: str = MatchStatus.NOT_STARTED

    @property
    def uid(self):
        return self.uid

    @staticmethod
    def from_dict(dict: Dict[str, Any]):
        return Match(**dict)
