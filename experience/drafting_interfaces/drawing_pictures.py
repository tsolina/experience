from pathlib import Path
from typing import Iterator

from experience.exceptions import CATIAApplicationException
from experience.drafting_interfaces import DrawingPicture
from experience.system import Collection
from experience.types import cat_variant

class DrawingPictures(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingPictures
    """

    def __init__(self, com):
        super().__init__(com, _child=DrawingPicture)
        self.drawing_pictures = com

    def add(self, i_drawing_picture_path: str, i_position_x: float, i_position_y: float) -> DrawingPicture:
        absolute_path = Path(i_drawing_picture_path).absolute()
        if not absolute_path.is_file():
            raise CATIAApplicationException(f'Could not find image file: "{absolute_path}".')
        return DrawingPicture(self.drawing_pictures.Add(absolute_path, i_position_x, i_position_y))

    def item(self, i_index: cat_variant) -> DrawingPicture:
        return DrawingPicture(self.drawing_pictures.Item(i_index))

    def remove(self, i_index: cat_variant) -> 'DrawingPictures':
        self.drawing_pictures.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> DrawingPicture:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingPicture(self.drawing_pictures.item(n + 1))

    def __iter__(self) -> Iterator[DrawingPicture]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'DrawingPictures(name="{self.name}")'
