from typing import TYPE_CHECKING, Iterator

from experience.inf_interfaces import Reference
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class References(Collection):
    def __init__(self, com):
        super().__init__(com, child=Reference)
        self.references = com

    def item(self, i_index: 'cat_variant') -> Reference:
        return Reference(self.references.Item(i_index))

    def __getitem__(self, n: int) -> Reference:
        if (n + 1) > self.count():
            raise StopIteration

        return Reference(self.references.item(n + 1))

    def __iter__(self) -> Iterator[Reference]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'