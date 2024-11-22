from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from experience.plm_modeler_base_interfaces.plm_entity import PLMEntity

if TYPE_CHECKING:
    from experience.types.general import cat_variant

class ListObject(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ListObject
    """

    def __init__(self, com):
        super().__init__(com, child=PLMEntity)
        self.list_object = com

    def add(self, i_item_value: PLMEntity) -> 'ListObject':
        self.list_object.Add(i_item_value)
        return self
    
    def get(self, i_index: 'cat_variant') -> 'PLMEntity':
        return PLMEntity(self.list_object.Get(i_index))

    def item(self, i_index: 'cat_variant') -> 'PLMEntity':
        return PLMEntity(self.list_object.Item(i_index))
    
    def remove(self, i_index: 'cat_variant') -> 'ListObject':
        self.list_object.Remove(i_index)
        return self
    
    def name(self) -> str:
        return "ListObject"

    def __getitem__(self, n: int) -> PLMEntity:
        if (n + 1) > self.count():
            raise StopIteration

        return PLMEntity(self.list_object.item(n + 1))

    def __iter__(self) -> Iterator[PLMEntity]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'