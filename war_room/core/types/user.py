from dataclasses import dataclass, field

@dataclass
class User:
    id: int 
    game_count: int = 0
    rating: float = 800.0