from abc import ABC
from abc import abstractmethod


class AbstractOutput(ABC):
    @abstractmethod
    def get_type(self) -> str:
        pass

    @abstractmethod
    def to_json(self) -> dict:
        pass
