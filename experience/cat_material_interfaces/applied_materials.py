from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from experience.cat_material_interfaces import AppliedMaterial

if TYPE_CHECKING:
    from experience.types.general import cat_variant

class AppliedMaterials(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AppliedMaterials
    """

    def __init__(self, com):
        super().__init__(com, child=AppliedMaterial)
        self.applied_materials = com

    def add(self, i_applied_material: AppliedMaterial) -> 'AppliedMaterials':
        self.applied_materials.Add(i_applied_material)
        return self

    def item(self, i_index: 'cat_variant') -> 'AppliedMaterial':
        return AppliedMaterial(self.applied_materials.Item(i_index))
    
    def remove(self, i_index: 'cat_variant') -> 'AppliedMaterials':
        self.applied_materials.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> AppliedMaterial:
        if (n + 1) > self.count():
            raise StopIteration

        return AppliedMaterial(self.applied_materials.item(n + 1))

    def __iter__(self) -> Iterator[AppliedMaterial]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'