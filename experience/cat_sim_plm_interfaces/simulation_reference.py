from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject
from experience.plm_modeler_base_interfaces.plm_entity import PLMEntity

if TYPE_CHECKING:
    from experience.cat_sim_plm_interfaces.simulation_results import SimulationResults
    from experience.cat_sim_plm_interfaces.simulation_specifications import SimulationSpecifications

class SimulationReference(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         SimulationReference
    """

    def __init__(self, com):
        super().__init__(com)
        self.simulation_reference = com

    def model(self) -> AnyObject:
        return AnyObject(self.simulation_reference.Model)

    def results(self) -> 'SimulationResults':
        from experience.cat_sim_plm_interfaces.simulation_results import SimulationResults
        return SimulationResults(self.simulation_reference.Results)
    
    def specifications(self) -> 'SimulationSpecifications':
        from experience.cat_sim_plm_interfaces.simulation_specifications import SimulationSpecifications
        return SimulationSpecifications(self.simulation_reference.Specifications)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'