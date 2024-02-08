from experience.cat_annotation_interfaces import DrawingDimExtLine, DrawingDimLine, DrawingDimValue
from experience.knowledge_interfaces import Parameters
from experience.system import AnyObject

class DrawingDimension(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingDimension
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_dimension = com

    def cumulate_mode(self) -> bool:
        return self.drawing_dimension.CumulateMode

    def dim_status(self, value: int = None) -> int:
        if value is not None:
            self.drawing_dimension.DimStatus = value
            return self
        return self.drawing_dimension.DimStatus

    def dim_type(self) -> int:
        return self.drawing_dimension.DimType

    def dual_value(self, value: int = None) -> int:
        if value is not None:
            self.drawing_dimension.DualValue = value
            return self
        return self.drawing_dimension.DualValue

    def forshortened(self, value: bool = None) -> bool:
        if value is not None:
            self.drawing_dimension.Forshortened = value
            return self
        return self.drawing_dimension.Forshortened

    def half_dim_mode(self, value: bool = None) -> bool:
        if value is not None:
            self.drawing_dimension.HalfDimMode = value
            return self
        return self.drawing_dimension.HalfDimMode

    def is_clipped(self) -> bool:
        return self.drawing_dimension.IsClipped

    def nb_ext_line(self) -> int:
        return self.drawing_dimension.NbExtLine

    def nb_symb(self) -> int:
        return self.drawing_dimension.NbSymb

    def parameters(self) -> Parameters:
        return Parameters(self.drawing_dimension.Parameters)

    def symbols_side(self, value: int = None) -> int:
        if value is not None:
            self.drawing_dimension.SymbolsSide = value
            return self
        return self.drawing_dimension.SymbolsSide

    def true_dim_mode(self) -> bool:
        return self.drawing_dimension.TrueDimMode

    def value_angle(self, value: float = None) -> float:
        if value is not None:
            self.drawing_dimension.ValueAngle = value
            return self
        return self.drawing_dimension.ValueAngle

    def value_auto_mode(self, value: int = None) -> int:
        if value is not None:
            self.drawing_dimension.ValueAutoMode = value
            return self
        return self.drawing_dimension.ValueAutoMode

    def value_display(self) -> int:
        if value is not None:
            self.drawing_dimension.ValueDisplay = value
            return self
        return self.drawing_dimension.ValueDisplay

    def value_frame(self, value: int = None) -> int:
        if value is not None:
            self.drawing_dimension.ValueFrame = value
            return self
        return self.drawing_dimension.ValueFrame

    def value_in_out(self, value: int = None) -> int:
        if value is not None:
            self.drawing_dimension.ValueInOut = value
            return self
        return self.drawing_dimension.ValueInOut

    def value_orientation(self, value: int = None) -> int:
        if value is not None:
            self.drawing_dimension.ValueOrientation = value
            return self
        return self.drawing_dimension.ValueOrientation

    def value_reference(self, value: int = None) -> int:
        if value is not None:
            self.drawing_dimension.ValueReference = value
            return self
        return self.drawing_dimension.ValueReference

    def get_boundary_box(self) -> tuple: #CATSafeArrayVariant oValues
        return self.drawing_dimension.GetBoundaryBox()

    def get_clip(self) -> tuple[float, float, int]:
        return self.drawing_dimension.GetClip()

    def get_dim_ext_line(self) -> DrawingDimExtLine:
        return DrawingDimExtLine(self.drawing_dimension.GetDimExtLine())

    def get_dim_line(self) -> DrawingDimLine:
        return DrawingDimLine(self.drawing_dimension.GetDimLine())

    def get_tolerances(self) -> tuple[int, str, str, str, float, float, int]:
        return self.drawing_dimension.GetTolerances()

    def get_value(self) -> DrawingDimValue:
        return DrawingDimValue(self.drawing_dimension.GetValue())

    def move_value(self, x: float, y: float, sub_part: int, dim_angle_behavior: int) -> 'DrawingDimension':
        self.drawing_dimension.MoveValue(x, y, sub_part, dim_angle_behavior)
        return self

    def restore_value_position(self) -> 'DrawingDimension':
        self.drawing_dimension.RestoreValuePosition()
        return self

    def set_clip(self, x: float, y: float, i_kept_side: int) -> 'DrawingDimension':
        self.drawing_dimension.SetClip(x, y, i_kept_side)
        return self

    def set_tolerances(self, i_tol_type: int, itol_name: str, i_up_tol: str, i_low_tol: str, id_up_tol: float, id_low_tol: float, display_mode: int) -> 'DrawingDimension':
        self.drawing_dimension.SetTolerances(i_tol_type, itol_name, i_up_tol, i_low_tol, id_up_tol, id_low_tol, display_mode)
        return self

    def unclip(self) -> 'DrawingDimension':
        self.drawing_dimension.Unclip()
        return self

    def __repr__(self):
        return f'DrawingDimension(name="{self.name}")'
