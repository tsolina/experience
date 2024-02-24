from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Service, Reference
from experience.system import AnyObject


if TYPE_CHECKING:
    from experience.plm_modeler_base_interfaces import PLMEntities, PLMOccurrence
    from experience.product_structure_client_interfaces import VPMRootOccurrence, VPMRepInstance

class PLMProductService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         PLMProductService
    """

    def __init__(self, com):
        super().__init__(com)
        self.plm_product_service = com
    
    def edited_content(self) -> 'PLMEntities':
        return PLMEntities(self.plm_product_service.EditedContent)
    
    def root_occurrence(self) -> 'VPMRootOccurrence':
        return VPMRootOccurrence(self.plm_product_service.RootOccurrence)
    
    def compose_link(self, i_plm_occurrence: 'PLMOccurrence', i_vpm_rep_instance: 'VPMRepInstance', i_catia_reference: 'Reference') -> AnyObject:
        return AnyObject(self.plm_product_service.ComposeLink(i_plm_occurrence._com, i_vpm_rep_instance._com, i_catia_reference._com))