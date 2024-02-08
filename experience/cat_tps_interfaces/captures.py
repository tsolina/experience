from typing import Iterator

from experience.system import AnyObject, Collection
from experience.cat_tps_interfaces import Capture
from experience.types import cat_variant

class Captures(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Captures
    """

    def __init__(self, com):
        super().__init__(com)
        self.captures = com

    def item(self, i_index: cat_variant) -> AnyObject: #Capture
        return AnyObject(self.captures.Item(i_index))

    def __getitem__(self, n: int) -> Capture:
        if (n + 1) > self.count:
            raise StopIteration

        return Capture(self.captures.item(n + 1))

    def __iter__(self) -> Iterator[Capture]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'Captures(name="{self.name}")'
