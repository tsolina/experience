from typing import Iterator, TYPE_CHECKING

from experience.optimization_interfaces.optimization import Optimization
from experience.system import Collection, AnyObject

if TYPE_CHECKING:
    from experience.types import cat_variant
    from experience.knowledge_interfaces.set_of_equation import SetOfEquation

class Optimizations(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Optimizations
    """

    def __init__(self, com):
        super().__init__(com, child=Optimization)
        self.optimizations = com

    def create_constraints_satisfaction(self, i_name: str, i_comment: str, i_formula_body: str) -> 'SetOfEquation':
        from experience.knowledge_interfaces.set_of_equation import SetOfEquation
        return SetOfEquation(self.optimizations.CreateConstraintsSatisfaction(i_name, i_comment, i_formula_body))
    
    def create_optimization(self) -> Optimization:
        return Optimization(self.optimizations.CreateOptimization)

    def item(self, i_index: 'cat_variant') -> AnyObject:
        return AnyObject(self.optimizations.Item(i_index))

    def __getitem__(self, n: int) -> Optimization:
        if (n + 1) > self.count():
            raise StopIteration

        return Optimization(self.optimizations.item(n + 1))

    def __iter__(self) -> Iterator[Optimization]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
