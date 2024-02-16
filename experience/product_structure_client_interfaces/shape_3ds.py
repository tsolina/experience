from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from experience.product_structure_client_interfaces import Shape3D

if TYPE_CHECKING:
    from experience.types import cat_variant

class Shape3Ds(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Shape3Ds
    """

    def __init__(self, com):
        super().__init__(com, child=Shape3D)
        self.vpm_rep_occurrences = com

    def item(self, i_index: 'cat_variant') -> Shape3D:
        return Shape3D(self.printers.Item(i_index))

    def __getitem__(self, n: int) -> Shape3D:
        if (n + 1) > self.count():
            raise StopIteration
        return Shape3D(self.printers.item(n + 1))

    def __iter__(self) -> Iterator[Shape3D]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'Shape3Ds(name="{self.name()}")'