import abc

from .create_app import create_app
from .output import OutputBuilder as Output


class AbstractExercise(abc.ABC):
    def __new__(cls, static_folder_path: str = None, *args, **kwargs):
        exercise: AbstractExercise = super().__new__(cls, *args, **kwargs)

        return create_app(exercise, static_folder_path)

    @abc.abstractmethod
    def get_question(self) -> Output:
        pass

    @abc.abstractmethod
    def get_answer(self) -> Output:
        pass
