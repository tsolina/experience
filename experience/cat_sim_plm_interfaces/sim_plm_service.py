from typing import Iterator, TYPE_CHECKING, Union

from experience.inf_interfaces.service import Service

if TYPE_CHECKING:
    from experience.plm_modeler_base_interfaces.plm_entity import PLMEntity
    from experience.cat_sim_plm_interfaces.simulation_reference import SimulationReference
    from experience.inf_interfaces.editor import Editor

class SIMPLMService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         SIMPLMService
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_plm_service = com

    def plm_create(self, i_simulation_name: str, i_simulation_type: str, i_context: 'PLMEntity') -> tuple['SimulationReference', "Editor"]:
        rval = self._get_multi([self.sim_plm_service, i_simulation_name, i_simulation_type, i_context._com],
                               ('SIMPLMService', 'PLMCreate', 'String', 'String', 'PLMEntity'),
                               ('SimulationReference', 'Editor'))
        from experience.cat_sim_plm_interfaces.simulation_reference import SimulationReference
        from experience.inf_interfaces.editor import Editor
        return SimulationReference(rval[0]), Editor(rval[1])
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'