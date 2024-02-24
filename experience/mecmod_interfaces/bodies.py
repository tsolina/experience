from typing import Iterator

from experience.mecmod_interfaces import Body
from experience.system import Collection
from experience.types import cat_variant


class Bodies(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Bodies
    """

    def __init__(self, com):
        super().__init__(com, child=Body)
        self.bodies = com

    def add(self) -> Body:
        return Body(self.bodies.Add())

    def item(self, i_index: cat_variant) -> Body:
        return Body(self.bodies.Item(i_index))

    def __getitem__(self, n: int) -> Body:
        if (n + 1) > self.count():
            raise StopIteration

        return Body(self.bodies.item(n + 1))

    def __iter__(self) -> Iterator[Body]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))