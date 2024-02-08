from experience.cat_annotation_interfaces import DrawingLeaders, DrawingTextProperties, DrawingTextRange
from experience.system import AnyObject

class DrawingWelding(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingWelding
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_welding = com_object

    def angle(self, value: float = None) -> float:
        if value is not None:
            self.drawing_welding.Angle = value
            return self
        return self.drawing_welding.Angle

    def identification_line_side(self, value: int = None) -> int:
        if value is not None:
            self.drawing_welding.IdentificationLineSide = value
            return self
        return self.drawing_welding.IdentificationLineSide

    def leaders(self) -> DrawingLeaders:
        return DrawingLeaders(self.drawing_welding.Leaders)

    def text_properties(self) -> DrawingTextProperties:
        return DrawingTextProperties(self.drawing_welding.TextProperties)

    def welding_side(self, value: int = None) -> int:
        if value is not None:
            self.drawing_welding.WeldingSide = value
            return self
        return self.drawing_welding.WeldingSide

    def welding_tail(self, value: int = None) -> int:
        if value is not None:
            self.drawing_welding.WeldingTail = value
            return self
        return self.drawing_welding.WeldingTail

    def x(self, value: float = None) -> float:
        if value is not None:
            self.drawing_welding.x = value
            return self
        return self.drawing_welding.x

    def y(self, value: float = None) -> float:
        if value is not None:
            self.drawing_welding.y = value
            return self
        return self.drawing_welding.y

    def get_additional_symbol(self, i_weld: int) -> int:
        return self.drawing_welding.GetAdditionalSymbol(i_weld)

    def get_finish_symbol(self, i_weld: int) -> int:
        return self.drawing_welding.GetFinishSymbol(i_weld)

    def get_symbol(self, i_weld: int) -> int:
        return self.drawing_welding.GetSymbol(i_weld)

    def get_text_range(self, i_field: int) -> DrawingTextRange:
        return DrawingTextRange(self.drawing_welding.GetTextRange(i_field))

    def set_additional_symbol(self, i_symbol: int, i_weld: int) -> 'DrawingWelding':
        self.drawing_welding.SetAdditionalSymbol(i_symbol, i_weld)
        return self

    def set_finish_symbol(self, i_finish_symbol: int, i_weld: int) -> 'DrawingWelding':
        self.drawing_welding.SetFinishSymbol(i_finish_symbol, i_weld)
        return self

    def set_symbol(self, i_symbol: int, i_weld: int) -> 'DrawingWelding':
        self.drawing_welding.SetSymbol(i_symbol, i_weld)
        return self

    def __repr__(self):
        return f'DrawingWelding(name="{self.name}")'
