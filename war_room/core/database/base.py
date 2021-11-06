from abc import ABC, abstractmethod
from option import Option, Result
from war_room.core.types import User, Match

class UserDatabase(ABC):

    @abstractmethod
    def get_user(self, id: int) -> Result[Option[User], str]:
        """ Get a user by their unique ID. """
        pass

    def contains_user(self, id: int) -> Result[bool, str]:
        return self.get_user(id).map(
            lambda maybe_user: maybe_user.is_some
        )

    @abstractmethod
    def update_user(self, user: User) -> Result[None, str]:
        """ Update a user's data in the database. 
        
        If the user does not already exist, this function should create a new user.
        If the user already exists, this function should update that user's information
        without creating a duplicate. """
        pass

class MatchDatabase(ABC):

    @abstractmethod
    def get_match(self, match_id: int) -> Option[Match]:
        pass

    def contains_match(self, match_id: int) -> bool:
        return self.get_match(match_id).is_some()

    @abstractmethod
    def update_match(self, match: Match) -> Result:
        pass    
