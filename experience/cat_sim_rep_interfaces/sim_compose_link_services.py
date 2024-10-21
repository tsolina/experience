from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.plm_modeler_base_interfaces.plm_occurrence import PLMOccurrence
    from experience.product_structure_client_interfaces.vpm_rep_instance import VPMRepInstance
    from experience.inf_interfaces.reference import Reference

class SimComposeLinkServices(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimComposeLinkServices
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_compose_link_services = com

    def compose_link(self, i_plm_occurrence: 'PLMOccurrence' = None, i_vpm_rep_instance: 'VPMRepInstance' = None, i_catia_reference: 'Reference' = None) -> AnyObject:
        occ = None if i_plm_occurrence is None else i_plm_occurrence._com
        rep_i = None if i_vpm_rep_instance is None else i_vpm_rep_instance._com
        ref = None if i_catia_reference is None else i_catia_reference._com
        return AnyObject(self.sim_compose_link_services.ComposeLink(occ, rep_i, ref))
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'