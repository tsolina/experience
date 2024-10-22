from typing import Iterator, TYPE_CHECKING

from experience.plm_interference_interfaces.interference_result import InterferenceResult
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class InterferenceResults(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     InterferenceResults
    """

    def __init__(self, com):
        super().__init__(com, child=InterferenceResult)
        self.interference_results = com

    def item(self, i_index: 'cat_variant') -> InterferenceResult:
        return InterferenceResult(self.interference_results.Item(i_index))

    def __getitem__(self, n: int) -> InterferenceResult:
        if (n + 1) > self.count():
            raise StopIteration

        return InterferenceResult(self.interference_results.item(n + 1))

    def __iter__(self) -> Iterator[InterferenceResult]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
