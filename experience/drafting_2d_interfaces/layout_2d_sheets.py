from typing import Iterator, TYPE_CHECKING

from .layout_2d_sheet import Layout2DSheet
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class Layout2DSheets(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Layout2DSheets
    """

    def __init__(self, com):
        super().__init__(com, child=Layout2DSheet)
        self.layout_2d_sheets = com

    def active_sheet(self) -> Layout2DSheet:
        return Layout2DSheet(self.layout_2d_sheets.ActiveSheet)

    def add(self, i_layout_sheet_name: str) -> Layout2DSheet:
        return Layout2DSheet(self.layout_2d_sheets.Add(i_layout_sheet_name))
    
    def add_detail(self, i_layout_sheet_name: str) -> Layout2DSheet:
        return Layout2DSheet(self.layout_2d_sheets.AddDetail(i_layout_sheet_name))

    def item(self, i_index: 'cat_variant') -> Layout2DSheet:
        return Layout2DSheet(self.layout_2d_sheets.Item(i_index))

    def remove(self, i_index: 'cat_variant') -> 'Layout2DSheets':
        self.layout_2d_sheets.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> Layout2DSheet:
        if (n + 1) > self.count():
            raise StopIteration

        return Layout2DSheet(self.layout_2d_sheets.item(n + 1))

    def __iter__(self) -> Iterator[Layout2DSheet]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
