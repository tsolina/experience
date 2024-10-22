from typing import Iterator, TYPE_CHECKING, Union

from .plm_interference_types import *
from experience.system import AnyObject
from experience.inf_interfaces.service import Service

if TYPE_CHECKING:
    from experience.plm_interference_interfaces.interference_simulation import InterferenceSimulation

class InterferenceServices(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         InterferenceServices
    """

    def __init__(self, com):
        super().__init__(com)
        self.interference_services = com

    def create_interference_simulation(self, i_reference: AnyObject) -> 'InterferenceSimulation':
        from experience.plm_interference_interfaces.interference_simulation import InterferenceSimulation
        return InterferenceSimulation(self._get_multi([self.interference_services, i_reference._com],
                                                      ("InterferenceServices", 'CreateInterferenceSimulation', 'AnyObject'),
                                                      ("InterferenceSimulation")))
    
    def create_interference_simulation2(self, i_reference: AnyObject, i_group_computation_type2: CatInterferenceGroupComputationType2) -> 'InterferenceSimulation':
        from experience.plm_interference_interfaces.interference_simulation import InterferenceSimulation
        return InterferenceSimulation(self._get_multi([self.interference_services, i_reference._com, int(i_group_computation_type2)],
                                                      ("InterferenceServices", "CreateInterferenceSimulation2", "AnyObject", "CatInterferenceGroupComputationType2"),
                                                      ("InterferenceSimulation")))        
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'