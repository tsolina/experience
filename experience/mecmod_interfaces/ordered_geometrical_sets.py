from typing import Iterator

from experience.mecmod_interfaces import OrderedGeometricalSet
from experience.system import Collection
from experience.types import cat_variant

class OrderedGeometricalSets(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     OrderedGeometricalSets
    """

    def __init__(self, com):
        super().__init__(com, child=OrderedGeometricalSet)
        self.ordered_geometrical_sets = com

    def add(self) -> OrderedGeometricalSet:
        return OrderedGeometricalSet(self.ordered_geometrical_sets.Add())

    def item(self, i_index: cat_variant) -> OrderedGeometricalSet:
        return OrderedGeometricalSet(self.ordered_geometrical_sets.Item(i_index))

    def __getitem__(self, n: int) -> OrderedGeometricalSet:
        if (n + 1) > self.count():
            raise StopIteration

        return OrderedGeometricalSet(self.ordered_geometrical_sets.item(n + 1))

    def __iter__(self) -> Iterator[OrderedGeometricalSet]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))