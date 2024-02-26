from enum import Enum
from typing import TypeVar

T = TypeVar('T', bound=Enum)

class EnumString(Enum):
    @classmethod
    def item(cls, i_index: str) -> T:
        for en in cls:
            if en.value == i_index:
                return en
        raise ValueError(f"No enum member with value {i_index}")

    def __str__(self):
        return self.value

    def __eq__(self, value: 'EnumString') -> bool:
        return self.value == str(value)

if __name__ == "__main__":
    class Test(EnumString):
        First = 'First'
        Second = 'Second'

    some = Test.First
    print(str(some), some == Test.Second, some != "First")
    print(some)
