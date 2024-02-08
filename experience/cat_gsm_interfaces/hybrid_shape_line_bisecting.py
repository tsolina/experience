from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Line
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces.length import Length

class HybridShapeLineBisecting(Line):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Line
                |                             HybridShapeLineBisecting
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_line_bisecting = com

    def begin_offset(self) -> 'Length':
        from experience.knowledge_interfaces.length import Length
        return Length(self.hybrid_shape_line_bisecting.BeginOffset)

    def elem1(self, value: Reference = None) -> Union['HybridShapeLineBisecting', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_bisecting.Elem1 = value._com
            return self
        return Reference(self.hybrid_shape_line_bisecting.Elem1)

    def elem2(self, value: Reference = None) -> Union['HybridShapeLineBisecting', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_bisecting.Elem2 = value._com
            return self
        return Reference(self.hybrid_shape_line_bisecting.Elem2)

    def end_offset(self) -> 'Length':
        from experience.knowledge_interfaces.length import Length
        return Length(self.hybrid_shape_line_bisecting.EndOffset)

    def orientation(self, value: int = None) -> Union['HybridShapeLineBisecting', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_bisecting.Orientation = value
            return self
        return self.hybrid_shape_line_bisecting.Orientation

    def ref_point(self, value: Reference = None) -> Union['HybridShapeLineBisecting', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_bisecting.RefPoint = value._com
            return self
        return Reference(self.hybrid_shape_line_bisecting.RefPoint)

    def solution_type(self, value: bool = None) -> Union['HybridShapeLineBisecting', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_bisecting.SolutionType = value
            return self
        return self.hybrid_shape_line_bisecting.SolutionType

    def support(self, value: Reference = None) -> Union['HybridShapeLineBisecting', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_bisecting.Support = value._com
            return self
        return Reference(self.hybrid_shape_line_bisecting.Support)

    def get_length_type(self) -> int:
        return self.hybrid_shape_line_bisecting.GetLengthType()

    def get_symmetrical_extension(self) -> bool:
        return self.hybrid_shape_line_bisecting.GetSymmetricalExtension()

    def set_length_type(self, i_type: int) -> 'HybridShapeLineBisecting':
        self.hybrid_shape_line_bisecting.SetLengthType(i_type)
        return self

    def set_symmetrical_extension(self, i_sym: bool) -> None:
        self.hybrid_shape_line_bisecting.SetSymmetricalExtension(i_sym)
        return self

    def __repr__(self):
        return f'HybridShapeLineBisecting(name="{self.name}")'