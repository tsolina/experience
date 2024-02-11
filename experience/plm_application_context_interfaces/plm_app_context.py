from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Service

if TYPE_CHECKING:
    from experience.plm_modeler_base_interfaces import PLMEntities

class PLMAppContext(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         PLMAppContext
    """

    def __init__(self, com):
        super().__init__(com)
        self.plm_app_context = com
    
    def edited_content(self) -> 'PLMEntities':
        from experience.plm_modeler_base_interfaces import PLMEntities
        return PLMEntities(self.plm_app_context.EditedContent())

    def __repr__(self):
        return f'PLMAppContext(name="{self.name()}")'