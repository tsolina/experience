from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces.reference import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle, Length

class HybridShapeDevelop(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeDevelop
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_develop = com

    def mode(self, value: int = None) -> Union['HybridShapeDevelop', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_develop.Mode = value
            return self
        return self.hybrid_shape_develop.Mode

    def mode_pos(self, value: int = None) -> Union['HybridShapeDevelop', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_develop.ModePos = value
            return self
        return self.hybrid_shape_develop.ModePos

    def plane_axis_direction(self, value: Reference = None) -> Union['HybridShapeDevelop', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_develop.PlaneAxisDirection = value._com
            return self
        return Reference(self.hybrid_shape_develop.PlaneAxisDirection)

    def plane_axis_origin(self, value: Reference = None) -> Union['HybridShapeDevelop', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_develop.PlaneAxisOrigin = value._com
            return self
        return Reference(self.hybrid_shape_develop.PlaneAxisOrigin)

    def point_on_support(self, value: Reference = None) -> Union['HybridShapeDevelop', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_develop.PointOnSupport = value._com
            return self
        return Reference(self.hybrid_shape_develop.PointOnSupport)

    def positioned_wire(self, value: Reference = None) -> Union['HybridShapeDevelop', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_develop.PositionedWire = value._com
            return self
        return Reference(self.hybrid_shape_develop.PositionedWire)

    def support(self, value: Reference = None) -> Union['HybridShapeDevelop', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_develop.Support = value._com
            return self
        return Reference(self.hybrid_shape_develop.Support)

    def wire_to_develop(self, value: Reference = None) -> Union['HybridShapeDevelop', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_develop.WireToDevelop = value._com
            return self
        return Reference(self.hybrid_shape_develop.WireToDevelop)

    def get_plane_axis_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_develop.GetPlaneAxisAngle())

    def get_plane_axis_coord(self, i_coor_idx: int) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_develop.GetPlaneAxisCoord(i_coor_idx))

    def get_plane_axis_swap_axes(self) -> int:
        return self.hybrid_shape_develop.GetPlaneAxisSwapAxes(0)

    def set_plane_axis_angle(self, i_angle: float) -> 'HybridShapeDevelop':
        self.hybrid_shape_develop.SetPlaneAxisAngle(i_angle)
        return self

    def set_plane_axis_coord(self, i_coor_idx: int, i_coord_value: float) -> 'HybridShapeDevelop':
        self.hybrid_shape_develop.SetPlaneAxisCoord(i_coor_idx, i_coord_value)
        return self

    def set_plane_axis_swap_axes(self, i_inversion_value: int) -> 'HybridShapeDevelop':
        return self.hybrid_shape_develop.SetPlaneAxisSwapAxes(0, i_inversion_value)

    def __repr__(self):
        return f'HybridShapeDevelop(name="{self.name}")'