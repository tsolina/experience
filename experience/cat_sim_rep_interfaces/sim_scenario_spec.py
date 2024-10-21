from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_sim_rep_interfaces.sim_excitation import SimExcitation
    from experience.cat_sim_rep_interfaces.sim_excitations import SimExcitations
    from experience.cat_sim_rep_interfaces.sim_probe import SimProbe
    from experience.cat_sim_rep_interfaces.sim_probes import SimProbes
    from experience.cat_sim_rep_interfaces.sim_scenario_result import SimScenarioResult

class SimScenarioSpec(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimScenarioSpec
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_scenario_spec = com

    def excitations(self) -> 'SimExcitations':
        from experience.cat_sim_rep_interfaces.sim_excitations import SimExcitations
        return SimExcitations(self.sim_scenario_spec.Excitations)
    
    def is_current(self) -> bool:
        return self.sim_scenario_spec.IsCurrent
    
    def probes(self) -> 'SimProbes':
        from experience.cat_sim_rep_interfaces.sim_probes import SimProbes
        return SimProbes(self.sim_scenario_spec.Probes)
    
    def scenario_result(self) -> 'SimScenarioResult':
        from experience.cat_sim_rep_interfaces.sim_scenario_result import SimScenarioResult
        return SimScenarioResult(self.sim_scenario_spec.ScenarioResult)
    
    def solver_type(self) -> str:
        return self.sim_scenario_spec.SolverType
    
    def add_excitation(self, i_excitation: 'SimExcitation') -> 'SimScenarioSpec':
        self.sim_scenario_spec.AddExcitation(i_excitation._com)
        return self
    
    def add_probe(self, i_probe: 'SimProbe') -> 'SimScenarioSpec':
        self.sim_scenario_spec.AddProbe(i_probe._com)
        return self
    
    def get_behaviors(self) -> list:
        '''
        unclear what are behaviors, if they should be wrapped or not
        '''
        return self.sim_scenario_spec.GetBehaviors()
    
    def remove_excitation(self, i_excitation: 'SimExcitation') -> 'SimScenarioSpec':
        self.sim_scenario_spec.RemoveExcitation(i_excitation._com)
        return self
    
    def remove_probe(self, i_probe: 'SimProbe') -> 'SimScenarioSpec':
        self.sim_scenario_spec.RemoveProbe(i_probe._com)
        return self

    def set_current(self) -> 'SimScenarioSpec':
        self.sim_scenario_spec.SetCurrent()
        return self
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'