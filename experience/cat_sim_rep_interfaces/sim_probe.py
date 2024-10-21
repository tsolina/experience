from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_sim_rep_interfaces.sim_scenario_spec import SimScenarioSpec

class SimProbe(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimProbe
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_probe = com

    def scenario_spec(self) -> 'SimScenarioSpec':
        from experience.cat_sim_rep_interfaces.sim_scenario_spec import SimScenarioSpec
        return SimScenarioSpec(self.sim_probe.ScenarioSpec)
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'