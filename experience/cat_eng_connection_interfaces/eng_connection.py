from typing import Iterator, TYPE_CHECKING, Union

from .cat_eng_connection_types import *
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_eng_connection_interfaces.assembly_constraints import AssemblyConstraints

class EngConnection(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     EngConnection
    """

    def __init__(self, com):
        super().__init__(com)
        self.eng_connection = com

    def activity(self, value: bool = None) -> Union['EngConnection', bool]:
        if value is not None:
            self.eng_connection.Activity = value
            return self
        return self.eng_connection.Activity
    
    def assembly_constraints(self) -> 'AssemblyConstraints':
        from experience.cat_eng_connection_interfaces.assembly_constraints import AssemblyConstraints
        return AssemblyConstraints(self.eng_connection.AssemblyConstraints)
    
    def type(self, value: CatAssemblyConstraintType = None) -> Union['EngConnection', CatAssemblyConstraintType]:
        if value is not None:
            self.eng_connection.Type = int(value)
            return self
        return CatAssemblyConstraintType.item(self.eng_connection.Type) 
    
    def compute_equivalent_type(self) -> 'EngConnection':
        self.eng_connection.ComputeEquivalentType()
        return self
    
    def get_direction(self, i_nbp: int) -> CatEngConnectionDirection:
        return CatEngConnectionDirection.item(self.eng_connection.GetDirection(i_nbp))
    
    def get_impacted(self, i_num_impacted: int) -> tuple[str, str]:
        return self._get_multi([self.eng_connection, i_num_impacted], ('EngConnection', 'GetImpacted', 'short'), ('String', 'String'))

    def get_nb_impacteds(self) -> int:
        return self.eng_connection.GetNbImpacteds()
    
    def set_direction(self, i_nbp: int, i_direction: CatEngConnectionDirection) -> 'EngConnection':
        self.eng_connection.SetDirection(i_nbp, int(i_direction))
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'