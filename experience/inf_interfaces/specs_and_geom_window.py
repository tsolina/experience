from typing import Union, TYPE_CHECKING
from experience.system import AnyObject
from experience.inf_interfaces.inf_types import *
from experience.inf_interfaces import Window

if TYPE_CHECKING:
    from experience.inf_interfaces import SpecsViewer

class SpecsAndGeomWindow(Window):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Window
                |                         SpecsAndGeomWindow
    """
    def __init__(self, com):
        super().__init__(com)
        self.specs_and_geom_window = com

    def layout(self, value: CatSpecsAndGeomWindowLayout = None) -> Union['SpecsAndGeomWindow', CatSpecsAndGeomWindowLayout]:
        if value is not None:
            self.specs_and_geom_window.Layout = int(value)
            return self
        return CatSpecsAndGeomWindowLayout.item(self.specs_and_geom_window.Layout)
    
    def specs_viewer(self) -> 'SpecsViewer':
        from experience.inf_interfaces import SpecsViewer
        return SpecsViewer(self.specs_and_geom_window.SpecsViewer)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'