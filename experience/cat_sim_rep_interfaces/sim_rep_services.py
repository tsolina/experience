from typing import Iterator, TYPE_CHECKING, Union

from experience.inf_interfaces.service import Service

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces.vpm_rep_reference import VPMRepReference

class SimRepServices(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         SimRepServices
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_rep_services = com

    def is_loaded(self, i_rep_reference: 'VPMRepReference') -> bool:
        return self.sim_rep_services.IsLoaded(i_rep_reference._com)
    
    def load_rep(self, i_rep_reference: 'VPMRepReference') -> 'SimRepServices':
        self.sim_rep_services.LoadRep(i_rep_reference._com)
        return self
    
    def unload_rep(self, i_rep_reference: 'VPMRepReference') -> 'SimRepServices':
        self.sim_rep_services.UnloadRep(i_rep_reference._com)
        return self
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'