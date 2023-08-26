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
        m_1 = randint(2, 5)
        b_1 = randint(1, 10)

        m_2 = randint(6, 10)
        b_2 = randint(1, 10)

        line_1 = r'$$f_{1}(x) = \frac{x}{%d} + {%d}$$' % (m_1, b_1)
        line_2 = r'$$f_{2}(x) = \frac{x}{%d} + {%d}$$' % (m_2, b_2)

        question = Latex(r'''
            What is the intersection point $(x,y)$ of the two lines?
            \newline
            {line1}
            {line2}
            '''.format(line1=line_1, line2=line_2))
        label_x = Latex(r'''
            What is the value of $x$ (with a precision of {e})?
            '''.format(e=self._epsilon))
        label_y = Latex(r'''
            What is the value of $y$ (with a precision of {e})?
            '''.format(e=self._epsilon))

        return self.output \
            .add_paragraph(question) \
            .add_number_field(name='x',
                              label=label_x,
                              step=self._epsilon) \
            .add_number_field(name='y',
                              label=label_y,
                              step=self._epsilon) \
            .add_action('Solve', self.solve,
                        m_1=m_1,
                        b_1=b_1,
                        m_2=m_2,
                        b_2=b_2)

    def solve(self, **kwargs):
        score = self.check(**kwargs)

        return self.output \
            .add_score(score) \
            .add_paragraph(f'Your score: {score}') \
            .add_action('Back to start', self.start)

    @classmethod
    def check(cls, x, y, m_1, b_1, m_2, b_2):
        x_correct = (b_2 - b_1) / (1 / m_1 - 1 / m_2)
        y_correct = x_correct / m_1 + b_1

        x_diff = abs(x - x_correct)
        y_diff = abs(y - y_correct)

        score = 0.0

        if x_diff < cls._epsilon:
            score += 0.5

        if y_diff < cls._epsilon:
            score += 0.5

        return score


app = Exercise()
