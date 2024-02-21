from typing import Iterator, Union

from experience.system.collection import Collection
from experience.cat_opns_measure_interfaces import Measure

from experience.types import cat_variant

class Measures(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Measures
    """

    def __init__(self, com):
        super().__init__(com, child=Measure)
        self.measures = com

    def add(self) -> Measure:
        return Measure(self.light_sources.Add())

    def item(self, i_index: 'cat_variant') -> Measure:
        return Measure(self.light_sources.Item(i_index))

    def remove(self, i_index: 'cat_variant') -> None:
        return self.light_sources.Remove(i_index)

    def __getitem__(self, n: int) -> Measure:
        if (n + 1) > self.count():
            raise StopIteration

        return Measure(self.light_sources.item(n + 1))

    def __iter__(self) -> Iterator[Measure]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
