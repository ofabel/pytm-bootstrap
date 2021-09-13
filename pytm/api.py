from base64 import b64encode
from typing import TYPE_CHECKING
from typing import Union

from flask import Blueprint
from flask import Response
from flask import jsonify
from flask_cors import CORS

from .archiver import Archiver

if TYPE_CHECKING:
    from .abstract_exercise import AbstractExercise
    from .output import OutputBuilder


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

    def handle_start(self) -> Response:
        result: 'OutputBuilder' = self.exercise.start()
        json: list = result.to_json()
        envelop = self._wrap_with_envelop(json)
        return jsonify(envelop)

    def handle_action(self, action: str) -> Response:
        method: callable = getattr(self.exercise, action, None)
        result: 'OutputBuilder' = method()
        json: list = result.to_json()
        envelop = self._wrap_with_envelop(json)
        return jsonify(envelop)

    def handle_upload(self) -> Response:
        data: bytes = Archiver('.').create_tar()
        mimetype: str = 'application/tar+gzip'
        b64_encoded_data: str = b64encode(data).decode('utf-8')
        data_uri: str = 'data:%s;base64,%s' % (mimetype, b64_encoded_data)

        json_data: dict = self._wrap_with_envelop(data_uri)

        return jsonify(json_data)

    def _create_blueprint(self) -> Blueprint:
        api: Blueprint = Blueprint('api', __name__)

        CORS(api)

        api.add_url_rule('/start', 'start', self.handle_start, methods=['GET'])
        api.add_url_rule('/call/{action}', 'call', self.handle_action, methods=['POST'])
        api.add_url_rule('/upload', 'upload', self.handle_upload, methods=['GET'])

        return api

    def _wrap_with_envelop(self, payload: Union[list, dict, str, int, float]) -> dict:
        return {
            'exercise_id': self._exercise.unique_id,
            'payload': payload
        }
