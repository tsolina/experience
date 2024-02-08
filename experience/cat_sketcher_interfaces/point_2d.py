from experience.cat_sketcher_interfaces import Geometry2D

class Point2D(Geometry2D):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SketcherInterfaces.GeometricElement
                |                         SketcherInterfaces.Geometry2D
                |                             Point2D
    """

    def __init__(self, com):
        super().__init__(com)
        self.point_2d = com

    def get_coordinates(self) -> tuple[float, float]:
        return self._get_safe_array(self.point_2d, "GetCoordinates", 1)

    def set_data(self, i_x: float, i_y: float) -> 'Point2D':
        self.point_2d.SetData(i_x, i_y)
        return self

    def __repr__(self):
        return f'Point2D(name="{self.name}")'