import random
import enum
import typing
from uuid import uuid4
from war_room.types import player

def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

class PlayerStatus(enum.Enum):
    MATCHED = 'MATCHED'
    WAITING = 'WAITING'

MatchId = typing.NewType('MatchId', str)

class Match:

    def __init__(self, player1: player.Player, player2: player.Player):
        self.id = Match.generate_match_id()
        self.player1, self.player2 = Match.shuffle_players(player1, player2)

    def shuffle_players(player1, player2) -> typing.Tuple[player.Player, player.Player]:
        players = [player1, player2]
        random.shuffle(players)
        return players[0], players[1]

    @staticmethod 
    def generate_match_id() -> MatchId:
        return uuid4().hex

class Matchmaker:
    
    def __init__(self):
        self.active_players: typing.Dict[player.Player, PlayerStatus] = {}
        self.active_matches: typing.Dict[MatchId, Match] = {}

    def add_player(self, player: player.Player):
        self.active_players[player] = PlayerStatus.WAITING

    def remove_player(self, player: player.Player):
        del self.active_players[player]

    def match_active_players(self):
        # Sort players in ascending order by rating 
        waiting_players = list(self.active_players.keys())
        waiting_players.sort(key = lambda x: x.rating)
        for player1, player2 in pairwise(waiting_players):
            self.start_match(Match(player1, player2))

    def start_match(self, match: Match) -> MatchId:
        self.active_matches[match.id] = match
        self.pool[match.player1] = PlayerStatus.MATCHED
        self.pool[match.player2] = PlayerStatus.MATCHED
        return match.id

    def end_match(self, match_id: MatchId):
        match = self.active_matches[match_id]
        self.remove_player(match.player1)
        self.remove_player(match.player2)
        del self.active_matches[match_id]


