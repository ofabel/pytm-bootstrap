import abc

from .context import Context
from .create_app import create_app
from .output import OutputBuilder as Output


class AbstractExercise(abc.ABC):
    def __new__(cls, unique_id: str, secret: str, static_folder_path: str = None, *args, **kwargs):
        exercise: AbstractExercise = super().__new__(cls, *args, **kwargs)
        context: Context = Context(unique_id, secret, exercise)
        exercise._context = context

        return create_app(context, static_folder_path)

    @property
    def output(self) -> Output:
        return self._context.output

    @abc.abstractmethod
    def start(self) -> Output:
        pass
