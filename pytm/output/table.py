from typing import List
from typing import Union

from .abstract import AbstractOutput


class TableOutput(AbstractOutput):
    def __init__(self, index: int, data: List[List[Union[str, int, float]]]):
        super().__init__(index)

        self._data: List[List[Union[str, int, float]]] = data

    @property
    def data(self) -> List[List[Union[str, int, float]]]:
        return self._data

    def get_type(self) -> str:
        return 'table'

    def to_json(self) -> dict:
        return {
            **super().to_json(),
            'data': self._data
        }
