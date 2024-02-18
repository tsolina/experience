from typing import TYPE_CHECKING

from experience.system import AnyObject
from experience.types import cat_variant

from experience.drafting_interfaces.drafting_types import *

class DrawingAreaFill(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingAreaFill
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_area_fill = com

    def area_fill_type(self) -> CatAreaFillType:
        return CatAreaFillType.item(self.drawing_area_fill.AreaFillType)

    def display_at_true_depth(self, value: bool = None) -> bool:
        if value is not None:
            self.drawing_area_fill.DisplayAtTrueDepth = value
            return self
        return self.drawing_area_fill.DisplayAtTrueDepth

    def get_characteristics(self) -> tuple:
        return self.drawing_area_fill.GetCharacteristics()

    def get_points(self) -> tuple[tuple, tuple]:
        return self.drawing_area_fill.GetPoints()

    def isolate(self) -> 'DrawingAreaFill':
        self.drawing_area_fill.Isolate()
        return self

    def modify_points(self, i_number_of_points_per_contour: list, i_points_coordinates: list) -> 'DrawingAreaFill':
        self.drawing_area_fill.ModifyPoints(i_number_of_points_per_contour, i_points_coordinates)
        return self

    def set_pattern(self, i_pattern_name_from_standard: str) -> 'DrawingAreaFill':
        self.drawing_area_fill.SetPattern(i_pattern_name_from_standard)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
