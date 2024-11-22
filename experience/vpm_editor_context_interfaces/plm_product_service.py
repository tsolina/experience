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
        from experience.plm_modeler_base_interfaces import PLMEntities
        return PLMEntities(self.plm_product_service.EditedContent)
    
    def root_occurrence(self) -> 'VPMRootOccurrence':
        from experience.product_structure_client_interfaces import VPMRootOccurrence
        return VPMRootOccurrence(self.plm_product_service.RootOccurrence)
    
    def compose_link(self, i_plm_occurrence:Optional['PLMOccurrence']=None, i_vpm_rep_instance:Optional['VPMRepInstance']=None, i_catia_reference:Optional['Reference']=None) -> AnyObject:
        plm_occurrence_com = i_plm_occurrence._com if i_plm_occurrence else None
        vpm_rep_instance_com = i_vpm_rep_instance._com if i_vpm_rep_instance else None
        catia_reference_com = i_catia_reference._com if i_catia_reference else None 
        return AnyObject(self.plm_product_service.ComposeLink(plm_occurrence_com, vpm_rep_instance_com, catia_reference_com))