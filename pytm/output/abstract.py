import abc


class AbstractOutput(abc.ABC):
    @abc.abstractmethod
    def get_type(self) -> str:
        pass

    @abc.abstractmethod
    def to_json(self) -> dict:
        pass
