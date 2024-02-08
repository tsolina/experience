from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection
    from experience.knowledge_interfaces.angle import Angle

class HybridShapeReflectLine(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeReflectLine
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_reflect_line = com

    def angle(self, value: 'Angle' = None) -> Union['HybridShapeReflectLine', 'Angle']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_reflect_line.Angle = value._com
            return self
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_reflect_line.Angle)

    def direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeReflectLine', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_reflect_line.Direction = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_reflect_line.Direction)

    def orientation_direction(self, value: int = None) -> Union['HybridShapeReflectLine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_reflect_line.OrientationDirection = value
            return self
        return self.hybrid_shape_reflect_line.OrientationDirection

    def orientation_support(self, value: int = None) -> Union['HybridShapeReflectLine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_reflect_line.OrientationSupport = value
            return self
        return self.hybrid_shape_reflect_line.OrientationSupport

    def origin(self, value: Reference = None) -> Union['HybridShapeReflectLine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_reflect_line.Origin = value._com
            return self
        return Reference(self.hybrid_shape_reflect_line.Origin)

    def source_type(self, value: int = None) -> Union['HybridShapeReflectLine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_reflect_line.SourceType = value
            return self
        return self.hybrid_shape_reflect_line.SourceType

    def support(self, value: Reference = None) -> Union['HybridShapeReflectLine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_reflect_line.Support = value._com
            return self
        return Reference(self.hybrid_shape_reflect_line.Support)

    def type_solution(self, value: int = None) -> Union['HybridShapeReflectLine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_reflect_line.TypeSolution = value
            return self
        return self.hybrid_shape_reflect_line.TypeSolution

    def invert_orientation_direction(self) -> 'HybridShapeReflectLine':
        self.hybrid_shape_reflect_line.InvertOrientationDirection()
        return self

    def invert_orientation_support(self) -> 'HybridShapeReflectLine':
        self.hybrid_shape_reflect_line.InvertOrientationSupport()
        return self
    
    def __repr__(self):
        return f'HybridShapeReflectLine(name="{self.name}")'