import abc

from .create_app import create_app
from .output import OutputBuilder as Output


class AbstractExercise(abc.ABC):
    def __new__(cls, unique_id: str, static_folder_path: str = None, *args, **kwargs):
        exercise: AbstractExercise = super().__new__(cls, *args, **kwargs)
        exercise._unique_id = unique_id

        return create_app(exercise, static_folder_path)

    @property
    def unique_id(self) -> str:
        return self._unique_id

    @abc.abstractmethod
    def get_question(self) -> Output:
        pass

    @abc.abstractmethod
    def get_answer(self) -> Output:
        pass
