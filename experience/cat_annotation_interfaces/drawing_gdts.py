from typing import Iterator

from experience.cat_annotation_interfaces.annotation_types import *
from experience.cat_annotation_interfaces import DrawingGDT
from experience.system import Collection

class DrawingGDTs(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingTables
    """

    def __init__(self, com):
        super().__init__(com, child=DrawingGDT)
        self.drawing_gdts = com

    def add(self, i_position_leader_x: float, i_position_leader_y: float, i_position_x: float, i_position_y: float, i_gdts_symbol: AnnotationToleranceType, i_text: str) -> DrawingGDT:
        return DrawingGDT(self.drawing_gdts.Add(i_position_leader_x, i_position_leader_y, i_position_x, i_position_y, int(i_gdts_symbol), i_text))

    def item(self, i_index: int) -> DrawingGDT:
        return DrawingGDT(self.drawing_gdts.Item(i_index))

    def remove(self, i_index: int) -> 'DrawingGDTs':
        return self.drawing_gdts.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingGDT:
        if (n + 1) > self.count():
            raise StopIteration

        return DrawingGDT(self.drawing_gdts.item(n + 1))

    def __iter__(self) -> Iterator[DrawingGDT]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
