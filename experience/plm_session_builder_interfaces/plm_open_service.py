from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Service

if TYPE_CHECKING:
    from experience.types import cat_variant
    from experience.inf_interfaces import Editor
    from experience.plm_modeler_base_interfaces import PLMEntity

class PLMOpenService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         PLMOpenService
    """

    def __init__(self, com):
        super().__init__(com)
        self.plm_open_service = com
    
    def plm_open(self, i_plm_entity: 'PLMEntity') -> 'Editor':
        from experience.inf_interfaces import Editor
        #return Editor(self._get_multi([self.plm_open_service, i_plm_entity._com], ("PLMOpenService", "PLMOpen", "PLMEntity"), ["Editor"]))
        return Editor(self.plm_open_service.PLMOpen(i_plm_entity._com)) 
        

    def plm_open_in_new_window(self, i_plm_entity: 'PLMEntity') -> 'Editor':
        from experience.inf_interfaces import Editor
        return Editor(self.plm_open_service.PLMOpenInNewWindow(i_plm_entity._com)) 
    
    def get_last_error(self) -> tuple[str, int]:
        return self._get_multi([self._com],("PLMOpenService", "getLastError"),("String", "Long"))

    def __repr__(self):
        return f'PLMOpenService(name="{self.name()}")'