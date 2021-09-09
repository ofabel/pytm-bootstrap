from .abstract import AbstractOutput


class ParagraphOutput(AbstractOutput):
    def __init__(self, index: int, text: str):
        super().__init__(index)

        self._text: str = text

    @property
    def text(self) -> str:
        return self._text

    def get_type(self) -> str:
        return 'paragraph'

    def to_json(self) -> dict:
        return {
            **super().to_json(),
            'text': self._text
        }
