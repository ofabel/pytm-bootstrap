from typing import Any
from typing import List

from .abstract import AbstractOutput
from .dropdown import DropdownOutput
from .field import FieldOutput
from .field_attribute import FieldAttribute
from .field_type_enum import FieldType
from .image import ImageOutput
from .paragraph import ParagraphOutput


class OutputBuilder:
    def __init__(self):
        self._output: list[AbstractOutput] = []

    def add_paragraph(self, text: str) -> 'OutputBuilder':
        self._output.append(ParagraphOutput(text))

        return self

    def add_image(self, path: str, description: str = None) -> 'OutputBuilder':
        self._output.append(ImageOutput(path, description))

        return self

    def add_text_field(self, name: str, value: str = None, required: bool = None,
                       max_length: int = None) -> 'OutputBuilder':
        self._output.append(FieldOutput(FieldType.TEXT, name, value, **{
            FieldAttribute.REQUIRED: required,
            FieldAttribute.MAX_LENGTH: max_length
        }))

        return self

    def add_number_field(self, name: str, value: float, required: bool = None, min_value: float = None,
                         max_value: float = None, step: float = None) -> 'OutputBuilder':
        self._output.append(FieldOutput(FieldType.NUMBER, name, str(value), **{
            FieldAttribute.REQUIRED: required,
            FieldAttribute.MIN: min_value,
            FieldAttribute.MAX: max_value,
            FieldAttribute.STEP: step
        }))

        return self

    def add_dropdown(self, name: str, options: List[Any], value: Any = None, required: bool = False) -> 'OutputBuilder':
        self._output.append(DropdownOutput(name, options, value, required))

        return self

    def to_json(self) -> List[dict]:
        return list(map(self._output_to_json, self._output))

    @staticmethod
    def _output_to_json(output: AbstractOutput) -> dict:
        return {
            **output.to_json(),
            '_type': output.get_type()
        }
