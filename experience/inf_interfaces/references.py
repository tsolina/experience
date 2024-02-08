from typing import TYPE_CHECKING
from typing import Iterator

from experience.inf_interfaces import Reference
from experience.system import Collection
from experience.types.general import cat_variant

class References(Collection):
    def __init__(self, com):
        super().__init__(com, _child=Reference)
        self.references = com

    def item(self, i_index: cat_variant) -> Reference:
        return Reference(self.references.Item(i_index))

    def __getitem__(self, n: int) -> Reference:
        if (n + 1) > self.count:
            raise StopIteration

        return Reference(self.references.item(n + 1))

    def __iter__(self) -> Iterator[Reference]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'References(name="{self.name}")'
