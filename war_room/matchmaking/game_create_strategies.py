import random
from abc import ABC, abstractmethod
from typing import List, Tuple

from war_room.core.custom_types.match import Tier


class BaseGameCreationStrategy(ABC):
    @abstractmethod
    def select_map(self, map_ids: List[int]) -> int:
        pass

    @abstractmethod
    def select_tier(self, tiers: List[Tier]) -> Tier:
        pass

    @abstractmethod
    def select_player_order(self, users: Tuple[int, int]) -> Tuple[int, int]:
        pass


class RandomStrategy(BaseGameCreationStrategy):
    def select_map(self, map_ids: List[int]) -> int:
        return random.choice(map_ids)

    def select_tier(self, tiers: List[Tier]) -> Tier:
        return random.choice(tiers)

    def select_player_order(self, user_ids: Tuple[int, int]) -> Tuple[int, int]:
        return user_ids if random.choice([True, False]) else (user_ids[1], user_ids[0])
