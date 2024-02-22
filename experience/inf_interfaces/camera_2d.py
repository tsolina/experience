from typing import TYPE_CHECKING

from experience.inf_interfaces import Camera

if TYPE_CHECKING:
    from experience.inf_interfaces import Viewpoint2D

class Camera2D(Camera):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Camera
                |                         Camera2D
    """

    def __init__(self, com):
        super().__init__(com)
        self.camera_2d = com

    def viewpoint_2d(self, value: 'Viewpoint2D' = None) -> 'Viewpoint2D':
        if value is not None:
            self.camera_2d.Viewpoint2D = value
            return self
        from experience.inf_interfaces import Viewpoint2D
        return Viewpoint2D(self.camera_2d.Viewpoint2D)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'