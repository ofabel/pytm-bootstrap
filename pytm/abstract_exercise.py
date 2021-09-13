import abc

from .create_app import create_app
from .output import OutputBuilder as Output
from .output import Serializer


class AbstractExercise(abc.ABC):
    def __new__(cls, unique_id: str, secret: str, static_folder_path: str = None, *args, **kwargs):
        exercise: AbstractExercise = super().__new__(cls, *args, **kwargs)
        exercise._unique_id = unique_id
        exercise._serializer = Serializer(secret)

        return create_app(exercise, static_folder_path)

    @property
    def unique_id(self) -> str:
        return self._unique_id

    @property
    def output(self) -> Output:
        return Output(self._serializer)

    @abc.abstractmethod
    def start(self) -> Output:
        pass
