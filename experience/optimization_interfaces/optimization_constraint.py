from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject
from experience.knowledge_interfaces.check import Check

if TYPE_CHECKING:
    from experience.knowledge_interfaces.real_param import RealParam

class OptimizationConstraint(Check):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                         KnowledgeIDLItf.KnowledgeActivateObject
                |                             KnowledgeIDLItf.Relation
                |                                 KnowledgeIDLItf.Check
                |                                     OptimizationConstraint
    """

    def __init__(self, com):
        super().__init__(com)
        self.optimization_constraint = com

    def distance_to_satisfaction(self) -> 'RealParam':
        from experience.knowledge_interfaces.real_param import RealParam
        return RealParam(self.optimization_constraint.DistanceToSatisfaction)
    
    def precision(self, value: float = None) -> Union['OptimizationConstraint', float]:
        if value is not None:
            self.optimization_constraint.Precision = value
            return self
        return self.optimization_constraint.Precision
    
    def satisfaction(self) -> bool:
        return self.optimization_constraint.Satisfaction()        
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'