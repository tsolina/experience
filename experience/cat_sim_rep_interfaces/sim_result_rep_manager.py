from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_sim_rep_interfaces.sim_scenario_results import SimScenarioResults

class SimResultRepManager(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimResultRepManager
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_result_rep_manager = com

    def scenario_results(self) -> 'SimScenarioResults':
        return self.sim_result_rep_manager.ScenarioResults
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'