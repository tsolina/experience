from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from experience.plm_modeler_base_interfaces import PLMEntity

if TYPE_CHECKING:
    from experience.types import cat_variant

class PLMEntities(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     PLMEntities
    """

    def __init__(self, com):
        super().__init__(com, child=PLMEntity)
        self.plm_entities = com

    def item(self, i_index: 'cat_variant') -> PLMEntity:
        return PLMEntity(self.plm_entities.Item(i_index))

    def __getitem__(self, n: int) -> PLMEntity:
        if (n + 1) > self.count():
            raise StopIteration
        return PLMEntity(self.plm_entities.item(n + 1))

    def __iter__(self) -> Iterator[PLMEntity]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))