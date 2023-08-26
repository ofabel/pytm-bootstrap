from collections import namedtuple
from math import sqrt
from random import randint

from matplotlib.figure import Figure
from matplotlib.patches import Polygon
from pytmlib import AbstractExercise
from pytmlib import Latex
from pytmlib import entrypoint

Triangle = namedtuple('Triangle', 'a_x a_y b_x b_y c_x c_y')


class Exercise(AbstractExercise):
    _epsilon = 0.01

    @property
    def version(self) -> str:
        return '0.1.0'

    @entrypoint
    def start(self):
        a_x = randint(1, 9)
        a_y = randint(1, 9)

        b_x = randint(11, 19)
        b_y = randint(11, 19)

        c_x = randint(11, 19)
        c_y = randint(1, 9)

        triangle = Triangle(a_x, a_y, b_x, b_y, c_x, c_y)

        figure = self._get_figure(*triangle)

        question = Latex(r'''
            What is the magnitude of the following vectors?
            Answer the question with a precision of {e}.
            '''.format(e=self._epsilon))

        return self.output \
            .add_paragraph(question) \
            .add_figure(figure) \
            .add_number_field(name='a_b',
                              label=Latex(r'''
                              $\lvert \overrightarrow{AB} \rvert$
                              '''),
                              step=self._epsilon) \
            .add_number_field(name='b_c',
                              label=Latex(r'''
                              $\lvert \overrightarrow{BC} \rvert$
                              '''),
                              step=self._epsilon) \
            .add_number_field(name='a_c',
                              label=Latex(r'''
                              $\lvert \overrightarrow{AC} \rvert$
                              '''),
                              step=self._epsilon) \
            .add_action('Solve', self.solve, **triangle._asdict())

    def solve(self, **kwargs):
        score = self.check(**kwargs)

        return self.output \
            .add_score(score) \
            .add_paragraph(f'Your score: {score}') \
            .add_action('Back to start', self.start)

    @classmethod
    def check(cls, a_b, b_c, a_c, a_x, a_y, b_x, b_y, c_x, c_y):
        scores = iter([0.0, 0.2, 0.5, 1.0])
        score = next(scores)
        edges = [
            [a_b, a_x, a_y, b_x, b_y],
            [b_c, b_x, b_y, c_x, c_y],
            [a_c, a_x, a_y, c_x, c_y]
        ]

        for points in edges:
            answer, *points = points
            length = cls._magnitude(*points)
            diff = abs(length - answer)

            if diff < cls._epsilon:
                score = next(scores)

        return score

    @staticmethod
    def _get_figure(a_x, a_y, b_x, b_y, c_x, c_y):
        figure = Figure()
        plot = figure.add_subplot(1, 1, 1)

        p_a = [a_x, a_y]
        p_b = [b_x, b_y]
        p_c = [c_x, c_y]

        triangle = Polygon(xy=[p_a, p_b, p_c],
                           lw=1.5,
                           edgecolor='red',
                           facecolor='white',
                           axes=plot)

        plot.add_patch(triangle)
        plot.text(a_x, a_y, 'A', ha='center', va='center', size=16)
        plot.text(b_x, b_y, 'B', ha='center', va='center', size=16)
        plot.text(c_x, c_y, 'C', ha='center', va='center', size=16)

        min_x = min(a_x, b_x, c_x) - 1
        min_y = min(a_y, b_y, c_y) - 1

        max_x = max(a_x, b_x, c_x) + 1
        max_y = max(a_y, b_y, c_y) + 1

        plot.set_xlim(min_x, max_x)
        plot.set_ylim(min_y, max_y)

        plot.grid(True, 'both', ls='--', lw=0.5)

        x_ticks = range(min_x, max_x)
        y_ticks = range(min_y, max_y)

        plot.set_xticks(x_ticks)
        plot.set_yticks(y_ticks)

        figure.tight_layout()

        return figure

    @staticmethod
    def _magnitude(x0, y0, x1, y1):
        x = x1 - x0
        y = y1 - y0

        return sqrt(x * x + y * y)


app = Exercise()
