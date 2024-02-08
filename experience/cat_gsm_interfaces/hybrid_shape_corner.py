from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces.reference import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection
    from experience.knowledge_interfaces import Length

class HybridShapeCorner(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeCorner
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_corner = com

    def begin_of_corner(self, value: int = None) -> Union['HybridShapeCorner', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.BeginOfCorner = value
            return self
        return self.hybrid_shape_corner.BeginOfCorner

    def corner_type(self, value: int = None) -> Union['HybridShapeCorner', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.CornerType = value
            return self
        return self.hybrid_shape_corner.CornerType

    def direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeCorner', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.Direction = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_corner.Direction)

    def discrimination_index(self, value: int = None) -> Union['HybridShapeCorner', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.DiscriminationIndex = value
            return self
        return self.hybrid_shape_corner.DiscriminationIndex

    def first_elem(self, value: Reference = None) -> Union['HybridShapeCorner', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.FirstElem = value._com
            return self
        return Reference(self.hybrid_shape_corner.FirstElem)

    def first_orientation(self, value: int = None) -> Union['HybridShapeCorner', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.FirstOrientation = value
            return self
        return self.hybrid_shape_corner.FirstOrientation

    def first_tangent_orientation(self, value: int = None) -> Union['HybridShapeCorner', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.FirstTangentOrientation = value
            return self
        return self.hybrid_shape_corner.FirstTangentOrientation

    def on_vertex(self, value: bool = None) -> Union['HybridShapeCorner', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.OnVertex = value
            return self
        return self.hybrid_shape_corner.OnVertex

    def radius(self, value: 'Length' = None) -> Union['HybridShapeCorner', 'Length']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.Radius = value._com
            return self
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_corner.Radius)

    def second_elem(self, value: Reference = None) -> Union['HybridShapeCorner', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.SecondElem = value._com
            return self
        return Reference(self.hybrid_shape_corner.SecondElem)

    def second_orientation(self, value: int = None) -> Union['HybridShapeCorner', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.SecondOrientation = value
            return self
        return self.hybrid_shape_corner.SecondOrientation

    def second_tangent_orientation(self, value: int = None) -> Union['HybridShapeCorner', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.SecondTangentOrientation = value
            return self
        return self.hybrid_shape_corner.SecondTangentOrientation

    def support(self, value: Reference = None) -> Union['HybridShapeCorner', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.Support = value._com
            return self
        return Reference(self.hybrid_shape_corner.Support)

    def trim(self, value: bool = None) -> Union['HybridShapeCorner', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.Trim = value
            return self
        return self.hybrid_shape_corner.Trim

    def trim_mode(self, value: int = None) -> Union['HybridShapeCorner', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_corner.TrimMode = value
            return self
        return self.hybrid_shape_corner.TrimMode

    def invert_first_orientation(self) -> 'HybridShapeCorner':
        """ perform the action and return self"""
        self.hybrid_shape_corner.InvertFirstOrientation()
        return self

    def invert_second_orientation(self) -> 'HybridShapeCorner':
        """ perform the action and return self"""
        self.hybrid_shape_corner.InvertSecondOrientation()
        return self

    def __repr__(self):
        return f'HybridShapeCorner(name="{ self.name }")'