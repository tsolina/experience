from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import HybridShapeCircle
from experience.inf_interfaces import Reference

class HybridShapeCircleBitangentPoint(HybridShapeCircle):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircleBitangentPoint
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_circle_bitangent_point = com

    def begin_of_circle(self, value: int = None) -> Union['HybridShapeCircleBitangentPoint', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.BeginOfCircle = value
            return self
        return self.hybrid_shape_circle_bitangent_point.BeginOfCircle

    def curve1(self, value: Reference = None) -> Union['HybridShapeCircleBitangentPoint', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_bitangent_point.Curve1 = value._com
            return self
        return Reference(self.hybrid_shape_circle_bitangent_point.Curve1)

    def curve2(self, value: Reference = None) -> Union['HybridShapeCircleBitangentPoint', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_bitangent_point.Curve2 = value._com
            return self
        return Reference(self.hybrid_shape_circle_bitangent_point.Curve2)

    def discrimination_index(self, value: int = None) -> Union['HybridShapeCircleBitangentPoint', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.DiscriminationIndex = value
            return self
        return self.hybrid_shape_circle_bitangent_point.DiscriminationIndex

    def orientation1(self, value: int = None) -> Union['HybridShapeCircleBitangentPoint', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.Orientation1 = value
            return self
        return self.hybrid_shape_circle_bitangent_point.Orientation1

    def orientation2(self, value: int = None) -> Union['HybridShapeCircleBitangentPoint', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.Orientation2 = value
            return self
        return self.hybrid_shape_circle_bitangent_point.Orientation2

    def pt(self, value: Reference = None) -> Union['HybridShapeCircleBitangentPoint', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_bitangent_point.Pt = value._com
            return self
        return Reference(self.hybrid_shape_circle_bitangent_point.Pt)

    def support(self, value: Reference = None) -> Union['HybridShapeCircleBitangentPoint', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_bitangent_point.Support = value._com
            return self
        return Reference(self.hybrid_shape_circle_bitangent_point.Support)

    def tangent_orientation1(self, value: int = None) -> Union['HybridShapeCircleBitangentPoint', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.TangentOrientation1 = value
            return self
        return self.hybrid_shape_circle_bitangent_point.TangentOrientation1

    def tangent_orientation2(self, value: int = None) -> Union['HybridShapeCircleBitangentPoint', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.TangentOrientation2 = value
            return self
        return self.hybrid_shape_circle_bitangent_point.TangentOrientation2

    def trim_mode(self, value: int = None) -> Union['HybridShapeCircleBitangentPoint', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.TrimMode = value
            return self
        return self.hybrid_shape_circle_bitangent_point.TrimMode

    def __repr__(self):
        return f'HybridShapeCircleBitangentPoint(name="{self.name}")'