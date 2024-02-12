from typing import Iterator

from experience.cat_annotation_interfaces import DrawingCoordDim
from experience.system import Collection


class DrawingCoordDims(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingCoordDims
    """

    def __init__(self, com):
        super().__init__(com, _child=DrawingCoordDim)
        self.drawing_coord_dims = com

    def item(self, i_index: int) -> DrawingCoordDim:
        return DrawingCoordDim(self.drawing_coord_dims.Item(i_index))

    def remove(self, i_index: int) -> 'DrawingCoordDims':
        self.drawing_coord_dims.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> DrawingCoordDim:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingCoordDim(self.drawing_coord_dims.item(n + 1))

    def __iter__(self) -> Iterator[DrawingCoordDim]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'DrawingCoordDims(name="{self.name()}")'
