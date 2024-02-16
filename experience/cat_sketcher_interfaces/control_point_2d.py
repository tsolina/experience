from experience.cat_sketcher_interfaces import Point2D

class ControlPoint2D(Point2D):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SketcherInterfaces.GeometricElement
                |                         SketcherInterfaces.Geometry2D
                |                             SketcherInterfaces.Point2D
                |                                 ControlPoint2D
    """

    def __init__(self, com):
        super().__init__(com)
        self.control_point_2d = com

    def curvature(self, value: float = None) -> float:
        if value is not None:
            self.control_point_2d.Curvature = value
            return self
        return self.control_point_2d.Curvature

    def get_tangent(self) -> tuple[float, float]:
        return self._get_safe_array(self.control_point_2d, "GetTangent", 1)

    def set_tangent(self, i_tangent_x: float, i_tangent_y: float) -> 'ControlPoint2D':
        self.control_point_2d.SetTangent(i_tangent_x, i_tangent_y)
        return self

    def unset_curvature(self) -> 'ControlPoint2D':
        self.control_point_2d.UnsetCurvature()
        return self

    def unset_tangent(self) -> 'ControlPoint2D':
        self.control_point_2d.UnsetTangent()
        return self

    def __repr__(self):
        return f'ControlPoint2D(name="{self.name()}")'