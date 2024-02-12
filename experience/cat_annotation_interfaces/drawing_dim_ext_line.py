from typing import Union
from experience.system import AnyObject

class DrawingDimExtLine(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingDimExtLine
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_dim_ext_line = com

    def color(self, value: int = None) -> Union['DrawingDimExtLine', int]:
        if value is not None:
            self.drawing_dim_ext_line.Color = value
            return self
        return self.drawing_dim_ext_line.Color

    def ext_line_slant(self, value: float = None) -> Union['DrawingDimExtLine', float]:
        if value is not None:
            self.drawing_dim_ext_line.ExtLineSlant = value
            return self
        return self.drawing_dim_ext_line.ExtLineSlant

    def ext_line_type(self) -> int:
        return self.drawing_dim_ext_line.ExtLineType

    def thickness(self, value: float = None) -> Union['DrawingDimExtLine', float]:
        if value is not None:
            self.drawing_dim_ext_line.Thickness = value
            return self
        return self.drawing_dim_ext_line.Thickness

    def add_interrupt(self, i_index: int, i_two_points: tuple) -> 'DrawingDimExtLine':
        self.drawing_dim_ext_line.AddInterrupt(i_index, i_two_points)
        return self

    def get_funnel(self, i_index: int) -> tuple[int, float, float, float]:
        return self._get_multi([self.drawing_dim_ext_line, i_index],("DrawingDimExtLine", "GetFunnel", "Long"),("Long", "Double", "Double", "Double"))

    def get_gap(self, i_index: int) -> float:
        return self.drawing_dim_ext_line.GetGap(i_index)

    def get_geom_info(self, i_index: int) -> tuple[float, float, float, float, float, float]:
        return self._get_safe_array(self.drawing_dim_ext_line, "GetGeomInfo", 5, i_index)

    def get_interrupt(self, i_index: int) -> int:
        return self.drawing_dim_ext_line.GetInterrupt(i_index)

    def get_overrun(self, i_index: int) -> float:
        return self.drawing_dim_ext_line.GetOverrun(i_index)

    def get_visibility(self, i_index: int) -> int:
        return self.drawing_dim_ext_line.GetVisibility(i_index)

    def remove_interrupt(self, i_index: int) -> 'DrawingDimExtLine':
        self.drawing_dim_ext_line.RemoveInterrupt(i_index)
        return self

    def set_funnel(self, i_index: int, i_mode: int, i_angle: float, i_height: float, i_width: float) -> 'DrawingDimExtLine':
        self.drawing_dim_ext_line.SetFunnel(i_index, i_mode, i_angle, i_height, i_width)
        return self

    def set_gap(self, i_index: int, i_gap: float) -> 'DrawingDimExtLine':
        self.drawing_dim_ext_line.SetGap(i_index, i_gap)
        return self

    def set_overrun(self, i_index: int, i_overrun: float) -> 'DrawingDimExtLine':
        self.drawing_dim_ext_line.SetOverrun(i_index, i_overrun)
        return self

    def set_visibility(self, i_index: int, i_extline_visibility: int) -> 'DrawingDimExtLine':
        self.drawing_dim_ext_line.SetVisibility(i_index, i_extline_visibility)
        return self

    def __repr__(self):
        return f'DrawingDimExtLine(name="{self.name()}")'
