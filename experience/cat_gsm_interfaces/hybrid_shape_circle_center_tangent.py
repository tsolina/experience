from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import HybridShapeCircle
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class HybridShapeCircleCenterTangent(HybridShapeCircle):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircleCenterTangent
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_circle_center_tangent = com

    def begin_of_circle(self, value: int = None) -> Union['HybridShapeCircleCenterTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_center_tangent.BeginOfCircle = value
            return self
        return self.hybrid_shape_circle_center_tangent.BeginOfCircle

    def center_elem(self, value: Reference = None) -> Union['HybridShapeCircleCenterTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_center_tangent.CenterElem = value._com
            return self
        return Reference(self.hybrid_shape_circle_center_tangent.CenterElem)

    def diameter(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_circle_center_tangent.Diameter)

    def diameter_mode(self, value: bool = None) -> Union['HybridShapeCircleCenterTangent', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_center_tangent.DiameterMode = value
            return self
        return self.hybrid_shape_circle_center_tangent.DiameterMode

    def discrimination_index(self, value: int = None) -> Union['HybridShapeCircleCenterTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_center_tangent.DiscriminationIndex = value
            return self
        return self.hybrid_shape_circle_center_tangent.DiscriminationIndex

    def orientation1(self, value: int = None) -> Union['HybridShapeCircleCenterTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_center_tangent.Orientation1 = value
            return self
        return self.hybrid_shape_circle_center_tangent.Orientation1

    def orientation2(self, value: int = None) -> Union['HybridShapeCircleCenterTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_center_tangent.Orientation2 = value
            return self
        return self.hybrid_shape_circle_center_tangent.Orientation2

    def radius(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_circle_center_tangent.Radius)

    def support(self, value: Reference = None) -> Union['HybridShapeCircleCenterTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_center_tangent.Support = value._com
            return self
        return Reference(self.hybrid_shape_circle_center_tangent.Support)

    def tangent_curve(self, value: Reference = None) -> Union['HybridShapeCircleCenterTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_center_tangent.TangentCurve = value._com
            return self
        return Reference(self.hybrid_shape_circle_center_tangent.TangentCurve)

    def tangent_orientation1(self, value: int = None) -> Union['HybridShapeCircleCenterTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_center_tangent.TangentOrientation1 = value
            return self
        return self.hybrid_shape_circle_center_tangent.TangentOrientation1

    def tangent_orientation2(self, value: int = None) -> Union['HybridShapeCircleCenterTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_center_tangent.TangentOrientation2 = value
            return self
        return self.hybrid_shape_circle_center_tangent.TangentOrientation2

    def __repr__(self):
        return f'HybridShapeCircleCenterTangent(name="{self.name}")'