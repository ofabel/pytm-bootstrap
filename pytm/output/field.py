from typing import Any
from typing import Dict
from typing import Union

from .abstract import AbstractOutput
from .field_type_enum import FieldType


class FieldOutput(AbstractOutput):
    def __init__(self, field_type: FieldType, name: str, value: Any = None, **attrs: Union[int, str]):
        self._type: FieldType = field_type
        self._name: str = name
        self._raw_value: Any = value
        self._value = str(value)
        self._attributes: Dict[str, Union[int, str]] = attrs

    @property
    def type(self) -> FieldType:
        return self._type

    @property
    def name(self) -> str:
        return self._name

    @property
    def raw_value(self) -> Any:
        return self._raw_value

    @property
    def value(self) -> str:
        return self._value

    @property
    def attributes(self) -> Dict[str, Union[int, str]]:
        return self._attributes

    def get_type(self) -> str:
        return 'field'

    def to_json(self) -> dict:
        return {
            **self._attributes,
            'type': str(self._type),
            'name': self._name,
            'value': self._value
        }