from typing import Iterator

from experience.inf_interfaces.window import Window
from experience.system.collection import Collection
from experience.types.general import cat_variant

class Windows(Collection):
    def __init__(self, com):
        super().__init__(com, _child=Window)
        self.windows = com

    def arrange(self, i_style: int) -> None:
        return self.windows.Arrange(i_style)

    def item(self, i_index: cat_variant) -> Window:
        return Window(self.windows.Item(i_index))

    def __getitem__(self, n: int) -> Window:
        if (n + 1) > self.count:
            raise StopIteration

        return Window(self.windows.item(n + 1))

    def __iter__(self) -> Iterator[Window]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'Windows(name="{self.name}")'
