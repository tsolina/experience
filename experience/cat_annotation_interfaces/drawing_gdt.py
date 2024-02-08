from experience.system import AnyObject
# from experience.cat_annotation_interfaces import DrawingTextRange

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from experience.cat_annotation_interfaces import DrawingLeaders, DrawingTextProperties, DrawingTextRange

class DrawingGDT(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 DrawingTextRange
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_gdt = com

    def angle(self, value: float = None) -> float:
        if value is not None:
            self.drawing_gdt.Angle = value
            return self
        return self.drawing_gdt.Angle

    def drawing_leaders(self) -> 'DrawingGDT':
        from experience.cat_annotation_interfaces import DrawingLeaders
        return DrawingLeaders(self.drawing_gdt.DrawingLeaders())

    def row_number(self) -> int:
        return self.drawing_gdt.RowNumber

    def text_properties(self) -> 'DrawingGDT':
        from experience.cat_annotation_interfaces import DrawingTextProperties
        return DrawingTextProperties(self.drawing_gdt.DrawingTextProperties())

    def x(self, value: float = None) -> float:
        if value is not None:
            self.drawing_gdt.x = value
            return self
        return self.drawing_gdt.x

    def y(self, value: float = None) -> float:
        if value is not None:
            self.drawing_gdt.y = value
            return self
        return self.drawing_gdt.y

    def get_reference_number(self, i_row_number: int) -> int:
        return self.drawing_gdt.GetReferenceNumber(i_row_number)

    def get_text_range(self, i_row_number: int, i_number: int) -> 'DrawingTextRange':
        from experience.cat_annotation_interfaces import DrawingTextRange
        return DrawingTextRange(self.drawing_gdt.GetTextRange(i_row_number, i_number))

    def get_tolerance_type(self, i_row_number: int) -> int:
        return self.drawing_gdt.GetToleranceType(i_row_number)

    def set_tolerance_type(self, i_row_number: int, i_gdt_symbol: int) -> 'DrawingGDT':
        self.drawing_gdt.SetToleranceType(i_row_number, i_gdt_symbol)
        return self

    def __repr__(self):
        return f'DrawingGDT()'
