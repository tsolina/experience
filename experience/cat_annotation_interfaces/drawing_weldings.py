from typing import Iterator, TYPE_CHECKING

from experience.cat_annotation_interfaces.annotation_types import *
from experience.cat_annotation_interfaces import DrawingWelding
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class DrawingWeldings(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingWeldings
    """

    def __init__(self, com):
        super().__init__(com, child=DrawingWelding)
        self.drawing_weldings = com

    def add(self, i_symbol: CatWeldingSymbol, i_position_x: float, i_position_y: float) -> DrawingWelding:
        return DrawingWelding(self.drawing_weldings.Add(int(i_symbol), i_position_x, i_position_y))

    def item(self, i_index: 'cat_variant') -> DrawingWelding:
        return DrawingWelding(self.drawing_weldings.Item(i_index))

    def remove(self, i_index: 'cat_variant') -> 'DrawingWeldings':
        self.drawing_weldings.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> DrawingWelding:
        if (n + 1) > self.count():
            raise StopIteration

        return DrawingWelding(self.drawing_weldings.item(n + 1))

    def __iter__(self) -> Iterator[DrawingWelding]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
