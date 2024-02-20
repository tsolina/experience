from typing import Iterator, TYPE_CHECKING

from experience.cat_annotation_interfaces import DrawingText
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class DrawingTexts(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingTexts
    """

    def __init__(self, com):
        super().__init__(com, child=DrawingText)
        self.drawing_texts = com
        self._child = DrawingText

    def add(self, i_drawing_text: str, i_position_x: float, i_position_y: float) -> DrawingText:
        return DrawingText(self.drawing_texts.Add(i_drawing_text, i_position_x, i_position_y))

    def item(self, i_index: 'cat_variant') -> DrawingText:
        return DrawingText(self.drawing_texts.Item(i_index))

    def remove(self, i_index: 'cat_variant') -> 'DrawingTexts':
        self.drawing_texts.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> DrawingText:
        if (n + 1) > self.count():
            raise StopIteration

        return DrawingText(self.drawing_texts.item(n + 1))

    def __iter__(self) -> Iterator[DrawingText]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
