from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import HybridShapeCircle
from experience.inf_interfaces import Reference

class HybridShapeCircleTritangent(HybridShapeCircle):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircleTritangent
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_circle_tritangent = com

    def begin_of_circle(self, value: int = None) -> Union['HybridShapeCircleTritangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_tritangent.BeginOfCircle = value
            return self
        return self.hybrid_shape_circle_tritangent.BeginOfCircle

    def curve1(self, value: Reference = None) -> Union['HybridShapeCircleTritangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_tritangent.Curve1 = value._com
            return self
        return Reference(self.hybrid_shape_circle_tritangent.Curve1)

    def curve2(self, value: Reference = None) -> Union['HybridShapeCircleTritangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_tritangent.Curve2 = value._com
            return self
        return Reference(self.hybrid_shape_circle_tritangent.Curve2)

    def curve3(self, value: Reference = None) -> Union['HybridShapeCircleTritangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_tritangent.Curve3 = value._com
            return self
        return Reference(self.hybrid_shape_circle_tritangent.Curve3)

    def discrimination_index(self, value: int = None) -> Union['HybridShapeCircleTritangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_tritangent.DiscriminationIndex = value
            return self
        return self.hybrid_shape_circle_tritangent.DiscriminationIndex

    def orientation1(self, value: int = None) -> Union['HybridShapeCircleTritangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_tritangent.Orientation1 = value
            return self
        return self.hybrid_shape_circle_tritangent.Orientation1

    def orientation2(self, value: int = None) -> Union['HybridShapeCircleTritangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_tritangent.Orientation2 = value
            return self
        return self.hybrid_shape_circle_tritangent.Orientation2

    def orientation3(self, value: int = None) -> Union['HybridShapeCircleTritangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_tritangent.Orientation3 = value
            return self
        return self.hybrid_shape_circle_tritangent.Orientation3

    def support(self, value: Reference = None) -> Union['HybridShapeCircleTritangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_tritangent.Support = value._com
            return self
        return Reference(self.hybrid_shape_circle_tritangent.Support)

    def tangent_orientation1(self, value: int = None) -> Union['HybridShapeCircleTritangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_tritangent.TangentOrientation1 = value
            return self
        return self.hybrid_shape_circle_tritangent.TangentOrientation1

    def tangent_orientation2(self, value: int = None) -> Union['HybridShapeCircleTritangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_tritangent.TangentOrientation2 = value
            return self
        return self.hybrid_shape_circle_tritangent.TangentOrientation2

    def tangent_orientation3(self, value: int = None) -> Union['HybridShapeCircleTritangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_tritangent.TangentOrientation3 = value
            return self
        return self.hybrid_shape_circle_tritangent.TangentOrientation3

    def trim_mode(self, value: int = None) -> Union['HybridShapeCircleTritangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_tritangent.TrimMode = value
            return self
        return self.hybrid_shape_circle_tritangent.TrimMode

    def __repr__(self):
        return f'HybridShapeCircleTritangent(name="{ self.name }")'