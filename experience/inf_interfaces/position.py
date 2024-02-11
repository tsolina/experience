from typing import TYPE_CHECKING, Type, TypeVar, Optional
from experience.inf_interfaces import Move

if TYPE_CHECKING:
    from experience.types import cat_variant

class Position(Move):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfModelInterfaces.Move
                |                         Position
    """

    def __init__(self, com):
        super().__init__(com)
        self.position = com

    def get_abs_components(self) -> tuple:
        return self._get_safe_array(self.position, "GetAbsComponents", 11)

    def get_components(self) -> tuple:
        return self._get_safe_array(self.position, "GetComponents", 11)
    
    def set_abs_components(self, i_axis_components_array: 'cat_variant') -> 'Position':
        self.position.SetAbsComponents(i_axis_components_array)
        return self
    
    def set_components(self, i_axis_components_array: 'cat_variant') -> 'Position':
        self.position.SetComponents(i_axis_components_array)
        return self
    
    def __repr__(self):
        return f'Position(name="{self.name()}")'
