from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from experience.plm_validation_interfaces import VALConcern

if TYPE_CHECKING:
    from experience.types import cat_variant

class VALConcerns(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     VALConcerns
    """
    def __init__(self, com):
        super().__init__(com, child=VALConcern)
        self.val_concerns = com

    def add(self) -> VALConcern:
        return VALConcern(self.val_concerns.Add())

    def item(self, i_index: 'cat_variant') -> VALConcern:
        return VALConcern(self.val_concerns.Item(i_index))
    
    def remove(self, i_index: 'cat_variant') -> 'VALConcerns':
        self.val_concerns.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> VALConcern:
        if (n + 1) > self.count():
            raise StopIteration
        return VALConcern(self.val_concerns.item(n + 1))

    def __iter__(self) -> Iterator[VALConcern]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))