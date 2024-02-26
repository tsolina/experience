from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from experience.plm_validation_interfaces import VALCheck

if TYPE_CHECKING:
    from experience.types import cat_variant

class VALChecks(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     VALChecks
    """
    def __init__(self, com):
        super().__init__(com, child=VALCheck)
        self.val_checks = com

    def add(self) -> VALCheck:
        return VALCheck(self.val_checks.Add())

    def item(self, i_index: 'cat_variant') -> VALCheck:
        return VALCheck(self.val_checks.Item(i_index))
    
    def remove(self, i_index: 'cat_variant') -> 'VALChecks':
        self.val_checks.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> VALCheck:
        if (n + 1) > self.count():
            raise StopIteration
        return VALCheck(self.val_checks.item(n + 1))

    def __iter__(self) -> Iterator[VALCheck]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))