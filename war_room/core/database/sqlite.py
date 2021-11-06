from os import stat
import sqlite3
from contextlib import closing
from typing import Tuple
from war_room.core.user import User
from war_room.core.database.base import UserDatabase
from war_room.utils.utils import mkdir_and_touch

class SQLiteUserDatabase(UserDatabase):
    
    def __init__(self, database_path: str):
        self._connection = sqlite3.connect(database_path)

        with self._connection as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                discord_id INT PRIMARY KEY,
                game_count INT,
                rating FLOAT);
            """)

    @staticmethod
    def _user_to_record(user: User) -> Tuple:
        return (user.discord_id, user.game_count, user.rating)

    @staticmethod
    def _record_to_user(record: Tuple) -> User:
        return User(
            discord_id = record[0],
            game_count = record[1],
            rating = record[2]
        )
    
    def contains_user(self, discord_id: int):
        with closing(self._connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM users WHERE discord_id = ?", (discord_id,))
            data = cursor.fetchone()
            return data is not None

    def register_user(self, discord_id: int):
        user = User(discord_id = discord_id)
        with closing(self._connection.cursor()) as cursor:
            cursor.execute(
                "INSERT INTO users (discord_id, game_count, rating) VALUES (?,?,?)", 
                (user.discord_id, user.game_count, user.rating)
            )
    
    def get_user(self, discord_id: int):
        with closing(self._connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM users WHERE discord_id = ?", (discord_id,))
            record = cursor.fetchone()
            return self._record_to_user(record)

    def update_user_information(self, user: User) -> None:
        with closing(self._connection.cursor()) as cursor:
            cursor.execute(
                "UPDATE users SET discord_id = :discord_id, game_count = :game_count, rating = :rating WHERE discord_id = :discord_id", 
                {
                    'discord_id': user.discord_id,
                    'game_count': user.game_count,
                    'rating': user.rating
                }
            )
    