from typing import Iterator

from experience.drafting_interfaces import DrawingAreaFill
from experience.system import CATBaseDispatch, Collection

class DrawingAreaFills(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingAreaFills
    """

    def __init__(self, com):
        super().__init__(com, child=DrawingAreaFill)
        self.drawing_area_fills = com

    def add(self, i_number_of_points_per_contour: tuple, i_points_coordinates: tuple) -> DrawingAreaFill:
        return DrawingAreaFill(self.drawing_area_fills.Add(i_number_of_points_per_contour, i_points_coordinates))

    def item(self, i_index: int) -> DrawingAreaFill:
        return DrawingAreaFill(self.drawing_area_fills.Item(i_index))

    def remove(self, i_index: int) -> 'DrawingAreaFills':
        self.drawing_area_fills.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> DrawingAreaFill:
        if (n + 1) > self.count():
            raise StopIteration

        return DrawingAreaFill(self.drawing_area_fills.item(n + 1))

    def __iter__(self) -> Iterator[DrawingAreaFill]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'DrawingAreaFills(name="{self.name()}")'
