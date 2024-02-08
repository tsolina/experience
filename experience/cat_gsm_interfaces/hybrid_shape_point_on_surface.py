from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Point
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length
    from experience.cat_gsm_interfaces import HybridShapeDirection

class HybridShapePointOnSurface(Point):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Point
                |                             HybridShapePointOnSurface
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_point_on_surface = com

    def direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapePointOnSurface', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_on_surface.Direction = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_point_on_surface.Direction)

    def offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_point_on_surface.Offset)

    def point(self, value: Reference = None) -> Union['HybridShapePointOnSurface', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_on_surface.Point = value._com
            return self
        return Reference(self.hybrid_shape_point_on_surface.Point)

    def surface(self, value: Reference = None) -> Union['HybridShapePointOnSurface', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_on_surface.Surface = value._com
            return self
        return Reference(self.hybrid_shape_point_on_surface.Surface)

    def __repr__(self):
        return f'HybridShapePointOnSurface(name="{self.name}")'