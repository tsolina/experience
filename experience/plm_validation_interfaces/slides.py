from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from experience.plm_validation_interfaces import Slide

if TYPE_CHECKING:
    from experience.types import cat_variant

class Slides(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Slides
    """
    def __init__(self, com):
        super().__init__(com, child=Slide)
        self.slides = com

    def add(self) -> Slide:
        return Slide(self.slides.Add())

    def item(self, i_index: 'cat_variant') -> Slide:
        return Slide(self.slides.Item(i_index))
    
    def remove(self, i_index: 'cat_variant') -> 'Slides':
        self.slides.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> Slide:
        if (n + 1) > self.count():
            raise StopIteration
        return Slide(self.slides.item(n + 1))

    def __iter__(self) -> Iterator[Slide]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))