from typing import Any
from typing import Callable
from typing import List
from typing import Union

from .abstract import AbstractOutput
from .button import ButtonOutput
from .field import FieldOutput
from .field_attribute import FieldAttribute
from .field_type_enum import FieldType
from .image import ImageOutput
from .option import Option
from .option_group import OptionGroupOutput
from .paragraph import ParagraphOutput
from ..latex import Latex
from ..serializer import Serializer


class OutputBuilder:
    def __init__(self, serializer: Serializer):
        self._serializer: Serializer = serializer
        self._output: list[AbstractOutput] = []

    @property
    def _index(self):
        return len(self._output)

    def add_paragraph(self, text: Union[str, Latex]) -> 'OutputBuilder':
        """Add a paragraph to the output. Can be used for normal text output.

        :param text: The text to print.
        :return: The current output builder instance.
        """
        paragraph: ParagraphOutput = ParagraphOutput(self._index, text)

        self._output.append(paragraph)

        return self

    def add_latex(self, text: str) -> 'OutputBuilder':
        """Add LaTeX to the output.

        :param text: The text to print.
        :return: The current output builder instance.
        """
        paragraph: ParagraphOutput = ParagraphOutput(self._index, Latex(text))

        self._output.append(paragraph)

        return self

    def add_image(self, path: str, description: str = None) -> 'OutputBuilder':
        """Add an image to the output. The path can either be absolute or relative to the working directory,
        which is normally the project root folder.

        :param path: The path to the image.
        :param description: An optional description of the image.
        :return: The current output builder instance.
        """
        image: ImageOutput = ImageOutput(self._index, path, description)

        self._output.append(image)

        return self

    def add_text_field(
            self,
            name: str,
            label: Union[str, Latex],
            value: str = None,
            required: bool = None,
            max_length: int = None
    ) -> 'OutputBuilder':
        """Add a text input field. The input will be handled as string.
        Use :meth:`add_number_field` to add a numeric input field.

        :param name: The name of the text field, should be unique.
        :param label: The label for the text field.
        :param value: The default value to display.
        :param required: Mark the field as required.
        :param max_length: The maximum length of this text field.
        :return: The current output builder instance.
        """
        field: FieldOutput = FieldOutput(self._index, FieldType.TEXT, name, label, value, **{
            FieldAttribute.REQUIRED: required,
            FieldAttribute.MAX_LENGTH: max_length
        })

        self._output.append(field)

        return self

    def add_number_field(
            self,
            name: str,
            label: Union[str, Latex],
            value: float,
            required: bool = None,
            min_value: float = None,
            max_value: float = None,
            step: float = None
    ) -> 'OutputBuilder':
        """Add a numeric input field. The input will be handled as float.
        Use :meth:`add_text_field` to add a text input field.

        :param name: The name of the input field, should be unique.
        :param label: The label for the input field.
        :param value: The default value to display.
        :param required: Mark the field as required.
        :param min_value: The minimum value to accept.
        :param max_value: The maximum value to accept.
        :param step: The granularity of the input.
        :return: The current output builder instance.
        """
        field: FieldOutput = FieldOutput(self._index, FieldType.NUMBER, name, label, str(value), **{
            FieldAttribute.REQUIRED: required,
            FieldAttribute.MIN: min_value,
            FieldAttribute.MAX: max_value,
            FieldAttribute.STEP: step
        })

        self._output.append(field)

        return self

    def add_option_group(
            self,
            name: str,
            label: Union[str, Latex],
            options: List[Union[Option, str, int, float]],
            value: Any = None,
            required: bool = False
    ) -> 'OutputBuilder':
        """Add a dropdown field. The user can choose between the provided options.

        :param name: The name of the input field, should be unique.
        :param label: The label for the input field, should be unique.
        :param options: A list of available options to choose from.
        :param value: The default value to display.
        :param required: Mark the field as required.
        :return: The current output builder instance.
        """
        option_group: OptionGroupOutput = OptionGroupOutput(self._index, name, label, options, value, required)

        self._output.append(option_group)

        return self

    def add_action(self, title: str, action: Callable[..., 'OutputBuilder'], **kwargs) -> 'OutputBuilder':
        """Add an action button. Creates a button, if the user clicks on it, he will be redirected to the specified
        action. The action should be a method reference to another action in the exercise class.

        :param title: The title for the button, e.g. Submit.
        :param action: A method reference to the next action.
        :param kwargs: Additional arguments to pass to the action method.
        :return: The current output builder instance.
        """
        button: ButtonOutput = ButtonOutput(self._index, self._serializer, title, action.__name__, kwargs)

        self._output.append(button)

        return self

    def to_json(self) -> List[dict]:
        return list(map(self._output_to_json, self._output))

    @staticmethod
    def _output_to_json(output: AbstractOutput) -> dict:
        return {
            **output.to_json(),
            '_type': output.get_type()
        }
