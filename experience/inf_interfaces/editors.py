from typing import Iterator

from experience.inf_interfaces import Editor
from experience.system import Collection
from experience.types.general import cat_variant

class Editors(Collection):
    def __init__(self, com):
        super().__init__(com, _child=Editor)
        self.editors = com

    def item(self, i_index: cat_variant) -> 'Editor':
        return Window(self.editors.Item(i_index))

    def __getitem__(self, n: int) -> Editor:
        if (n + 1) > self.count:
            raise StopIteration

        return Window(self.editors.item(n + 1))

    def __iter__(self) -> Iterator[Editor]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'Editors(name="{self.name}")'
