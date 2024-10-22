from typing import Iterator, TYPE_CHECKING

from experience.optimization_interfaces.free_parameter import FreeParameter
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant
    from experience.knowledge_interfaces.real_param import RealParam

class FreeParameters(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     FreeParameters
    """

    def __init__(self, com):
        super().__init__(com, child=FreeParameter)
        self.free_parameters = com

    def add_free_parameter(self, i_parameter: 'RealParam') -> FreeParameter:
        return FreeParameter(self.free_parameters.AddFreeParameter(i_parameter._com))

    def item(self, i_index: 'cat_variant') -> FreeParameter:
        return FreeParameter(self.free_parameters.Item(i_index))

    def remove_free_parameter(self, i_index: 'cat_variant') -> 'FreeParameters':
        self.free_parameters.RemoveFreeParameter(i_index)
        return self

    def __getitem__(self, n: int) -> FreeParameter:
        if (n + 1) > self.count():
            raise StopIteration

        return FreeParameter(self.free_parameters.item(n + 1))

    def __iter__(self) -> Iterator[FreeParameter]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
