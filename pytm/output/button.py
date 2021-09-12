from .abstract import AbstractOutput


class ButtonOutput(AbstractOutput):
    def __init__(self, index: int, name: str):
        super().__init__(index)

        self._name: str = name

    @property
    def name(self) -> str:
        return self._name

    def get_type(self) -> str:
        return 'button'

    def to_json(self) -> dict:
        return {
            **super().to_json(),
            'name': self._name,
        }
