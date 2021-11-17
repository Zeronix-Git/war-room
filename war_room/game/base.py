from abc import ABC, abstractmethod

from option import Option, Result

from war_room.core.custom_types import Match
from war_room.core.custom_types.match import MatchDescription


class BaseGameHandler(ABC):
    """Base class for handling games."""

    @abstractmethod
    def create_game(self, match_desc: MatchDescription) -> Result[Match, str]:
        """Create a game"""
        pass

    @abstractmethod
    def get_game_info(self, id: int) -> Result[Option[Match], str]:
        """Get information about an ongoing game"""
        pass
