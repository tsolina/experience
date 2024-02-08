from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Line
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle, Length

class HybridShapeLineAngle(Line):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Line
                |                             HybridShapeLineAngle
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_line_angle = com

    def angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_line_angle.Angle)

    def begin_offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_line_angle.BeginOffset)

    def curve(self, value: Reference = None) -> Union['HybridShapeLineAngle', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_angle.Curve = value._com
            return self
        return Reference(self.hybrid_shape_line_angle.Curve)

    def end_offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_line_angle.EndOffset)

    def geodesic(self, value: bool = None) -> Union['HybridShapeLineAngle', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_angle.Geodesic = value
            return self
        return self.hybrid_shape_line_angle.Geodesic

    def orientation(self, value: int = None) -> Union['HybridShapeLineAngle', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_angle.Orientation = value
            return self
        return self.hybrid_shape_line_angle.Orientation

    def point(self, value: Reference = None) -> Union['HybridShapeLineAngle', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_angle.Point = value._com
            return self
        return Reference(self.hybrid_shape_line_angle.Point)

    def surface(self, value: Reference = None) -> Union['HybridShapeLineAngle', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_angle.Surface = value._com
            return self
        return Reference(self.hybrid_shape_line_angle.Surface)

    def get_length_type(self) -> int:
        return self.hybrid_shape_line_angle.GetLengthType()

    def get_symmetrical_extension(self) -> bool:
        return self.hybrid_shape_line_angle.GetSymmetricalExtension()

    def set_length_type(self, i_type: int) -> 'HybridShapeLineAngle':
        self.hybrid_shape_line_angle.SetLengthType(i_type)
        return self

    def set_symmetrical_extension(self, i_sym: bool) -> 'HybridShapeLineAngle':
        self.hybrid_shape_line_angle.SetSymmetricalExtension(i_sym)
        return self

    def __repr__(self):
        return f'HybridShapeLineAngle(name="{self.name}")'