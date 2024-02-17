from typing import Union, TYPE_CHECKING
from experience.knowledge_interfaces import Relation

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Parameter

class SetOfEquation(Relation):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                         KnowledgeIDLItf.KnowledgeActivateObject
                |                             KnowledgeIDLItf.Relation
                |                                 SetOfEquation
    """

    def __init__(self, com):
        super().__init__(com)
        self.set_of_equation = com

    def get_max_calculation_time(self) -> int:
        return self.set_of_equation.GetMaxCalculationTime()
    
    def get_precision(self) -> float:
        return self.set_of_equation.GetPrecision()
    
    def get_symbolic_transformations(self) -> bool:
        return self.set_of_equation.GetSymbolcTransformations()
    
    def is_stop_dialog(self) -> bool:
        return self.set_of_equation.IsStopDialog()

    def set_input_parameters(self, i_index: int) -> 'SetOfEquation':
        self.set_of_equation.SetInputParameters(i_index)
        return self
    
    def set_max_calculation_time(self, i_max_time: int) -> 'SetOfEquation':
        self.set_of_equation.SetMaxCalculationTime(i_max_time)
        return self
    
    def set_parameter_as_input(self, i_parameter: 'Parameter') -> 'SetOfEquation':
        self.set_of_equation.SetParameterAsInput(i_parameter._com)
        return self
    
    def set_parameter_as_output(self, i_parameter: 'Parameter') -> 'SetOfEquation':
        self.set_of_equation.SetParameterAsOutput(i_parameter._com)
        return self

    def set_precision(self, i_eps: float) -> 'SetOfEquation':
        self.set_of_equation.SetPrecision(i_eps)
        return self
    
    def use_stop_dialog(self, i_used: bool) -> 'SetOfEquation':
        self.set_of_equation.UseStopDialog(i_used)
        return self 

    def use_symbolic_transformations(self, i_gauss: bool) -> 'SetOfEquation':
        self.set_of_equation.UseSymbolcTransformations(i_gauss)
        return self        

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'