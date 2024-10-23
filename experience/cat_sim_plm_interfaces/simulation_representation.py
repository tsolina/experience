from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject
from experience.cat_sim_plm_interfaces.simulation_object import SimulationObject

class SimulationRepresentation(SimulationObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         CATSimPLMIDLItf.SimulationObject
                |                             SimulationRepresentation
    """

    def __init__(self, com):
        super().__init__(com)
        self.simulation_representation = com

    def root(self) -> AnyObject:
        return AnyObject(self.simulation_object.Root)
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'