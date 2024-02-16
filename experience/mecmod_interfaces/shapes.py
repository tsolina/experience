from typing import Iterator

from experience.mecmod_interfaces import Boundary, Shape
from experience.system import Collection
from experience.types import cat_variant

class Shapes(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Shapes
    """

    def __init__(self, com):
        super().__init__(com, child=Shape)
        self.shapes = com

    def get_boundary(self, i_label: str) -> Boundary:
        return Boundary(self.shapes.GetBoundary(i_label))

    def item(self, i_index: cat_variant) -> Shape:
        return Shape(self.shapes.Item(i_index))

    def __getitem__(self, n: int) -> Shape:
        if (n + 1) > self.count():
            raise StopIteration

        return Shape(self.shapes.item(n + 1))

    def __iter__(self) -> Iterator[Shape]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'Shapes(name="{self.name()}")'