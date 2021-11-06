from abc import ABC, abstractmethod
from typing import Dict, Any
from dataclasses import dataclass, asdict

class Unique(ABC):
    """ Abstract base class for an object with a unique ID """
    @property
    @abstractmethod
    def uid(self):
        pass 

class DictionaryLike(ABC):
    """ Abstract base class for an object which can be converted to / from a dictionary """

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass 

    @staticmethod
    @abstractmethod
    def from_dict(dict: Dict[str, Any]) -> 'DictionaryLike':
        pass

@dataclass
class DataclassDictionaryLike(DictionaryLike):

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @staticmethod
    @abstractmethod
    def from_dict(dict: Dict[str, Any]):
        pass
