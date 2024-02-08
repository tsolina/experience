from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import HybridShapeCircle
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class HybridShapeCircleBitangentRadius(HybridShapeCircle):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircleBitangentRadius
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_circle_bitangent_radius = com

    def begin_of_circle(self, value: int = None) -> Union['HybridShapeCircleBitangentRadius', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_bitangent_radius.BeginOfCircle = value
            return self
        return self.hybrid_shape_circle_bitangent_radius.BeginOfCircle

    def curve1(self, value: Reference = None) -> Union['HybridShapeCircleBitangentRadius', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_bitangent_radius.Curve1 = value._com
            return self
        return Reference(self.hybrid_shape_circle_bitangent_radius.Curve1)

    def curve2(self, value: Reference = None) -> Union['HybridShapeCircleBitangentRadius', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_bitangent_radius.Curve2 = value._com
            return self
        return Reference(self.hybrid_shape_circle_bitangent_radius.Curve2)

    def diameter(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_circle_bitangent_radius.Diameter)

    def diameter_mode(self, value: bool = None) -> Union['HybridShapeCircleBitangentRadius', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_bitangent_radius.DiameterMode = value
            return self
        return self.hybrid_shape_circle_bitangent_radius.DiameterMode

    def discrimination_index(self, value: int = None) -> Union['HybridShapeCircleBitangentRadius', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_bitangent_radius.DiscriminationIndex = value
            return self
        return self.hybrid_shape_circle_bitangent_radius.DiscriminationIndex

    def orientation1(self, value: int = None) -> Union['HybridShapeCircleBitangentRadius', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_bitangent_radius.Orientation1 = value
            return self
        return self.hybrid_shape_circle_bitangent_radius.Orientation1

    def orientation2(self, value: int = None) -> Union['HybridShapeCircleBitangentRadius', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_bitangent_radius.Orientation2 = value
            return self
        return self.hybrid_shape_circle_bitangent_radius.Orientation2

    def radius(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_circle_bitangent_radius.Radius)

    def support(self, value: Reference = None) -> Union['HybridShapeCircleBitangentRadius', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_bitangent_radius.Support = value._com
            return self
        return Reference(self.hybrid_shape_circle_bitangent_radius.Support)

    def tangent_orientation1(self, value: int = None) -> Union['HybridShapeCircleBitangentRadius', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_bitangent_radius.TangentOrientation1 = value
            return self
        return self.hybrid_shape_circle_bitangent_radius.TangentOrientation1

    def tangent_orientation2(self, value: int = None) -> Union['HybridShapeCircleBitangentRadius', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_bitangent_radius.TangentOrientation2 = value
            return self
        return self.hybrid_shape_circle_bitangent_radius.TangentOrientation2

    def trim_mode(self, value: int = None) -> Union['HybridShapeCircleBitangentRadius', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_bitangent_radius.TrimMode = value
            return self
        return self.hybrid_shape_circle_bitangent_radius.TrimMode

    def __repr__(self):
        return f'HybridShapeCircleBitangentRadius(name="{self.name}")'