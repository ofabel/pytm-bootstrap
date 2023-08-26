from random import randint

from pytmlib import AbstractExercise
from pytmlib import Latex
from pytmlib import entrypoint


class Exercise(AbstractExercise):
    _epsilon = 0.01

    @property
    def version(self) -> str:
        return '0.1.0'

    @entrypoint
    def start(self):
        y = randint(0, 100)
        b = randint(1, 100)
        m = randint(2, 100)

        question = Latex(r'''
            What is the solution of the following equation?
            \newline
            ${m}x + {b} = {y}$
            '''.format(m=m, b=b, y=y))
        label = Latex(r'''
            What is the value of $x$ (with a precision of {e})?
            '''.format(e=self._epsilon))

        return self.output \
            .add_paragraph(question) \
            .add_number_field(name='answer',
                              label=label,
                              step=self._epsilon) \
            .add_action('Solve', self.solve, m=m, b=b, y=y)

    def solve(self, answer, **kwargs):
        correct = 'right' if self.check(answer, **kwargs) else 'wrong'

        return self.output \
            .add_paragraph(f'Your answer {answer} is: {correct}') \
            .add_action('Back to start', self.start)

    @classmethod
    def check(cls, answer, m, b, y):
        x = (y - b) / m
        diff = abs(answer - x)

        return diff < cls._epsilon


app = Exercise()
