from typing import Iterator, TYPE_CHECKING

from experience.system import Collection, AnyObject

if TYPE_CHECKING:
    from experience.types.general import cat_variant

class MaterialBehaviorOptions(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     MaterialBehaviorOptions
    """

    def __init__(self, com):
        super().__init__(com, child=AnyObject)
        self.material_behavior_options = com

    def add(self, i_material_behavior_option: AnyObject) -> int:
        return self.material_behavior_options.Add(i_material_behavior_option)
    
    def get_option(self, i_index: 'cat_variant') -> 'AnyObject':
        return AnyObject(self.material_behavior_options.GetOption(i_index))
    
    def remove(self, i_index: 'cat_variant') -> 'MaterialBehaviorOptions':
        self.material_behavior_options.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> AnyObject:
        if (n + 1) > self.count():
            raise StopIteration

        return AnyObject(self.material_behavior_options.item(n + 1))

    def __iter__(self) -> Iterator[AnyObject]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))