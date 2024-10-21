from typing import Iterator, TYPE_CHECKING, Union

from experience.inf_interfaces.service import Service
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.plm_modeler_base_interfaces.plm_occurrence import PLMOccurrence
    from experience.product_structure_client_interfaces.vpm_rep_instance import VPMRepInstance

class SimLinkServices(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         SimLinkServices
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_link_services = com
        
    def get_occurrence(self, i_link: AnyObject) -> 'PLMOccurrence':
        from experience.plm_modeler_base_interfaces.plm_occurrence import PLMOccurrence
        return PLMOccurrence(self.sim_link_services.GetOccurrence(i_link._com))
    
    def get_rep_instance(self, i_link: AnyObject) -> 'VPMRepInstance':
        from experience.product_structure_client_interfaces.vpm_rep_instance import VPMRepInstance
        return VPMRepInstance(self.sim_link_services.GetRepInstance(i_link._com))

    def get_target(self, i_link: AnyObject) -> AnyObject:
        return AnyObject(self.sim_link_services.GetTarget(i_link._com)) 
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'