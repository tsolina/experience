from typing import Union
from experience.system import AnyObject
from experience.inf_interfaces.inf_types import *

class Viewpoint3D(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Viewpoint3D
    """

    def __init__(self, com):
        super().__init__(com)
        self.viewpoint_3d = com

    def field_of_view(self, value: float = None) -> Union['Viewpoint3D', float]:
        if value is not None:
            self.viewpoint_3d.FieldOfView = value
            return self
        return self.viewpoint_3d.FieldOfView

    def focus_distance(self, value: float = None) -> Union['Viewpoint3D', float]:
        if value is not None:
            self.viewpoint_3d.FocusDistance = value
            return self
        return self.viewpoint_3d.FocusDistance

    def projection_mode(self, value: CatProjectionMode = None) -> Union['Viewpoint3D', CatProjectionMode]:
        if value is not None:
            self.viewpoint_3d.ProjectionMode = int(value)
            return self
        return CatProjectionMode.item(self.viewpoint_3d.ProjectionMode)

    def zoom(self, value: float = None) -> Union['Viewpoint3D', float]:
        if value is not None:
            self.viewpoint_3d.Zoom = value
            return self
        return self.viewpoint_3d.Zoom

    def get_origin(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.viewpoint_3d, "GetOrigin", 2)

    def get_sight_direction(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.viewpoint_3d, "GetSightDirection", 2)

    def get_up_direction(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.viewpoint_3d, "GetUpDirection", 2)

    def put_origin(self, origin: tuple[float, float, float]) -> None:
        return self.viewpoint_3d.PutOrigin(origin)

    def put_sight_direction(self, o_sight: tuple[float, float, float]) -> None:
        return self.viewpoint_3d.PutSightDirection(o_sight)

    def put_up_direction(self, o_up: tuple[float, float, float]) -> None:
        return self.viewpoint_3d.PutUpDirection(o_up)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'