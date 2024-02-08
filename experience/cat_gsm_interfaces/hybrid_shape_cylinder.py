from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection
    from experience.knowledge_interfaces import Length

class HybridShapeCylinder(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeCylinder
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_cylinder = com

    def center(self, value: Reference = None) -> Union['HybridShapeCylinder', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_cylinder.Center = value._com
            return self
        return Reference(self.hybrid_shape_cylinder.Center)

    def direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeCylinder', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_cylinder.Direction = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_cylinder.Direction)

    def length1(self, value: 'Length' = None) -> Union['HybridShapeCylinder', 'Length']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_cylinder.Length1 = value._com
            return self
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_cylinder.Length1)

    def length2(self, value: 'Length' = None) -> Union['HybridShapeCylinder', 'Length']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_cylinder.Length2 = value._com
            return self
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_cylinder.Length2)

    def orientation(self, value: bool = None) -> Union['HybridShapeCylinder', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_cylinder.Orientation = value
            return self
        return self.hybrid_shape_cylinder.Orientation

    def radius(self, value: 'Length' = None) -> Union['HybridShapeCylinder', 'Length']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_cylinder.Radius = value._com
            return self
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_cylinder.Radius)

    def symmetrical_extension(self, value: bool = None) -> Union['HybridShapeCylinder', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_cylinder.SymmetricalExtension = value
            return self
        return self.hybrid_shape_cylinder.SymmetricalExtension

    def invert_orientation(self) -> 'HybridShapeCylinder':
        self.hybrid_shape_cylinder.InvertOrientation()
        return self

    def __repr__(self):
        return f'HybridShapeCylinder(name="{self.name}")'