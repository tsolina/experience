from typing import Union, Optional, TYPE_CHECKING

from experience.cat_sketcher_interfaces import Curve2D

if TYPE_CHECKING:
    from experience.cat_sketcher_interfaces import Point2D

class Ellipse2D(Curve2D):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SketcherInterfaces.GeometricElement
                |                         SketcherInterfaces.Geometry2D
                |                             SketcherInterfaces.Curve2D
                |                                 Ellipse2D
    """

    def __init__(self, com):
        super().__init__(com)
        self.ellipse_2d = com

    def center_point(self, value: 'Point2D' = None) -> Union['Ellipse2D', 'Point2D']:
        if value is not None:
            self.ellipse_2d.CenterPoint = value._com
            return self
        return Point2D(self.ellipse_2d.CenterPoint)

    def major_radius(self) -> float:
        return self.ellipse_2d.MajorRadius

    def minor_radius(self) -> float:
        return self.ellipse_2d.MinorRadius

    def get_center(self) -> tuple[float, float]:
        return self._get_safe_array(self.ellipse_2d, "GetCenter", 1)

    def get_major_axis(self) -> tuple[float, float]:
        return self._get_safe_array(self.ellipse_2d, "GetMajorAxis", 1)

    def get_minor_axis(self) -> tuple[float, float]:
        return self._get_safe_array(self.ellipse_2d, "GetMinorAxis", 1)

    def set_data(self, i_center_x: float, i_center_y: float, i_major_x: float, i_major_y: float, i_major_radius: float, i_minor_radius: float) -> 'Ellipse2D':
        self.ellipse_2d.SetData(i_center_x, i_center_y, i_major_x, i_major_y, i_major_radius, i_minor_radius)
        return self

    def __repr__(self):
        return f'Ellipse2D(name="{self.name}")'