from typing import TypeVar, Type, Optional, TYPE_CHECKING
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.inf_interfaces import Reference


T = TypeVar('T')

class SelectedElement(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.selected_element = com

    def leaf_product(self) -> AnyObject:
        return AnyObject(self.selected_element.LeafProduct)

    def reference(self) -> 'Reference':
        from experience.inf_interfaces import Reference
        return Reference(self.selected_element.Reference)

    def type(self) -> str:
        return self.selected_element.Type

    def value(self, value: Optional[Type[T]] = None) -> T:
        if value is not None:
            return value(self.selected_element.Value)
        return AnyObject(self.selected_element.Value)

# TODO: fix the length for drawing document
    def get_coordinates(self) -> tuple:
        return self._get_safe_array(self.selected_element, "GetCoordinates", 2)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'