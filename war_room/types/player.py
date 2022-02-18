from dataclasses import dataclass

@dataclass
class Player:
    discord_id: int # discord.Member.id
    rating: float