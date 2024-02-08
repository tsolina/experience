from typing import Union, Optional, TYPE_CHECKING

from experience.mecmod_interfaces import HybridShape

class Plane(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         Plane
    """

    def __init__(self, com):
        super().__init__(com)
        self.plane = com

    def get_first_axis(self) -> tuple[float, float, float]:
        return self._get_safe_array(self._com, "GetFirstAxis", 2)

    def get_origin(self, o_origin: tuple) -> tuple[float, float, float]:
        return self._get_safe_array(self._com, "GetOrigin", 2)

    def get_position(self) -> tuple[float, float, float]:
        return self._get_multi(([self._com]), ("Plane", 'GetPosition'), ("Double", "Double", "Double"))

    def get_second_axis(self) -> tuple[float, float, float]:
        return self._get_safe_array(self._com, "GetSecondAxis", 2)
 
    def is_a_ref_plane(self) -> int:
        return self.plane.IsARefPlane()

    def put_first_axis(self, i_first_axis: tuple[float, float, float]) -> 'Plane':
        self.plane.PutFirstAxis(i_first_axis)
        return self

    def put_origin(self, i_origin: tuple[float, float, float]) -> 'Plane':
        self.plane.PutOrigin(i_origin)
        return self

    def put_second_axis(self, i_second_axis: tuple[float, float, float]) -> 'Plane':
        self.plane.PutSecondAxis(i_second_axis)
        return self

    def remove_position(self) -> 'Plane':
        self.plane.RemovePosition()
        return self

    def set_position(self, i_x: float, i_y: float, i_z: float) -> 'Plane':
        self.plane.SetPosition(i_x, i_y, i_z)
        return self

    def __repr__(self):
        return f'Plane(name="{ self.name }")'