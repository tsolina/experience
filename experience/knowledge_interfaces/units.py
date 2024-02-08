from typing import Iterator

from experience.knowledge_interfaces import Unit
from experience.system import Collection
from experience.types import cat_variant


class Units(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Units
    """

    def __init__(self, com):
        super().__init__(com, _child=Unit)
        self.units = com

    def item(self, i_index: cat_variant) -> Unit:
        return Unit(self.units.Item(i_index))

    def __getitem__(self, n: int) -> Unit:
        if (n + 1) > self.count:
            raise StopIteration

        return Unit(self.units.item(n + 1))

    def __iter__(self) -> Iterator[Unit]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'Units(name="{self.name}")'
