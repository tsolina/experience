from typing import Iterator

from experience.cat_sketcher_interfaces import GeometricElement
from experience.system import Collection
from experience.types import cat_variant

class GeometricElements(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     GeometricElements
    """

    def __init__(self, com):
        super().__init__(com, child=GeometricElement)
        self.geometric_elements = com

    def item(self, i_index: cat_variant) -> GeometricElement:
        return GeometricElement(self.geometric_elements.Item(i_index))

    def __getitem__(self, n: int) -> GeometricElement:
        if (n + 1) > self.count():
            raise StopIteration

        return GeometricElement(self.geometric_elements.item(n + 1))

    def __iter__(self) -> Iterator[GeometricElement]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))