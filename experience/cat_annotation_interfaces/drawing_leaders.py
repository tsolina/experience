from typing import Iterator

from experience.cat_annotation_interfaces import DrawingLeader
from experience.system import Collection


class DrawingLeaders(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingLeaders
    """

    def __init__(self, com):
        super().__init__(com, child=DrawingLeader)
        self.drawing_leaders = com

    def add(self, i_head_point_x: float, i_head_point_y: float) -> DrawingLeader:
        return DrawingLeader(self.drawing_leaders.Add(i_head_point_x, i_head_point_y))

    def item(self, i_index: int) -> DrawingLeader:
        return DrawingLeader(self.drawing_leaders.Item(i_index))

    def remove(self, i_index: int) -> 'DrawingLeaders':
        self.drawing_leaders.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> DrawingLeader:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingLeader(self.drawing_leaders.item(n + 1))

    def __iter__(self) -> Iterator[DrawingLeader]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'DrawingLeaders(name="{self.name()}")'
