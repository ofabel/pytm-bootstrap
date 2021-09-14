from typing import List
from typing import Optional
from typing import Union

from .abstract import AbstractOutput
from .field_attribute import FieldAttribute
from .option import Option
from ..latex import Latex


class OptionGroupOutput(AbstractOutput):
    def __init__(
            self,
            index: int,
            name: str,
            label: Union[str, Latex, None],
            options: List[Union[Option, str, int, float]],
            value: Union[str, int, float] = None,
            required: bool = False,
            inline: bool = True
    ):
        super().__init__(index)

        self._name: str = name
        self._label: Union[str, Latex, None] = label
        self._options: List[Option] = [] if options is None else map(self._normalize_option, options)
        self._value: Optional[Union[str, int, float]] = value
        self._required: bool = required
        self._inline: bool = inline

    @property
    def name(self) -> str:
        return self._name

    @property
    def label(self) -> Union[str, Latex, None]:
        return self._label

    @property
    def options(self) -> List[Option]:
        return self._options

    @property
    def value(self) -> Optional[Union[str, int, float]]:
        return self._value

    @property
    def inline(self) -> bool:
        return self._inline

    @property
    def required(self) -> bool:
        return self._required

    def get_type(self) -> str:
        return 'option-group'

    def to_json(self) -> dict:
        return {
            **super().to_json(),
            FieldAttribute.NAME: self._name,
            'label': Latex.marshal(self._label),
            'options': list(map(lambda option: option.to_json(), self._options)),
            'inline': self._inline,
            FieldAttribute.VALUE: self._value,
            FieldAttribute.REQUIRED: self._required
        }

    @staticmethod
    def _normalize_option(option: Union[Option, str, int, float]) -> Option:
        return option if isinstance(option, Option) else Option(option, str(option))
