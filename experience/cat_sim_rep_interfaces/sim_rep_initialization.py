from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_sim_rep_interfaces.sim_parameter_set import SimParameterSet

class SimRepInitialization(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimRepInitialization
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_rep_initialization = com

    def parameters(self) -> 'SimParameterSet':
        from experience.cat_sim_rep_interfaces.sim_parameter_set import SimParameterSet
        return SimParameterSet(self.sim_rep_initialization.Parameters)
    
    def results(self) -> list[AnyObject]:
        objs = self.sim_rep_initialization.Results
        return [AnyObject(obj) for obj in objs]
        
    def initialize_rep(self, i_parameter_set: 'SimParameterSet') -> 'SimRepInitialization':
        self.sim_rep_initialization.InitializeRep(i_parameter_set._com)
        return self
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'