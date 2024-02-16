from typing import Union, Optional, TYPE_CHECKING

from experience.cat_sketcher_interfaces import Geometry2D

if TYPE_CHECKING:
    from experience.cat_sketcher_interfaces import Point2D

class Curve2D(Geometry2D):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SketcherInterfaces.GeometricElement
                |                         SketcherInterfaces.Geometry2D
                |                             Curve2D
    """

    def __init__(self, com):
        super().__init__(com)
        self.curve_2d = com

    def continuity(self) -> int:
        return self.curve_2d.Continuity

    def end_point(self, value: 'Point2D' = None) -> Union['Curve2D', 'Point2D']:
        if value is not None:
            self.curve_2d.EndPoint = value._com
            return self
        from experience.cat_sketcher_interfaces import Point2D
        return Point2D(self.curve_2d.EndPoint)

    def period(self) -> float:
        return self.curve_2d.Period

    def start_point(self, value: 'Point2D' = None) -> Union['Curve2D', 'Point2D']:
        if value is not None:
            self.curve_2d.StartPoint = value._com
            return self
        from experience.cat_sketcher_interfaces import Point2D
        return Point2D(self.curve_2d.StartPoint)

    def get_curvature(self, i_param: float) -> tuple[float, float, float]:
        return self._get_safe_array(self.curve_2d, "GetCurvature", 2, i_param)

    def get_derivatives(self, i_param: float) -> tuple[float, float, float]:
        return self._get_safe_array(self.curve_2d, "GetDerivatives", 2, i_param)   

    def get_end_points(self) -> tuple[float, float, float, float]:
        return self._get_safe_array(self.curve_2d, "GetEndPoints", 3) 

    def get_length_at_param(self, i_from_param: float, i_to_param: float) -> float:
        return self.curve_2d.GetLengthAtParam(i_from_param, i_to_param)

    def get_param_at_length(self, i_from_param: float, i_length: float) -> float:
        return self.curve_2d.GetParamAtLength(i_from_param, i_length)

    def get_param_extents(self) -> tuple[float, float]:
        return self._get_safe_array(self.curve_2d, "GetParamExtents", 1) 

    def get_point_at_param(self, i_param: float) -> tuple: #, o_point: cat_variant
        return self._get_safe_array(self.curve_2d, "GetPointAtParam", 1, i_param)

    def get_range_box(self) -> tuple[float, float, float, float]:
        return self._get_safe_array(self.curve_2d, "GetRangeBox", 3) 

    def get_tangent(self, i_param: float) -> tuple[float, float]:
        return self._get_safe_array(self.curve_2d, "GetTangent", 1) 

    def is_periodic(self) -> bool:
        return self.curve_2d.IsPeriodic()

    def __repr__(self):
        return f'Curve2D(name="{self.name()}")'