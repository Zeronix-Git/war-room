import random
from abc import ABC, abstractmethod
from typing import List, Tuple


class BaseGameCreationStrategy(ABC):
    @abstractmethod
    def select_map(self, map_ids: List[int]) -> int:
        pass

    @abstractmethod
    def select_pref(self, pref_ids: List[int]) -> int:
        pass

    @abstractmethod
    def select_player_order(self, users: Tuple[int, int]) -> Tuple[int, int]:
        pass


class RandomStrategy(BaseGameCreationStrategy):
    def select_map(self, map_ids: List[int]) -> int:
        return random.choice(map_ids)

    def select_pref(self, pref_ids: List[int]) -> int:
        return random.choice(pref_ids)

    def select_player_order(self, user_ids: Tuple[int, int]) -> Tuple[int, int]:
        return user_ids if random.choice([True, False]) else (user_ids[1], user_ids[0])
