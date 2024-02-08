from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Point
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length
    from experience.cat_gsm_interfaces import HybridShapeDirection

class HybridShapePointOnPlane(Point):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObcomect
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Point
                |                             HybridShapePointOnPlane
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_point_on_plane = com

    def first_direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapePointOnPlane', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_on_plane.FirstDirection = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_point_on_plane.FirstDirection)

    def plane(self, value: Reference = None) -> Union['HybridShapePointOnPlane', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_on_plane.Plane = value._com
            return self
        return Reference(self.hybrid_shape_point_on_plane.Plane)

    def point(self, value: Reference = None) -> Union['HybridShapePointOnPlane', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_on_plane.Point = value._com
            return self
        return Reference(self.hybrid_shape_point_on_plane.Point)

    def procomection_surface(self, value: Reference = None) -> Union['HybridShapePointOnPlane', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_on_plane.ProcomectionSurface = value._com
            return self
        return Reference(self.hybrid_shape_point_on_plane.ProcomectionSurface)

    def x_offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_point_on_plane.XOffset)

    def y_offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_point_on_plane.YOffset)

    def get_second_direction(self) -> None:
        return self._get_multi([self._com], ("HybridShapePointOnPlane", "GetSecondDirection"), ("Double", "Double", "Double"))

    def set_second_direction(self, i_dir_x: float, i_dir_y: float, i_dir_z: float) -> 'HybridShapePointOnPlane':
        self.hybrid_shape_point_on_plane.SetSecondDirection(i_dir_x, i_dir_y, i_dir_z)
        return self

    def __repr__(self):
        return f'HybridShapePointOnPlane(name="{self.name}")'