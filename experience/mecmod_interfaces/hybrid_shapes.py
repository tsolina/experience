from typing import Iterator, TYPE_CHECKING

from experience.mecmod_interfaces import Boundary
from experience.mecmod_interfaces import HybridShape
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant


class HybridShapes(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     HybridShapes
    """

    def __init__(self, com):
        super().__init__(com, child=HybridShape)
        self.hybrid_shapes = com

    def get_boundary(self, i_label: str) -> Boundary:
        return Boundary(self.hybrid_shapes.GetBoundary(i_label))

    def item(self, i_index: 'cat_variant') -> HybridShape:
        return HybridShape(self.hybrid_shapes.Item(i_index))

    def __getitem__(self, n: int) -> HybridShape:
        if (n + 1) > self.count():
            raise StopIteration

        return HybridShape(self.hybrid_shapes.item(n + 1))

    def __iter__(self) -> Iterator[HybridShape]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))