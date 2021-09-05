from typing import TYPE_CHECKING

from flask import Blueprint
from flask import Response
from flask import jsonify
from flask_cors import CORS

if TYPE_CHECKING:
    from .abstract_exercise import AbstractExercise


class API:
    def __init__(self, exercise: 'AbstractExercise'):
        self._exercise: 'AbstractExercise' = exercise
        self._blueprint: Blueprint = self._create_blueprint()

    @property
    def exercise(self) -> 'AbstractExercise':
        return self._exercise

    @property
    def blueprint(self) -> Blueprint:
        return self._blueprint

    def get_question(self) -> Response:
        question = self.exercise.get_question()
        return jsonify(question.to_json())

    def handle_answer(self) -> Response:
        answer = self.exercise.get_answer()
        return jsonify(answer.to_json())

    def _create_blueprint(self) -> Blueprint:
        api: Blueprint = Blueprint('api', __name__)

        CORS(api)

        api.add_url_rule('/question', 'question', self.get_question, True, methods=['GET'])
        api.add_url_rule('/answer', 'answer', self.handle_answer, True, methods=['POST'])

        return api
