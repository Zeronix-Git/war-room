import sqlite3
from contextlib import closing
from typing import Tuple
from war_room.core.types import User
from option import Option, Result
from war_room.core.database.base import UserDatabase

class SQLiteUserDatabase(UserDatabase):
    
    def __init__(self, database_path: str):
        self._connection = sqlite3.connect(database_path)

        with self._connection as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                id INT PRIMARY KEY,
                game_count INT,
                rating FLOAT);
            """)

    @staticmethod
    def _user_to_record(user: User) -> Tuple:
        return (user.id, user.game_count, user.rating)

    @staticmethod
    def _record_to_user(record: Tuple) -> User:
        return User(
            id = record[0],
            game_count = record[1],
            rating = record[2]
        )
    
    def get_user(self, id: int) -> Result[Option[User], str]:
        try:
            with closing(self._connection.cursor()) as cursor:
                cursor.execute(
                    "SELECT * FROM users WHERE id = :id", 
                    {
                        'id': id,
                    }
                )
                record = cursor.fetchone()
                if record is None:
                    return Result.Ok(Option.NONE())
                else:
                    return Result.Ok(Option.Some(self._record_to_user(record)))
        except sqlite3.Error as e:
            return Result.Err(str(e))

    def update_user(self, user: User) -> Result[None, str]:
        return self.contains_user(user.id).map(
            lambda contains_user: self._update_existing_user(user) if contains_user else self._add_new_user(user)
        )

    def _add_new_user(self, user: User) -> Result[None, str]:
        try:
            with closing(self._connection.cursor()) as cursor:
                cursor.execute(
                    "INSERT INTO users (id, game_count, rating) VALUES (:id, :game_count, :rating);", 
                    {
                        'id': user.id,
                        'game_count': user.game_count,
                        'rating': user.rating
                    }
                )
            return Result.Ok(None)

        except sqlite3.Error as e:
            return Result.Err(str(e))   

    def _update_existing_user(self, user: User) -> Result[None, str]:      
            try:
                with closing(self._connection.cursor()) as cursor:
                    cursor.execute(
                        "UPDATE users SET id = :id, game_count = :game_count, rating = :rating WHERE id = :id", 
                        {
                            'id': user.id,
                            'game_count': user.game_count,
                            'rating': user.rating
                        }
                    )
                    
                    return Result.Ok(None)
                    
            except sqlite3.Error as e:
                return Result.Err(str(e))
