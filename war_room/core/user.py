from dataclasses import dataclass, field

@dataclass
class User:
    discord_id: int 
    game_count: int
    rating: float

    _discord_id: int = field(init=False, repr=False)
    _game_count: int = field(init=False, repr=False, default = 0)
    _rating: float = field(init=False, repr=False, default = 800.0)

    @property 
    def game_count(self) -> int:
        return self._game_count

    @game_count.setter
    def game_count(self, value: int) -> None:
        if type(value) is property:
            # initial value not specified, use default
            value = User._game_count
        self._game_count = value

    @property 
    def rating(self) -> float:
        return self._rating 

    @rating.setter
    def rating(self, value: float) -> None:
        if type(value) is property:
            # initial value not specified, use default
            value = User._rating
        self._rating = value