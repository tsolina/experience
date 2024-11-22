from typing import Iterator, TYPE_CHECKING

from experience.inf_interfaces.inf_types import *
from experience.inf_interfaces import Window
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class Windows(Collection):
    def __init__(self, com):
        super().__init__(com, child=Window)
        self.windows = com

    def arrange(self, i_style: CatArrangeStyle) -> None:
        return self.windows.Arrange(int(i_style))

    def item(self, i_index: 'cat_variant') -> Window:
        return Window(self.windows.Item(i_index))

    def __getitem__(self, n: int) -> Window:
        if (n + 1) > self.count():
            raise StopIteration

        return Window(self.windows.item(n + 1))

    def __iter__(self) -> Iterator[Window]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'