from typing import TYPE_CHECKING

from experience.system import AnyObject
from experience.types import cat_variant

if TYPE_CHECKING:
    from experience.drafting_interfaces import DrawingView, DrawingSheet


class DrawingComponent(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingComponent
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_component = com

    def angle(self, value: float = None) -> float:
        if value is not None:
            self.drawing_component.Angle = value
            return self
        return self.drawing_component.Angle


    def comp_ref(self) -> 'DrawingView':
        from experience.drafting_interfaces import DrawingView
        return DrawingView(self.drawing_component.CompRef)

    def scale2(self, value: float = None) -> float:
        if value is not None:
            self.drawing_component.Scale2 = value
            return self
        return self.drawing_component.Scale2

    def x(self, value: float = None) -> float:
        if value is not None:
            self.drawing_component.x = value
            return self
        return self.drawing_component.x

    def y(self, value: float = None) -> float:
        if value is not None:
            self.drawing_component.y = value
            return self
        return self.drawing_component.y

    def explode(self) -> 'DrawingComponent':
        self.drawing_component.Explode()
        return self

    def explode_and_select(self) -> 'DrawingComponent':
        self.drawing_component.ExplodeAndSelect()
        return self

    def expose_comp_ref(self) -> 'DrawingComponent':
        self.drawing_component.ExposeCompRef()
        return self

    def expose_comp_ref_in_sheet(self, i_sheet: 'DrawingSheet') -> 'DrawingComponent':
        self.drawing_component.ExposeCompRefInSheet(i_sheet.com_object)
        return self

    def flip(self) -> 'DrawingComponent':
        self.drawing_component.Flip()
        return self

    def get_flip(self) -> bool:
        return self.drawing_component.GetFlip()

    def get_matrix(self, io_matrix: tuple) -> tuple:
        return self.drawing_component.GetMatrix(io_matrix)

    def get_modifiable_object(self, i_index: cat_variant) -> AnyObject:
        return AnyObject(self.drawing_component.GetModifiableObject(i_index))

    def get_modifiable_objects_count(self) -> int:
        return self.drawing_component.GetModifiableObjectsCount()

    def set_matrix(self, i_matrix: tuple) -> 'DrawingComponent':
        self.drawing_component.SetMatrix(i_matrix)
        return self

    def __repr__(self):
        return f'DrawingComponent(name="{self.name}")'
