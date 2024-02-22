from typing import Iterator, TYPE_CHECKING

from experience.inf_interfaces import Editor
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types.general import cat_variant

class Editors(Collection):
    def __init__(self, com):
        super().__init__(com, child=Editor)
        self.editors = com

    def item(self, i_index: 'cat_variant') -> 'Editor':
        return Editor(self.editors.Item(i_index))

    def __getitem__(self, n: int) -> Editor:
        if (n + 1) > self.count():
            raise StopIteration

        return Editor(self.editors.item(n + 1))

    def __iter__(self) -> Iterator[Editor]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'