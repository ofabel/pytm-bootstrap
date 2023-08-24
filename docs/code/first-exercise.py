from pytmlib import AbstractExercise
from pytmlib import entrypoint


class Exercise(AbstractExercise):
    @property
    def version(self) -> str:
        return '0.1.0'

    @entrypoint
    def start(self):
        return self.output.add_paragraph('hello from pytmlib')


app = Exercise()
