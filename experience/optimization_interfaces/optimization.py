from typing import Iterator, TYPE_CHECKING, Union

from .optimization_types import *
from experience.system import AnyObject
from experience.knowledge_interfaces.knowledge_object import KnowledgeObject

if TYPE_CHECKING:
    from experience.optimization_interfaces.optimization_constraints import OptimizationConstraints
    from experience.optimization_interfaces.free_parameters import FreeParameters
    from experience.knowledge_interfaces.real_param import RealParam

class Optimization(KnowledgeObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                         Optimization
    """

    def __init__(self, com):
        super().__init__(com)
        self.optimization = com

    def algoritm_type(self, value: CatAlgorithmType = None) -> Union["Optimization" ,CatAlgorithmType]:
        if value is not None:
            self.optimization.AlgorithmType = int(value)
            return self
        return CatAlgorithmType.item(self.optimization.AlgorithmType)
    
    def constraints(self) -> 'OptimizationConstraints':
        from experience.optimization_interfaces.optimization_constraints import OptimizationConstraints
        return OptimizationConstraints(self.optimization.Constraints)
        
    def conv_speed(self, value: int = None) -> Union['Optimization', int]:
        if value is not None:
            self.optimization.ConvSpeed = value
            return self
        return self.optimization.ConvSpeed
    
    def free_parameters(self) -> 'FreeParameters':
        from experience.optimization_interfaces.free_parameters import FreeParameters
        return FreeParameters(self.optimization.FreeParameters)
    
    def max_evals_nb(self, value: int = None) -> Union['Optimization', int]:
        if value is not None:
            self.optimization.MaxEvalsNb = value
            return self
        return self.optimization.MaxEvalsNb
    
    def max_evals_wo_improvement(self, value: int = None) -> Union['Optimization', int]:
        if value is not None:
            self.optimization.MaxEvalsWoImprovement = value
            return self
        return self.optimization.MaxEvalsWoImprovement
    
    def max_time(self, value: int = None) -> Union['Optimization', int]:
        if value is not None:
            self.optimization.MaxTime = value
            return self
        return self.optimization.MaxTime
    
    def objective_parameter(self, value: 'RealParam' = None) -> Union['Optimization', 'RealParam']:
        if value is not None:
            self.optimization.ObjectiveParameter = value._com
            return self
        from experience.knowledge_interfaces.real_param import RealParam
        return RealParam(self.optimization.ObjectiveParameter)
    
    def optimization_type(self, value: CatOptimizationType = None) -> Union["Optimization" ,CatOptimizationType]:
        if value is not None:
            self.optimization.OptimizationType = int(value)
            return self
        return CatOptimizationType.item(self.optimization.OptimizationType)
    
    def target_value(self) -> 'RealParam':
        from experience.knowledge_interfaces.real_param import RealParam
        return RealParam(self.optimization.TargetValue)
    
    def use_max_evals_wo_improvement(self, value: bool = None) -> Union['Optimization', bool]:
        if value is not None:
            self.optimization.UseMaxEvalsWoImprovement = value
            return self
        return self.optimization.UseMaxEvalsWoImprovement
    
    def use_max_time(self, value: bool = None) -> Union['Optimization', bool]:
        if value is not None:
            self.optimization.UseMaxTime = value
            return self
        return self.optimization.UseMaxTime
    
    def run(self, i_with_stop_dialog: bool) -> 'Optimization':
        self.optimization.Run(i_with_stop_dialog)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'