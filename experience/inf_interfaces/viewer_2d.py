from experience.inf_interfaces.viewer import Viewer
from experience.inf_interfaces.viewpoint_2d import Viewpoint2D

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

    def viewpoint_2d(self, value: Viewpoint2D = None) -> Viewpoint2D:
        if value is not None:
            self.viewer_2d.Viewpoint2D = value
            return self
        return Viewpoint2D(self.viewer_2d.Viewpoint2D)

    def __repr__(self):
        return f'Viewer2D(name="{self.name}")'
