from typing import TYPE_CHECKING

from experience.inf_interfaces import Camera

if TYPE_CHECKING:
    from experience.inf_interfaces import Viewpoint3D

class Camera3D(Camera):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Camera
                |                         Camera3D
    """

    def __init__(self, com):
        super().__init__(com)
        self.camera_3d = com

    def viewpoint_3d(self, value: 'Viewpoint3D' = None) -> 'Viewpoint3D':
        if value is not None:
            self.camera_3d.Viewpoint3D = value
            return self
        from experience.inf_interfaces import Viewpoint3D
        return Viewpoint3D(self.camera_3d.Viewpoint3D)

    def __repr__(self):
        return f'Camera3D(name="{self.name()}")'
