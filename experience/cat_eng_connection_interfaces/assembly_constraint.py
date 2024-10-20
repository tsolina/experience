from typing import Iterator, TYPE_CHECKING, Union

from .cat_eng_connection_types import *
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.knowledge_interfaces.parameter import Parameter

class AssemblyConstraint(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AssemblyConstraint
    """

    def __init__(self, com):
        super().__init__(com)
        self.assembly_constraint = com

    def activity(self, value: bool = None) -> Union['AssemblyConstraint', bool]:
        if value is not None:
            self.assembly_constraint.Activity = value
            return self
        return self.assembly_constraint.Activity
    
    def mode(self, value: CatAssemblyConstraintMode = None) -> Union['AssemblyConstraint', CatAssemblyConstraintMode]:
        if value is not None:
            self.assembly_constraint.Mode = int(value)
            return self
        return CatAssemblyConstraintMode.item(self.assembly_constraint.Mode) 
    
    def type(self, value: CatAssemblyConstraintType = None) -> Union['AssemblyConstraint', CatAssemblyConstraintType]:
        if value is not None:
            self.assembly_constraint.Type = int(value)
            return self
        return CatAssemblyConstraintType.item(self.assembly_constraint.Type) 
    
    def get_max_value(self, i_nbv: int) -> float:
        return self.assembly_constraint.GetMaxValue(i_nbv)
    
    def get_max_value_as_param(self, i_nbv: int) -> 'Parameter':
        from experience.knowledge_interfaces.parameter import Parameter
        return Parameter(self.assembly_constraint.GetMaxValueAsParam(i_nbv))
    
    def get_min_value(self, i_nbv: int) -> float:
        return self.assembly_constraint.GetMinValue(i_nbv)

    def get_min_value_as_param(self, i_nbv: int) -> 'Parameter':
        from experience.knowledge_interfaces.parameter import Parameter
        return Parameter(self.assembly_constraint.GetMinValueAsParam(i_nbv))
    
    def get_nb_options(self) -> int:
        return self.assembly_constraint.GetNbOptions()
    
    def get_nb_supports(self) -> int:
        return self.assembly_constraint.GetNbSupports()
    
    def get_nb_values(self) -> int:
        return self.assembly_constraint.GetNbValues()
    
    def get_option(self, i_num_option) -> CatAssemblyConstraintOption:
        return CatAssemblyConstraintOption.item(self.assembly_constraint.GetOption)
    
    def get_support(self, i_num_support: int, i_b_fold: bool) -> tuple[str, str]:
        return self._get_multi([self.assembly_constraint, i_num_support, i_b_fold], 
                               ('AssemblyConstraint', 'GetSupport', 'short', 'boolean'),
                               ("String", "String"))
    
    def get_value(self, i_nbv: int) -> float:
        return self.assembly_constraint.GetValue(i_nbv)
    
    def get_value_as_param(self, i_nbv: int) -> 'Parameter':
        return Parameter(self.assembly_constraint.GetValueAsParam(i_nbv))
    
    def set_max_value(self, i_nbv: int, i_val: float) -> 'AssemblyConstraint':
        self.assembly_constraint.SetMaxValue(i_nbv, i_val)
        return self
    
    def set_min_value(self, i_nbv: int, i_val: float) -> 'AssemblyConstraint':
        self.assembly_constraint.SetMinValue(i_nbv, i_val)
        return self
    
    def set_option(self, i_num_option: int, i_option: CatAssemblyConstraintOption) -> 'AssemblyConstraint':
        self.assembly_constraint.SetOption(i_num_option, int(i_option))
        return self
    
    def set_value(self, i_nbv: int, i_val: float) -> 'AssemblyConstraint':
        self.assembly_constraint.SetValue(i_nbv, i_val)
        return self
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'