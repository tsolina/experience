from typing import Iterator, TYPE_CHECKING, Union

from .cat_kin_simulation_types import *
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_kin_simulation_interfaces.kin_simulation_channels import KinSimulationChannels

class KinSimulationScenarioResult(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KinSimulationScenarioResult
    """

    def __init__(self, com):
        super().__init__(com)
        self.kin_simulation_scenario_result = com

    def name(self) -> str:
        return self.kin_simulation_scenario_result.Name
    
    def get_result_channels(self, i_name_filtering: str, i_type_filtering: CatKinSimuChannelType) -> 'KinSimulationChannels':
        from experience.cat_kin_simulation_interfaces.kin_simulation_channels import KinSimulationChannels
        return KinSimulationChannels(self.kin_simulation_scenario_result.GetResultChannels(i_name_filtering, int(i_type_filtering)))
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'