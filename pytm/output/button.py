from .abstract import AbstractOutput
from .serializer import Serializer


class ButtonOutput(AbstractOutput):
    def __init__(self, index: int, serializer: Serializer, name: str, action: str, additional_arguments: dict):
        super().__init__(index)

        self._serializer: Serializer = serializer
        self._name: str = name
        self._action: str = action
        self._additional_arguments: dict = additional_arguments

    @property
    def name(self) -> str:
        return self._name

    @property
    def action(self) -> str:
        return self._action

    @property
    def additional_arguments(self) -> dict:
        return self._additional_arguments

    def get_type(self) -> str:
        return 'button'

    def to_json(self) -> dict:
        signature, data = self._serializer.serialize(self._additional_arguments)
        return {
            **super().to_json(),
            'name': self._name,
            'action': self._action,
            'arguments': {
                'data': data,
                'signature': signature
            }
        }
