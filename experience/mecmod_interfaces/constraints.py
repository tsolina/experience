from typing import Iterator

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import Constraint
from experience.system import Collection
from experience.types import cat_variant

class Constraints(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Constraints
    """

    def __init__(self, com):
        super().__init__(com, child=Constraint)
        self.constraints = com

    def broken_constraints_count(self) -> int:
        return self.constraints.BrokenConstraintsCount

    def un_updated_constraints_count(self) -> int:
        return self.constraints.UnUpdatedConstraintsCount

    def add_bi_elt_cst(self, i_cst_type: int, i_first_elem: Reference, i_second_elem: Reference) -> Constraint:
        return Constraint(self.constraints.AddBiEltCst(i_cst_type, i_first_elem._com, i_second_elem._com))

    def add_mono_elt_cst(self, i_cst_type: int, i_elem: Reference) -> Constraint:
        return Constraint(self.constraints.AddMonoEltCst(i_cst_type, i_elem._com))

    def add_tri_elt_cst(self, i_cst_type: int, i_first_elem: Reference, i_second_elem: Reference, i_third_elem: Reference) -> Constraint:
        return Constraint(self.constraints.AddTriEltCst(i_cst_type, i_first_elem._com, i_second_elem._com, i_third_elem._com))

    def item(self, i_index: cat_variant) -> Constraint:
        return Constraint(self.constraints.Item(i_index))

    def remove(self, i_index: cat_variant) -> 'Constraints':
        self.constraints.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> Constraint:
        if (n + 1) > self.count():
            raise StopIteration

        return Constraint(self.constraints.item(n + 1))

    def __iter__(self) -> Iterator[Constraint]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'Constraints(name="{self.name()}")'