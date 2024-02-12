from typing import Iterator

from experience.cat_annotation_interfaces import DrawingArrow
from experience.system import Collection

class DrawingArrows(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingArrows
    """

    def __init__(self, com):
        super().__init__(com, _child=DrawingArrow)
        self.drawing_arrows = com

    def add(self, i_head_point_x: float, i_head_point_y: float, i_tail_point_x: float, i_tail_point_y: float) -> DrawingArrow:
        return DrawingArrow(self.drawing_arrows.Add(i_head_point_x, i_head_point_y, i_tail_point_x, i_tail_point_y))

    def item(self, i_index: int) -> DrawingArrow:
        return DrawingArrow(self.drawing_arrows.Item(i_index))

    def remove(self, i_index: int) -> 'DrawingArrows':
        self.drawing_arrows.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> DrawingArrow:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingArrow(self.drawing_arrows.item(n + 1))

    def __iter__(self) -> Iterator[DrawingArrow]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'DrawingArrows(name="{self.name()}")'
