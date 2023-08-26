from pytmlib import AbstractExercise
from pytmlib import entrypoint
from pytmlib import Latex


class Exercise(AbstractExercise):
    @property
    def version(self) -> str:
        return '0.1.0'

    @entrypoint
    def start(self):
        question = Latex(r'''
            What is the solution of the following equation?
            \newline
            $$2x + 4 = 10$$
            ''')
        label = Latex(r'What is the value of $x$?')

        return self.output \
            .add_paragraph(question) \
            .add_number_field(name='answer', label=label) \
            .add_action('Solve', self.solve)

    def solve(self, answer):
        correct = 'right' if answer == 3 else 'wrong'

        return self.output \
            .add_paragraph(f'Your answer {answer} is: {correct}') \
            .add_action('Back to start', self.start)


app = Exercise()
