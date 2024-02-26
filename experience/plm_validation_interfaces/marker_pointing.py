from typing import TYPE_CHECKING, Union
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.types import cat_variant

class MarkerPointing(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MarkerPointing
    """

    def __init__(self, com):
        super().__init__(com)
        self.marker_pointing = com

    def add_object(self, i_object: AnyObject) -> 'MarkerPointing':
        self.marker_pointing.AddObject(i_object._com)
        return self
    
    def count_object(self) -> int:
        return self.marker_pointing.CountObject()
    
    def get_pointing_positions(self, i_index: 'cat_variant') -> tuple:
        return self.marker_pointing.GetPointingPositions(i_index)
    
    def item_object(self, i_index: 'cat_variant') -> AnyObject:
        return AnyObject(self.marker_pointing.ItemObject(i_index))
    
    def remove_object(self, i_index: 'cat_variant') -> 'MarkerPointing':
        self.marker_pointing.RemoveObject(i_index)
        return self
    
    def set_pointing_positions(self, i_index: 'cat_variant', i_coordinates: tuple) -> 'MarkerPointing':
        self.marker_pointing.SetPointingPositions(i_index, i_coordinates)
        return self