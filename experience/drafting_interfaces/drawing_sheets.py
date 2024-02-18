from typing import Iterator, TYPE_CHECKING

from experience.drafting_interfaces import DrawingSheet
from experience.system import Collection, AnyObject

if TYPE_CHECKING:
    from experience.types import cat_variant

class DrawingSheets(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingSheets
    """

    def __init__(self, com):
        super().__init__(com, child=DrawingSheet)
        self.drawing_sheets = com

    def active_sheet(self) -> DrawingSheet:
        return  DrawingSheet(self.drawing_sheets.ActiveSheet)

    def add(self, i_drawing_sheet_name: str) -> DrawingSheet:
        return DrawingSheet(self.drawing_sheets.Add(i_drawing_sheet_name))
    
    def add_detail(self, i_drawing_sheet_name: str) -> DrawingSheet:
        return DrawingSheet(self.drawing_sheets.AddDetail(i_drawing_sheet_name))

    def item(self, i_index: 'cat_variant') -> DrawingSheet:
        return DrawingSheet(self.drawing_sheets.Item(i_index))

    def remove(self, i_index: int) -> 'DrawingSheets':
        self.drawing_sheets.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> DrawingSheet:
        if (n + 1) > self.count():
            raise StopIteration

        return DrawingSheet(self.drawing_sheets.item(n + 1))

    def __iter__(self) -> Iterator[DrawingSheet]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
