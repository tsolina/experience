from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject
from experience.inf_interfaces.service import Service

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces.vpm_root_occurence import VPMRootOccurrence
    from experience.cat_sim_plm_interfaces.simulation_reference import SimulationReference

class SimSimulationService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         SimSimulationService
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_simulation_service = com

    def get_product_root_occurrence(self, ip_simulation_reference: 'SimulationReference') -> 'VPMRootOccurrence':
        from experience.product_structure_client_interfaces.vpm_root_occurence import VPMRootOccurrence
        return VPMRootOccurrence(self.sim_simulation_service.GetProductRootOccurrence(ip_simulation_reference._com))
    
    def get_simulation_reference_from_object(self, i_object: AnyObject) -> 'SimulationReference':
        from experience.cat_sim_plm_interfaces.simulation_reference import SimulationReference
        return SimulationReference(self.sim_simulation_service.GetSimulationReferenceFromObject(i_object._com))
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'