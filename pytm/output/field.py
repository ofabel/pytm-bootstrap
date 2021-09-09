from typing import Any
from typing import Dict
from typing import Union

from .abstract import AbstractOutput
from .field_type_enum import FieldType


class FieldOutput(AbstractOutput):
    def __init__(
            self,
            index: int,
            field_type: FieldType,
            name: str,
            value: Union[int, float, str] = None,
            **attrs: Union[int, float, str]
    ):
        super().__init__(index)

        self._type: FieldType = field_type
        self._name: str = name
        self._raw_value: Union[int, float, str] = value
        self._value = str(value)
        self._attributes: Dict[str, Union[int, float, str]] = attrs

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
            **super().to_json(),
            'type': self._type,
            'name': self._name,
            'value': self._value
        }
