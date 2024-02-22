from typing import Union
from experience.inf_interfaces.inf_types import *
from experience.inf_interfaces import Viewer2D

class SpecsViewer(Viewer2D):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Viewer
                |                         InfInterfaces.Viewer2D
                |                             SpecsViewer
    """
    def __init__(self, com):
        super().__init__(com)
        self.specs_viewer = com

    def layout(self, value: CatSpecsLayout = None) -> Union['SpecsViewer', CatSpecsLayout]:
        if value is not None:
            self.specs_viewer.Layout = int(value)
            return self
        return CatSpecsLayout.item(self.specs_viewer.Layout)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'