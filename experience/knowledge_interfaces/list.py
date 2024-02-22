from typing import Iterator, TYPE_CHECKING

from experience.system import AnyObject, Collection
if TYPE_CHECKING:
    from experience.types import cat_variant

class List(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     List
    """

    def __init__(self, com):
        super().__init__(com)
        self.list = com

    def add(self, i_item_value: AnyObject) -> 'List':
        self.list.Add(i_item_value._com)
        return self

    def item(self, i_index: 'cat_variant') -> AnyObject:
        from experience.types import cat_variant
        return AnyObject(self.list.Item(i_index))

    def remove(self, i_index: 'cat_variant') -> 'List':
        from experience.types import cat_variant
        self.list.Remove(i_index)
        return self

    def reorder(self, i_index_current: 'cat_variant', i_index_target: 'cat_variant') -> 'List':
        from experience.types import cat_variant
        self.list.Reorder(i_index_current, i_index_target)
        return self

    def replace(self, i_index: 'cat_variant', i_item_value: AnyObject) -> 'List':
        from experience.types import cat_variant
        self.list.Replace(i_index, i_item_value.com_object)
        return self

    def __getitem__(self, n: int) -> AnyObject:
        if (n + 1) > self.count:
            raise StopIteration

        return AnyObject(self.list.item(n + 1))

    def __iter__(self) -> Iterator[AnyObject]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'