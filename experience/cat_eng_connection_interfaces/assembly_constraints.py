from typing import Iterator, TYPE_CHECKING

from experience.cat_eng_connection_interfaces.cat_eng_connection_types import *
from experience.cat_eng_connection_interfaces.assembly_constraint import AssemblyConstraint
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class AssemblyConstraints(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AssemblyConstraints
    """

    def __init__(self, com):
        super().__init__(com, child=AssemblyConstraint)
        self.assembly_constraint = com

    def add(self, i_type: CatAssemblyConstraintType, i_geometries: list) -> AssemblyConstraint:
        return AssemblyConstraint(self.assembly_constraint.Add(int(i_type), i_geometries))

    def item(self, i_index: 'cat_variant') -> AssemblyConstraint:
        return AssemblyConstraint(self.assembly_constraint.Item(i_index))

    def remove(self, i_eng_connection: AssemblyConstraint) -> 'AssemblyConstraints':
        self.assembly_constraint.Remove(i_eng_connection._com)
        return self

    def __getitem__(self, n: int) -> AssemblyConstraint:
        if (n + 1) > self.count():
            raise StopIteration

        return AssemblyConstraint(self.assembly_constraint.item(n + 1))

    def __iter__(self) -> Iterator[AssemblyConstraint]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
