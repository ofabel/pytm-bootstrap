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
        a = randint(2, 10)
        b = randint(2, 10)
        c = randint(1, 10)
        y = randint(0, 100)

        question = Latex(r'''
            What are the solutions of the following equation?
            \newline
            ${a}x^{p} + {b}x + {c} = {y}$
            '''.format(a=a, p=2, b=b, c=c, y=y))
        label = Latex(r'''
            What is the value of $x$ (with a precision of {e})?
            '''.format(e=self._epsilon))

        return self.output \
            .add_paragraph(question) \
            .add_number_field(name='answer',
                              label=label,
                              step=self._epsilon) \
            .add_action('Solve', self.solve, a=a, b=b, c=c, y=y)

    def solve(self, answer, a, b, c, y):
        x = (y - b) / y
        diff = abs(answer - x)
        correct = 'right' if diff < self._epsilon else 'wrong'

        return self.output \
            .add_paragraph(f'Your answer {answer} is: {correct}') \
            .add_action('Back to start', self.start)


app = Exercise()
