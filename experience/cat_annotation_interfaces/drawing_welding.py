from typing import Union, TYPE_CHECKING
from experience.system import AnyObject
from experience.cat_annotation_interfaces.annotation_types import *

if TYPE_CHECKING:
    from experience.cat_annotation_interfaces import DrawingLeaders, DrawingTextProperties, DrawingTextRange

class DrawingWelding(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingWelding
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_welding = com

    def angle(self, value: float = None) -> Union['DrawingWelding', float]:
        if value is not None:
            self.drawing_welding.Angle = value
            return self
        return self.drawing_welding.Angle

    def identification_line_side(self, value: CatWeldingSide = None) -> Union['DrawingWelding', CatWeldingSide]:
        if value is not None:
            self.drawing_welding.IdentificationLineSide = int(value)
            return self
        return CatWeldingSide.item(self.drawing_welding.IdentificationLineSide)

    def leaders(self) -> 'DrawingLeaders':
        from experience.cat_annotation_interfaces import DrawingLeaders
        return DrawingLeaders(self.drawing_welding.Leaders)

    def text_properties(self) -> 'DrawingTextProperties':
        from experience.cat_annotation_interfaces import DrawingTextProperties
        return DrawingTextProperties(self.drawing_welding.TextProperties)

    def welding_side(self, value: CatWeldingSide = None) -> Union['DrawingWelding', CatWeldingSide]:
        if value is not None:
            self.drawing_welding.WeldingSide = int(value)
            return self
        return CatWeldingSide.item(self.drawing_welding.WeldingSide)

    def welding_tail(self, value: CatDftWeldingTail = None) -> Union['DrawingWelding', CatDftWeldingTail]:
        if value is not None:
            self.drawing_welding.WeldingTail = int(value)
            return self
        return CatDftWeldingTail.item(self.drawing_welding.WeldingTail)

    def x(self, value: float = None) -> Union['DrawingWelding', float]:
        if value is not None:
            self.drawing_welding.x = value
            return self
        return self.drawing_welding.x

    def y(self, value: float = None) -> Union['DrawingWelding', float]:
        if value is not None:
            self.drawing_welding.y = value
            return self
        return self.drawing_welding.y

    def get_additional_symbol(self, i_weld: CatWelding) -> CatWeldAdditionalSymbol:
        return CatWeldAdditionalSymbol.item(self.drawing_welding.GetAdditionalSymbol(int(i_weld)))

    def get_finish_symbol(self, i_weld: CatWelding) -> CatDftWeldFinishSymbol:
        return CatDftWeldFinishSymbol.item(self.drawing_welding.GetFinishSymbol(int(i_weld)))

    def get_symbol(self, i_weld: CatWelding) -> CatWeldingSymbol:
        return CatWeldingSymbol.item(self.drawing_welding.GetSymbol(i_weld))

    def get_text_range(self, i_field: CatWeldingField) -> 'DrawingTextRange':
        from experience.cat_annotation_interfaces import DrawingTextRange
        return DrawingTextRange(self.drawing_welding.GetTextRange((i_field)))

    def set_additional_symbol(self, i_symbol: CatWeldAdditionalSymbol, i_weld: CatWelding) -> 'DrawingWelding':
        self.drawing_welding.SetAdditionalSymbol(int(i_symbol), int(i_weld))
        return self

    def set_finish_symbol(self, i_finish_symbol: CatDftWeldFinishSymbol, i_weld: CatWelding) -> 'DrawingWelding':
        self.drawing_welding.SetFinishSymbol(int(i_finish_symbol), int(i_weld))
        return self

    def set_symbol(self, i_symbol: CatWeldingSymbol, i_weld: CatWelding) -> 'DrawingWelding':
        self.drawing_welding.SetSymbol(int(i_symbol), int(i_weld))
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
