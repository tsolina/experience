from typing import Iterator

from pywintypes import com_error

from experience.exceptions import CATIAApplicationException
from experience.mecmod_interfaces import HybridBody
from experience.system import Collection
from experience.types import cat_variant

class HybridBodies(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     HybridBodies
    """

    def __init__(self, com):
        super().__init__(com, child=HybridBody)
        self.hybrid_bodies = com
        # self.child_object = _child

    def add(self) -> HybridBody:
        return HybridBody(self.hybrid_bodies.Add())

    def item(self, i_index: cat_variant) -> HybridBody:
        try:
            return HybridBody(self.hybrid_bodies.Item(i_index))
        except com_error:
            raise CATIAApplicationException(f'Could not find hybrid_body "i_index"')

    def __getitem__(self, n: int) -> HybridBody:
        if (n + 1) > self.count:
            raise StopIteration

        return HybridBody(self.hybrid_bodies.item(n + 1))

    def __iter__(self) -> Iterator[HybridBody]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'HybridBodies(name="{self.name}")'