from typing import Iterator, TYPE_CHECKING

from experience.knowledge_interfaces import ParameterSet
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class ParameterSets(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ParameterSets
    """

    def __init__(self, com):
        super().__init__(com, child=ParameterSet)
        self.parameter_sets = com

    def create_set(self, i_name: str) -> ParameterSet:
        return ParameterSet(self.parameter_sets.CreateSet(i_name))

    def item(self, i_index: 'cat_variant') -> ParameterSet:
        from experience.types import cat_variant
        return ParameterSet(self.parameter_sets.Item(i_index))

    def __getitem__(self, n: int) -> ParameterSet:
        if (n + 1) > self.count:
            raise StopIteration

        return ParameterSet(self.parameter_sets.item(n + 1))

    def __iter__(self) -> Iterator[ParameterSet]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'