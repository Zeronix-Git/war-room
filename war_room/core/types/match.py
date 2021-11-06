from dataclasses import dataclass, field

from _pytest.mark.structures import MARK_GEN

class MatchStatus:
    """ Utility class for handling match statuses """
    NOT_STARTED = 'not_started'
    ONGOING = 'ongoing'
    COMPLETED = 'completed'
    
    @staticmethod
    def is_valid(status: str) -> bool:
        return status in (MatchStatus.NOT_STARTED, MatchStatus.ONGOING, MatchStatus.COMPLETED)

@dataclass
class Match:
    id: int
    p1_user_id: int
    p2_user_id: int
    tier: int
    status: MatchStatus = MatchStatus.NOT_STARTED