from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle

class HybridShapeRevol(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeRevol
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_revol = com

    def axis(self, value: Reference = None) -> Union['HybridShapeRevol', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_revol.Axis = value._com
            return self
        return Reference(self.hybrid_shape_revol.Axis)

    def begin_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_revol.BeginAngle)

    def begin_angle_offset(self, value: float = None) -> Union['HybridShapeRevol', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_revol.BeginAngleOffset = value
            return self
        return self.hybrid_shape_revol.BeginAngleOffset

    def context(self, value: int = None) -> Union['HybridShapeRevol', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_revol.Context = value
            return self
        return self.hybrid_shape_revol.Context

    def end_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_revol.EndAngle)

    def end_angle_offset(self, value: float = None) -> Union['HybridShapeRevol', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_revol.EndAngleOffset = value
            return self
        return self.hybrid_shape_revol.EndAngleOffset    

    def first_limit_type(self, value: int = None) -> Union['HybridShapeRevol', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_revol.FirstLimitType = value
            return self
        return self.hybrid_shape_revol.FirstLimitType

    def first_upto_element(self, value: Reference = None) -> Union['HybridShapeRevol', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_revol.FirstUptoElement = value._com
            return self
        return Reference(self.hybrid_shape_revol.FirstUptoElement)

    def orientation(self, value: bool = None) -> Union['HybridShapeRevol', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_revol.Orientation = value
            return self
        return self.hybrid_shape_revol.Orientation

    def profile(self, value: Reference = None) -> Union['HybridShapeRevol', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_revol.Profil = value._com
            return self
        return Reference(self.hybrid_shape_revol.Profil)

    def second_limit_type(self, value: int = None) -> Union['HybridShapeRevol', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_revol.SecondLimitType = value
            return self
        return self.hybrid_shape_revol.SecondLimitType

    def second_upto_element(self, value: Reference = None) -> Union['HybridShapeRevol', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_revol.SecondUptoElement = value._com
            return self
        return Reference(self.hybrid_shape_revol.SecondUptoElement)

    def __repr__(self):
        return f'HybridShapeRevol(name="{self.name}")'