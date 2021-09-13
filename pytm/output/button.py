from .abstract import AbstractOutput


class ButtonOutput(AbstractOutput):
    def __init__(self, index: int, name: str, action: str):
        super().__init__(index)

        self._name: str = name
        self._action: str = action

    @property
    def name(self) -> str:
        return self._name

    @property
    def action(self) -> str:
        return self._action

    def get_type(self) -> str:
        return 'button'

    def to_json(self) -> dict:
        return {
            **super().to_json(),
            'name': self._name,
            'action': self._action
        }
