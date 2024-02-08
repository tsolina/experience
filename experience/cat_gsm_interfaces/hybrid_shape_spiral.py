from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection
    from experience.knowledge_interfaces import Angle, Length, RealParam

class HybridShapeSpiral(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeSpiral
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_spiral = com

    def axis(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeSpiral', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_spiral.Axis = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_spiral.Axis)

    def center_point(self, value: Reference = None) -> Union['HybridShapeSpiral', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_spiral.CenterPoint = value._com
            return self
        return Reference(self.hybrid_shape_spiral.CenterPoint)

    def clockwise_revolution(self, value: bool = None) -> Union['HybridShapeSpiral', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_spiral.ClockwiseRevolution = value
            return self
        return self.hybrid_shape_spiral.ClockwiseRevolution

    def ending_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_spiral.EndingAngle)

    def ending_radius(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_spiral.EndingRadius)

    def invert_axis(self, value: bool = None) -> Union['HybridShapeSpiral', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_spiral.InvertAxis = value
            return self
        return self.hybrid_shape_spiral.InvertAxis

    def pitch(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_spiral.Pitch)

    def revol_number(self) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.hybrid_shape_spiral.RevolNumber)

    def starting_radius(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_spiral.StartingRadius)

    def support(self, value: Reference = None) -> Union['HybridShapeSpiral', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_spiral.Support = value._com
            return self
        return Reference(self.hybrid_shape_spiral.Support)

    def type(self, value: int = None) -> Union['HybridShapeSpiral', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_spiral.Type = value
            return self
        return self.hybrid_shape_spiral.Type

    def set_angle_pitch_param(self, i_end_angle: float, i_revol_number: float, i_pitch: float) -> 'HybridShapeSpiral':
        self.hybrid_shape_spiral.SetAnglePitchParam(i_end_angle, i_revol_number, i_pitch)
        return self

    def set_angle_radius_param(self, i_end_angle: float, i_revol_number: float, i_end_radius: float) -> 'HybridShapeSpiral':
        self.hybrid_shape_spiral.SetAngleRadiusParam(i_end_angle, i_revol_number, i_end_radius)
        return self

    def set_radius_pitch_param(self, i_end_radius: float, i_pitch: float) -> 'HybridShapeSpiral':
        self.hybrid_shape_spiral.SetRadiusPitchParam(i_end_radius, i_pitch)
        return self

    def __repr__(self):
        return f'HybridShapeSpiral(name="{self.name}")'