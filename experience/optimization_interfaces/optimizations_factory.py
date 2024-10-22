from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject
from experience.knowledge_interfaces.knowledge_factory import KnowledgeFactory

if TYPE_CHECKING:
    from experience.knowledge_interfaces.set_of_equation import SetOfEquation
    from experience.optimization_interfaces.optimization import Optimization

class OptimizationsFactory(KnowledgeFactory):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeFactory
                |                         OptimizationsFactory
    """

    def __init__(self, com):
        super().__init__(com)
        self.optimizations_factory = com

    def create_constraints_satisfaction(self, i_name: str, i_comment: str, i_constraint_satisfaction_body: str) -> 'SetOfEquation':
        from experience.knowledge_interfaces.set_of_equation import SetOfEquation
        return SetOfEquation(self.optimizations_factory.CreateConstraintsSatisfaction(i_name, i_comment, i_constraint_satisfaction_body))
    
    def create_optimization(self, i_name: str) -> 'Optimization':
        from experience.optimization_interfaces.optimization import Optimization
        return Optimization(self.optimizations_factory.CreateOptimization(i_name))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'