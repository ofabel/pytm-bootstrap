from base64 import b64encode
from inspect import Parameter
from inspect import Signature
from inspect import signature
from typing import Callable
from typing import TYPE_CHECKING
from typing import Union

from flask import Blueprint
from flask import Response
from flask import jsonify
from flask import request
from flask_cors import CORS

from .archiver import Archiver
from .context import Context

if TYPE_CHECKING:
    from .output import OutputBuilder


class API:
    def __init__(self, context: Context):
        self._context: Context = context
        self._blueprint: Blueprint = self._create_blueprint()

    @property
    def context(self) -> Context:
        return self._context

    @property
    def blueprint(self) -> Blueprint:
        return self._blueprint

    def handle_start(self) -> Response:
        result: 'OutputBuilder' = self.context.exercise.start()
        json: list = result.to_json()
        envelop = self._wrap_with_envelop(json)
        return jsonify(envelop)

    def handle_action(self, action: str) -> Response:
        method: Callable[..., 'OutputBuilder'] = getattr(self.context.exercise, action, None)
        payload: dict = request.json
        result: 'OutputBuilder' = self._call_action(method, payload)
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
        api.add_url_rule('/call/<action>', 'call', self.handle_action, methods=['POST'])
        api.add_url_rule('/upload', 'upload', self.handle_upload, methods=['GET'])

        return api

    def _wrap_with_envelop(self, payload: Union[list, dict, str, int, float]) -> dict:
        return {
            'exercise_id': self.context.unique_id,
            'payload': payload
        }

    def _call_action(self, method: Callable[..., 'OutputBuilder'], available_arguments: dict) -> 'OutputBuilder':
        method_signature: Signature = signature(method)
        arguments: dict = {}

        for key in method_signature.parameters.keys():
            parameter: Parameter = method_signature.parameters[key]
            self._apply_argument(parameter, arguments, available_arguments)

        return method(**arguments)

    @staticmethod
    def _apply_argument(parameter: Parameter, arguments: dict, available_arguments: dict):
        name: str = parameter.name
        is_positional_or_keyword: bool = parameter.kind is Parameter.POSITIONAL_OR_KEYWORD
        is_empty_default: bool = parameter.default is Parameter.empty
        is_argument_available: bool = name in available_arguments

        # ignore not present arguments with default value
        if is_positional_or_keyword and not is_empty_default and not is_argument_available:
            return

        # raise error on required arguments
        if is_positional_or_keyword and is_empty_default and not is_argument_available:
            raise RuntimeError('parameter %s is not available' % name)

        # apply standard arguments
        if parameter.kind == Parameter.POSITIONAL_OR_KEYWORD:
            arguments[name] = available_arguments.pop(name)
        # apply kwargs
        elif parameter.kind == Parameter.VAR_KEYWORD:
            arguments.update(**available_arguments)
