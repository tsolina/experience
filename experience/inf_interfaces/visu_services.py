from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Service

if TYPE_CHECKING:
    from experience.inf_interfaces import Cameras, Window

class VisuServices(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         VisuServices
    """

    def __init__(self, com):
        super().__init__(com)
        self.visu_services = com

    def cameras(self) -> 'Cameras':
        from experience.inf_interfaces import Cameras
        return Cameras(self.visu_services.Cameras)

    def current_filter(self, value: str = None) -> Union['VisuServices', str]:
        if value is not None:
            self.visu_services.CurrentFilter = value
            return self
        return self.visu_services.CurrentFilter

    def current_layer(self, value: str = None) -> Union['VisuServices', str]:
        if value is not None:
            self.visu_services.CurrentLayer = value
            return self
        return self.visu_services.CurrentLayer   

    def see_hidden_elements(self, value: bool = None) -> Union['VisuServices', bool]:
        if value is not None:
            self.visu_services.SeeHiddenElements = value
            return self
        return self.visu_services.SeeHiddenElements
    
    def create_filter(self, i_filter_name: str, i_filter_definition: str) -> 'VisuServices':
        self.visu_services.CreateFilter(i_filter_name, i_filter_definition)
        return self
    
    def new_window(self) -> 'Window':
        return Window(self.visu_services.NewWindow())

    def remove_filter(self, i_filter_name: str) -> 'VisuServices':
        self.visu_services.RemoveFilter()
        return self

    def __repr__(self):
        return f'VisuServices(name="{self.name()}")'