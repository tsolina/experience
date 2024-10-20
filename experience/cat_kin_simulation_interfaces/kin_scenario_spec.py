from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_kin_mechanism_interfaces.kin_mechanism import KinMechanism
    from experience.cat_kin_simulation_interfaces.kin_recorded_excitation import KinRecordedExcitation

class KinScenarioSpec(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KinScenarioSpec
    """

    def __init__(self, com):
        super().__init__(com)
        self.kin_scenario_spec = com

    def end_time(self) -> float:
        return self.kin_scenario_spec.EndTime
    
    def mechanism(self) -> 'KinMechanism':
        return self.kin_scenario_spec.Mechanism
    
    def start_time(self) -> float:
        return self.kin_scenario_spec.StartTime
    
    def time_step(self) -> float:
        return self.kin_scenario_spec.TimeStep
    
    def add_recorded_excitation(self) -> 'KinRecordedExcitation':
        from experience.cat_kin_simulation_interfaces.kin_recorded_excitation import KinRecordedExcitation
        return KinRecordedExcitation(self.kin_scenario_spec.AddRecordedExcitation())
    
    def get_recorded_excitation(self) -> 'KinRecordedExcitation':
        from experience.cat_kin_simulation_interfaces.kin_recorded_excitation import KinRecordedExcitation
        return KinRecordedExcitation(self.kin_scenario_spec.GetRecordedExcitation())
    
    def remove_recorded_excitation(self, i_recorded_excitation: 'KinRecordedExcitation') -> 'KinScenarioSpec':
        self.kin_scenario_spec.RemoveRecordedExcitation(i_recorded_excitation._com)
        return self
    
    def set_time_parameters(self, i_start_time: float, i_end_time: float, i_time_step: float) -> 'KinScenarioSpec':
        self.kin_scenario_spec.SetTimeParameters(i_start_time, i_end_time, i_time_step)
        return self
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'