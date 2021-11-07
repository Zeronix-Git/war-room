from abc import ABC, abstractmethod
from typing import List, Tuple

from war_room.core.custom_types import User


class BaseMatchmakingStrategy(ABC):
    @abstractmethod
    def generate_matches(self, users: List[User]) -> List[Tuple[User, User]]:
        """Given a 2N-len multi-list of users, generate N pairings of matches"""
        pass


class RatingDifferenceMatchmakingStrategy(BaseMatchmakingStrategy):
    """Generates matches by minimizing the difference in rating"""

    def generate_matches(self, users: List[User]) -> List[Tuple[User, User]]:
        if len(users) % 2 != 0:
            users = users[:-1]

        matches = []
        users.sort(key=lambda user: user.rating)
        while len(users) > 0:
            user1 = users.pop(0)
            for index, user2 in enumerate(users):
                if user2.id != user1.id:
                    break
            user2 = users.pop(index)
            matches.append((user1, user2))

        return matches
