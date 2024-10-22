from typing import Iterator, TYPE_CHECKING

from experience.optimization_interfaces.optimization_constraint import OptimizationConstraint
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class OptimizationConstraints(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     OptimizationConstraints
    """

    def __init__(self, com):
        super().__init__(com, child=OptimizationConstraint)
        self.optimization_constraints = com

    def add_constraint(self, constraint_expression: str) -> OptimizationConstraint:
        return OptimizationConstraint(self.optimization_constraints.AddConstraint(constraint_expression))

    def item(self, i_index: 'cat_variant') -> OptimizationConstraint:
        return OptimizationConstraint(self.optimization_constraints.Item(i_index))

    def remove(self, i_index: 'cat_variant') -> 'OptimizationConstraints':
        self.optimization_constraints.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> OptimizationConstraint:
        if (n + 1) > self.count():
            raise StopIteration

        return OptimizationConstraint(self.optimization_constraints.item(n + 1))

    def __iter__(self) -> Iterator[OptimizationConstraint]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
