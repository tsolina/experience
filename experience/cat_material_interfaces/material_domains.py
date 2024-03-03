from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from experience.cat_material_interfaces import MaterialDomain
from experience.plm_modeler_base_interfaces import PLMEntities

if TYPE_CHECKING:
    from experience.types.general import cat_variant

class MaterialDomains(PLMEntities):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     PLMModelerBaseIDLItf.PLMEntities
                |                         MaterialDomains
    """

    def __init__(self, com):
        super().__init__(com, child=MaterialDomain)
        self.material_domains = com

    def add(self, i_user_discipline: str) -> MaterialDomain:
        return self.material_domains.Add(i_user_discipline)
    
    def get_item_by_discipline(self, i_user_discipline: tuple) -> Collection:
        return Collection(self.material_domains.GetItemByDiscipline(i_user_discipline))

    def __getitem__(self, n: int) -> MaterialDomain:
        if (n + 1) > self.count():
            raise StopIteration

        return MaterialDomain(self.material_domains.item(n + 1))

    def __iter__(self) -> Iterator[MaterialDomain]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))