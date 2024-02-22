from typing import TYPE_CHECKING, Union
from experience.inf_interfaces import Viewer

if TYPE_CHECKING:
    from experience.inf_interfaces import Viewpoint2D

class Viewer2D(Viewer):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Viewer
                |                         Viewer2D
    """

    def __init__(self, com):
        super().__init__(com)
        self.viewer_2d = com

    def viewpoint_2d(self, value: 'Viewpoint2D' = None) -> Union['Viewer2D', 'Viewpoint2D']:
        if value is not None:
            self.viewer_2d.Viewpoint2D = value
            return self
        from experience.inf_interfaces import Viewpoint2D
        return Viewpoint2D(self.viewer_2d.Viewpoint2D)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'