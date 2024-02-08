from typing import TYPE_CHECKING

from experience.system import AnyObject
from experience.types import cat_variant

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

    def area_fill_type(self) -> int:
        return self.drawing_area_fill.AreaFillType

    def display_at_true_depth(self, value: bool = None) -> bool:
        if value is not None:
            self.drawing_area_fill.DisplayAtTrueDepth = value
            return self
        return self.drawing_area_fill.DisplayAtTrueDepth

    def get_characteristics(self, o_number_of_contour: int, o_number_of_points: int) -> tuple:
        return self.drawing_area_fill.GetCharacteristics(o_number_of_contour, o_number_of_points)

    def get_points(self, o_number_of_points_per_contour: tuple, o_points_coordinates: tuple) -> tuple:
        return self.drawing_area_fill.GetPoints(o_number_of_points_per_contour, o_points_coordinates)

    def isolate(self) -> 'DrawingAreaFill':
        self.drawing_area_fill.Isolate()
        return self

    def modify_points(self, i_number_of_points_per_contour: tuple, i_points_coordinates: tuple) -> 'DrawingAreaFill':
        self.drawing_area_fill.ModifyPoints(i_number_of_points_per_contour, i_points_coordinates)
        return self

    def set_pattern(self, i_pattern_name_from_standard: str) -> 'DrawingAreaFill':
        self.drawing_area_fill.SetPattern(i_pattern_name_from_standard)
        return self

    def __repr__(self):
        return f'DrawingAreaFill(name="{self.name}")'
