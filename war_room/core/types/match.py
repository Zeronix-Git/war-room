from dataclasses import dataclass
from typing import Dict, Any
from war_room.core.types.interfaces import DataclassDictionaryLike, Unique

class MatchStatus:
    """ Utility class for handling match statuses """
    NOT_STARTED = 'not_started'
    ONGOING = 'ongoing'
    COMPLETED = 'completed'
    
    @staticmethod
    def is_valid(status: str) -> bool:
        return status in (MatchStatus.NOT_STARTED, MatchStatus.ONGOING, MatchStatus.COMPLETED)

@dataclass
class Match(Unique, DataclassDictionaryLike):
    id: int
    p1_user_id: int
    p2_user_id: int
    tier: int
    status: MatchStatus = MatchStatus.NOT_STARTED

    @property
    def uid(self):
        return self.uid

    @staticmethod
    def from_dict(dict: Dict[str, Any]):
        return Match(**dict)