from typing import Union, Optional, TYPE_CHECKING

from experience.cat_sketcher_interfaces import Curve2D

if TYPE_CHECKING:
    from experience.cat_sketcher_interfaces import Point2D

class Circle2D(Curve2D):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SketcherInterfaces.GeometricElement
                |                         SketcherInterfaces.Geometry2D
                |                             SketcherInterfaces.Curve2D
                |                                 Circle2D
    """

    def __init__(self, com):
        super().__init__(com)
        self.circle_2d = com

    def center_point(self, value: 'Point2D' = None) -> 'Point2D':
        if value is not None:
            self.circle_2d.CenterPoint = value._com
            return self
        from experience.cat_sketcher_interfaces import Point2D
        return Point2D(self.circle_2d.CenterPoint)

    def radius(self) -> float:
        return self.circle_2d.Radius

    def get_center(self) -> tuple[float, float]:
        return self._get_safe_array(self.circle_2d, "GetCenter", 1)

    def set_data(self, i_center_x: float, i_center_y: float, i_radius: float) -> 'Circle2D':
        self.circle_2d.SetData(i_center_x, i_center_y, i_radius)
        return self

    def __repr__(self):
        return f'Circle2D(name="{self.name()}")'