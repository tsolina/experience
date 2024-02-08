from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces.reference import Reference
from experience.mecmod_interfaces.hybrid_shape import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle, Length

class HybridShapeSphere(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeSphere
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_sphere = com

    def axis(self, value: Reference = None) -> Union['HybridShapeSphere', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sphere.Axis = value._com
            return self
        return Reference(self.hybrid_shape_sphere.Axis)

    def begin_meridian_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_sphere.BeginMeridianAngle)

    def begin_parallel_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_sphere.BeginParallelAngle)

    def center(self, value: Reference = None) -> Union['HybridShapeSphere', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sphere.Center = value._com
            return self
        return Reference(self.hybrid_shape_sphere.Center)

    def end_meridian_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_sphere.EndMeridianAngle)

    def end_parallel_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_sphere.EndParallelAngle)

    def limitation(self, value: int = None) -> Union['HybridShapeSphere', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sphere.Limitation = value
            return self
        return self.hybrid_shape_sphere.Limitation

    def radius(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_sphere.Radius)

    def set_begin_meridian_angle(self, i_angle: float) -> 'HybridShapeSphere':
        self.hybrid_shape_sphere.SetBeginMeridianAngle(i_angle)
        return self

    def set_begin_parallel_angle(self, i_angle: float) -> 'HybridShapeSphere':
        self.hybrid_shape_sphere.SetBeginParallelAngle(i_angle)
        return self

    def set_end_meridian_angle(self, i_angle: float) -> 'HybridShapeSphere':
        self.hybrid_shape_sphere.SetEndMeridianAngle(i_angle)
        return self

    def set_end_parallel_angle(self, i_angle: float) -> 'HybridShapeSphere':
        self.hybrid_shape_sphere.SetEndParallelAngle(i_angle)
        return self

    def set_radius(self, i_radius: float) -> 'HybridShapeSphere':
        self.hybrid_shape_sphere.SetRadius(i_radius)
        return self

    def __repr__(self):
        return f'HybridShapeSphere(name="{self.name}")'