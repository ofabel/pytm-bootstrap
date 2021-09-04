from enum import Enum


class FieldType(Enum):
    TEXT = 'text'
    PASSWORD = 'password'
    NUMBER = 'number'
    RANGE = 'range'

    def __str__(self):
        return self.value
