from typing import Any, List, Tuple

from war_room.core.custom_types.map import MapPool, User
from war_room.core.custom_types.match import MatchDescription
from war_room.core.database.base import MatchDatabase, UserDatabase
from war_room.matchmaking.game_create_strategies import BaseGameCreationStrategy, RandomStrategy
from war_room.matchmaking.matching_strategies import BaseMatchmakingStrategy, RatingDifferenceMatchmakingStrategy


class MatchmakingHandler:
    def __init__(
        self,
        user_db: UserDatabase,
        match_db: MatchDatabase,
        map_db: Any,
        map_pool: MapPool,
        matchmakinging_strategy: BaseMatchmakingStrategy = RatingDifferenceMatchmakingStrategy(),
        game_creation_strategy: BaseGameCreationStrategy = RandomStrategy(),
    ):
        self.user_db = user_db
        self.match_db = match_db
        self.map_db = map_db
        self.map_pool = map_pool
        self.matchmaking_strategy = matchmakinging_strategy
        self.game_creation_strategy = game_creation_strategy

    def _generate_user_multilist(self) -> List[Tuple[User, User]]:
        """Generate a multi-list of users with unfilled games.

        If a user has K unfilled games, they appear in the list K times."""
        multilist = []
        for maybe_user in self.user_db:
            if maybe_user.is_ok:
                user = maybe_user
                desired_game_count = user.game_count
                active_game_count = self.map_db.get_user_active_game_count(user.id)
                for _ in range(desired_game_count - active_game_count):
                    multilist.append(user)
            else:
                break

        return multilist

    def _generate_match_desc(self, users: Tuple[User, User]) -> MatchDescription:
        """Generate a match description for a game between two users.

        This can be passed to users for manual game creation, or to a script for
        automatic game creation."""
        user_ids = (users[0].id, users[1].id)
        p1_user_id, p2_user_id = self.game_creation_strategy.select_player_order(user_ids)
        map_id = self.game_creation_strategy.select_map(self.map_pool.map_ids)
        map = self.map_db.get(map_id)
        tier = self.game_creation_strategy.select_tier(map.tiers)
        pref_id = map.pref_ids[tier]

        return MatchDescription(p1_user_id=p1_user_id, p2_user_id=p2_user_id, map_id=map_id, tier=tier, pref_id=pref_id)
