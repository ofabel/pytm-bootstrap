import abc

from flask import Flask
from flask import jsonify

from .output import OutputBuilder as Output


class AbstractExercise(abc.ABC):
    def __new__(cls, *args, **kwargs):
        exercise: AbstractExercise = super().__new__(cls, *args, **kwargs)

        app = Flask(__name__)

        @app.get('/')
        def get():
            question = exercise.get_question()
            return jsonify(question.to_json())

        @app.post('/')
        def post():
            answer = exercise.get_answer()
            return jsonify(answer.to_json())

        return app

    @abc.abstractmethod
    def get_question(self) -> Output:
        pass

    @abc.abstractmethod
    def get_answer(self) -> Output:
        pass
