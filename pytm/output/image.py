from .abstract import AbstractOutput


class ImageOutput(AbstractOutput):
    def __init__(self, path: str, description: str = None):
        self._path: str = path
        self._description: str = description

    @property
    def path(self) -> str:
        return self._path

    @property
    def description(self) -> str:
        return self._description

    def get_type(self) -> str:
        return 'image'

    def to_json(self) -> dict:
        return {
            'path': self._path,
            'description': self._description
        }
