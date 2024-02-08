from typing import TypeVar, Type, Optional
from experience.inf_interfaces import Reference
from experience.system import AnyObject

T = TypeVar('T')

class SelectedElement(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.selected_element = com

    def leaf_product(self) -> AnyObject:
        return AnyObject(self.selected_element.LeafProduct)

    def reference(self) -> Reference:
        return Reference(self.selected_element.Reference)

    def type(self) -> str:
        return self.selected_element.Type

    # def value(self) -> AnyObject:
    #     return AnyObject(self.selected_element.Value)
    
    def value(self, value: Optional[Type[T]]) -> T:
        if value is not None:
            return value(self.selected_element.Value)
        return AnyObject(self.selected_element.Value)

# TODO: fix the length for drawing document
    def get_coordinates(self) -> tuple:
        # vba_function_name = 'get_coordinates'
        # vba_code = """
        # Public Function get_coordinates(selected_element)
        #     Dim ioPoint (2)
        #     selected_element.GetCoordinates ioPoint
        #     get_coordinates = ioPoint
        # End Function
        # """
        #
        # system_service = self.application.system_service
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])
        return self._get_safe_array(self.selected_element, "GetCoordinates", 2)

    def __repr__(self):
        return f'SelectedElement(name="{self.name}")'
