from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_sim_rep_interfaces.sim_excitations import SimExcitations
    from experience.cat_sim_rep_interfaces.sim_probes import SimProbes
    from experience.cat_sim_rep_interfaces.sim_scenario_specs import SimScenarioSpecs

class SimSpecsRepManager(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSpecsRepManager
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_specs_rep_manager = com

    def excitations(self) -> 'SimExcitations':
        from experience.cat_sim_rep_interfaces.sim_excitations import SimExcitations
        return SimExcitations(self.sim_specs_rep_manager.Excitations)
    
    def probes(self) -> 'SimProbes':
        from experience.cat_sim_rep_interfaces.sim_probes import SimProbes
        return SimProbes(self.sim_specs_rep_manager.Probes)
    
    def scenario_specs(self) -> 'SimScenarioSpecs':
        from experience.cat_sim_rep_interfaces.sim_scenario_specs import SimScenarioSpecs
        return SimScenarioSpecs(self.sim_specs_rep_manager.ScenarioSpecs)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'