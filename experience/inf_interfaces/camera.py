from experience.system.any_object import AnyObject

from experience.inf_interfaces.inf_types import *

class Camera(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Camera
    """

    def __init__(self, com):
        super().__init__(com)
        self.camera = com

    def type(self) -> CatCameraType:
        return CatCameraType.item(self.camera.Type)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'