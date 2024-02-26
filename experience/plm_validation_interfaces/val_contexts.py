from typing import Iterator, TYPE_CHECKING

from experience.system import Collection, AnyObject

if TYPE_CHECKING:
    from experience.types import cat_variant

class VALContexts(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     VALContexts
    """
    def __init__(self, com):
        super().__init__(com, child=AnyObject)
        self.val_contexts = com

    def add(self) -> AnyObject:
        return AnyObject(self.val_contexts.Add())

    def item(self, i_index: 'cat_variant') -> AnyObject:
        return AnyObject(self.val_contexts.Item(i_index))
    
    def load(self, i_index: 'cat_variant') -> 'VALContexts':
        self.val_contexts.Load(i_index)
        return self

    def remove(self, i_index: 'cat_variant') -> 'VALContexts':
        self.val_contexts.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> AnyObject:
        if (n + 1) > self.count():
            raise StopIteration
        return AnyObject(self.val_contexts.item(n + 1))

    def __iter__(self) -> Iterator[AnyObject]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))