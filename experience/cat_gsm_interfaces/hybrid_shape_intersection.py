from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeIntersection(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeIntersection
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_intersection = com

    def element1(self, value: Reference = None) -> Union['HybridShapeIntersection', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_intersection.Element1 = value._com
            return self
        return Reference(self.hybrid_shape_intersection.Element1)

    def element2(self, value: Reference = None) -> Union['HybridShapeIntersection', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_intersection.Element2 = value._com
            return self
        return Reference(self.hybrid_shape_intersection.Element2)

    def extend_mode(self, value: int = None) -> Union['HybridShapeIntersection', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_intersection.ExtendMode = value
            return self
        return self.hybrid_shape_intersection.ExtendMode

    def extrapolate_mode(self, value: bool = None) -> Union['HybridShapeIntersection', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_intersection.ExtrapolateMode = value
            return self
        return self.hybrid_shape_intersection.ExtrapolateMode

    def intersect_mode(self, value: bool = None) -> Union['HybridShapeIntersection', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_intersection.IntersectMode = value
            return self
        return self.hybrid_shape_intersection.IntersectMode

    def point_type(self, value: int = None) -> Union['HybridShapeIntersection', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_intersection.PointType = value
            return self
        return self.hybrid_shape_intersection.PointType

    def solid_mode(self, value: bool = None) -> Union['HybridShapeIntersection', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_intersection.SolidMode = value
            return self
        return self.hybrid_shape_intersection.SolidMode

    def __repr__(self):
        return f'HybridShapeIntersection(name="{ self.name }")'