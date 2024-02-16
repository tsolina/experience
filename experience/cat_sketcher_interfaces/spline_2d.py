from typing import TYPE_CHECKING

from experience.cat_sketcher_interfaces import Curve2D

if TYPE_CHECKING:
    from experience.cat_sketcher_interfaces import Point2D

class Spline2D(Curve2D):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SketcherInterfaces.GeometricElement
                |                         SketcherInterfaces.Geometry2D
                |                             SketcherInterfaces.Curve2D
                |                                 Spline2D
    """

    def __init__(self, com):
        super().__init__(com)
        self.spline_2d = com

    def get_control_points(self) -> tuple:
        return self._get_safe_array(self.spline_2d, "GetControlPoints", self.get_number_of_control_points() - 1)

    def get_number_of_control_points(self) -> int:
        return int(self.spline_2d.GetNumberOfControlPoints())

    def insert_control_point_after(self, i_ctrl_point: 'Point2D', i_position: int) -> 'Spline2D':
        self.spline_2d.InsertControlPointAfter(i_ctrl_point._com, i_position)
        return self

    def __repr__(self):
        return f'Spline2D(name="{self.name()}")'