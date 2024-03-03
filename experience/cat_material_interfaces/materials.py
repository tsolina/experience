from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from experience.cat_material_interfaces import Material

if TYPE_CHECKING:
    from experience.types.general import cat_variant

class Materials(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Materials
    """

    def __init__(self, com):
        super().__init__(com, child=Material)
        self.materials = com

    def add(self, i_material: Material) -> 'Materials':
        self.materials.Add(i_material)
        return self

    def item(self, i_index: 'cat_variant') -> 'Material':
        return Material(self.materials.Item(i_index))
    
    def remove(self, i_material: Material) -> 'Materials':
        self.materials.Remove(i_material)
        return self

    def __getitem__(self, n: int) -> Material:
        if (n + 1) > self.count():
            raise StopIteration

        return Material(self.materials.item(n + 1))

    def __iter__(self) -> Iterator[Material]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'