from enum import Enum
from typing import TypeVar

T = TypeVar('T', bound=Enum)

class EnumItem(Enum):
    @classmethod
    def item(cls, i_index: int) -> T:
        for en in cls:
            if en.value == i_index:
                return en
        raise ValueError(f"No enum member with value {i_index}")