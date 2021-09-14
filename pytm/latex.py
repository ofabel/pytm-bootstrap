class Latex:
    def __init__(self, code: str):
        self._code: str = code

    @property
    def code(self) -> str:
        return self._code

    def to_json(self) -> dict:
        return {
            'code': self._code
        }
