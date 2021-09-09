from typing import Any
from typing import List

from .abstract import AbstractOutput
from .field_attribute import FieldAttribute


class DropdownOutput(AbstractOutput):
    def __init__(self, index: int, name: str, options: List[Any], value: Any = None, required: bool = False):
        super().__init__(index)

        self._name: str = name
        self._raw_options: List[Any] = options
        self._options: List[str] = list(map(lambda item: str(item), options))
        self._raw_value: Any = value
        self._value: str = str(value)
        self._required: bool = required

    @property
    def name(self) -> str:
        return self._name

    @property
    def raw_options(self) -> List[Any]:
        return self._raw_options

    @property
    def options(self) -> List[str]:
        return self._options

    @property
    def raw_value(self) -> Any:
        return self._raw_value

    @property
    def value(self) -> str:
        return self._value

    @property
    def required(self) -> bool:
        return self._required

    def get_type(self) -> str:
        return 'dropdown'

    def to_json(self) -> dict:
        return {
            **super().to_json(),
            FieldAttribute.NAME: self._name,
            'options': self._options,
            FieldAttribute.VALUE: self._value,
            FieldAttribute.REQUIRED: self._required
        }
