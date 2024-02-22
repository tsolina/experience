from typing import Iterator

from experience.inf_interfaces import LightSource
from experience.system.collection import Collection

class LightSources(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     LightSources
    """

    def __init__(self, com):
        super().__init__(com, child=LightSource)
        self.light_sources = com

    def add(self) -> LightSource:
        return LightSource(self.light_sources.Add())

    def item(self, i_index: int) -> LightSource:
        return LightSource(self.light_sources.Item(i_index))

    def remove(self, i_index: int) -> None:
        return self.light_sources.Remove(i_index)

    def __getitem__(self, n: int) -> LightSource:
        if (n + 1) > self.count():
            raise StopIteration

        return LightSource(self.light_sources.item(n + 1))

    def __iter__(self) -> Iterator[LightSource]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'