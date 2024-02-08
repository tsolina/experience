from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import GeometricElements

from .geometry_2d import Geometry2D
from .point_2d import Point2D
from .hyperbola_2d import Hyperbola2D
from .control_point_2d import ControlPoint2D
from .ellipse_2d import Ellipse2D
from .circle_2d import Circle2D
from .parabola_2d import Parabola2D

from .line_2d import Line2D
from .spline_2d import Spline2D

from experience.system import AnyObject


class Factory2D(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Factory2D
    """

    def __init__(self, com):
        super().__init__(com)
        self.factory_2d = com

    def create_circle(self, i_center_x: float, i_center_y: float, i_radius: float, i_start_param: float, i_end_param: float) -> Circle2D:
        return Circle2D(self.factory_2d.CreateCircle(i_center_x, i_center_y, i_radius, i_start_param, i_end_param))

    def create_closed_circle(self, i_center_x: float, i_center_y: float, i_radius: float) -> Circle2D:
        return Circle2D(self.factory_2d.CreateClosedCircle(i_center_x, i_center_y, i_radius))

    def create_closed_ellipse(self, i_center_x: float, i_center_y: float, i_major_x: float, i_major_y: float, i_major_radius: float, i_minor_radius: float) -> Ellipse2D:
        return Ellipse2D( self.factory_2d.CreateClosedEllipse(i_center_x, i_center_y, i_major_x, i_major_y, i_major_radius, i_minor_radius))

    def create_control_point(self, i_x: float, i_y: float) -> ControlPoint2D:
        return ControlPoint2D(self.factory_2d.CreateControlPoint(i_x, i_y))

    def create_ellipse(self, i_center_x: float, i_center_y: float, i_major_x: float, i_major_y: float, i_major_radius: float, i_minor_radius: float, i_start_param: float, i_end_param: float) -> Ellipse2D:
        return Ellipse2D(self.factory_2d.CreateEllipse(i_center_x, i_center_y, i_major_x, i_major_y, i_major_radius, i_minor_radius, i_start_param, i_end_param))

    def create_hyperbola(self, i_center_x: float, i_center_y: float, i_axis_x: float, i_axis_y: float, i_major_radius: float, i_minor_radius: float) -> Hyperbola2D:
        return Hyperbola2D(self.factory_2d.CreateHyperbola(i_center_x, i_center_y, i_axis_x, i_axis_y, i_major_radius, i_minor_radius))

    def create_intersection(self, i_geometry: Reference) -> Geometry2D:
        return Geometry2D(self.factory_2d.CreateIntersection(i_geometry._com))

    def create_intersections(self, i_geometry: Reference) -> GeometricElements:
        return GeometricElements(self.factory_2d.CreateIntersections(i_geometry._com))

    def create_line(self, i_x1: float, i_y1: float, i_x2: float, i_y2: float) -> Line2D:
        return Line2D(self.factory_2d.CreateLine(i_x1, i_y1, i_x2, i_y2))

    def create_line_from_vector(self, i_x1: float, i_y1: float, i_ux: float, i_uy: float) -> Line2D:
        return Line2D(self.factory_2d.CreateLineFromVector(i_x1, i_y1, i_ux, i_uy))

    def create_parabola(self, i_center_x: float, i_center_y: float, i_axis_x: float, i_axis_y: float, i_focal_distance: float) -> Parabola2D:
        return Parabola2D(self.factory_2d.CreateParabola(i_center_x, i_center_y, i_axis_x, i_axis_y, i_focal_distance))

    def create_point(self, i_x: float, i_y: float) -> Point2D:
        return Point2D(self.factory_2d.CreatePoint(i_x, i_y))

    def create_projection(self, i_geometry: Reference) -> Geometry2D:
        return Geometry2D(self.factory_2d.CreateProjection(i_geometry._com))

    def create_projections(self, i_geometry: Reference) -> GeometricElements:
        return GeometricElements(self.factory_2d.CreateProjections(i_geometry._com))

    def create_spline(self, i_poles: tuple) -> Spline2D:
        return Spline2D(self.factory_2d.CreateSpline(i_poles))

    def __repr__(self):
        return f'Factory2D(name="{self.name}")'