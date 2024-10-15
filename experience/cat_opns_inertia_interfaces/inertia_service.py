from typing import Union, Optional, TYPE_CHECKING

from experience.system import AnyObject
from experience.inf_interfaces import Service
from experience.cat_opns_inertia_interfaces import Inertia

class InertiaService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         InertiaService
    """

    def __init__(self, com):
        super().__init__(com)
        self.inertia_service = com

    def get_inertia_element(self, i_selected_item: AnyObject) -> Inertia:
        return Inertia(self.inertia_service.GetInertiaElement(i_selected_item._com))
    
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'