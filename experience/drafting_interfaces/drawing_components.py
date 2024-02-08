from typing import Iterator, TYPE_CHECKING

from experience.drafting_interfaces import DrawingComponent
from experience.system import Collection
from experience.types import cat_variant

if TYPE_CHECKING:
    from experience.drafting_interfaces import DrawingView

class DrawingComponents(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingComponents
    """

    def __init__(self, com):
        super().__init__(com, _child=DrawingComponent)
        self.drawing_components = com

    def add(self, i_drawing_component_ref: 'DrawingView', i_position_x: float, i_position_y: float) -> DrawingComponent:
        return DrawingComponent(self.drawing_components.Add(i_drawing_component_ref._com,i_position_x,i_position_y))

    def item(self, i_index: cat_variant) -> DrawingComponent:
        return DrawingComponent(self.drawing_components.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.drawing_components.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingComponent:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingComponent(self.drawing_components.item(n + 1))

    def __iter__(self) -> Iterator[DrawingComponent]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'DrawingComponents()'
