from typing import Union

from ..latex import Latex


class Option:
    def __init__(self, value: Union[str, int, float], label: Union[str, Latex]):
        self._value: Union[str, int, float] = value
        self._label: Union[str, Latex] = label

    @property
    def value(self) -> Union[str, int, float]:
        return self._value

    @property
    def label(self) -> Union[str, Latex]:
        return self._label

    def to_json(self) -> dict:
        return {
            'value': self._value,
            'label': Latex.marshal(self._label)
        }
