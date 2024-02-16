from experience.cat_sketcher_interfaces import Curve2D

class Line2D(Curve2D):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SketcherInterfaces.GeometricElement
                |                         SketcherInterfaces.Geometry2D
                |                             SketcherInterfaces.Curve2D
                |                                 Line2D
    """

    def __init__(self, com):
        super().__init__(com)
        self.line_2d = com

    def get_direction(self) -> tuple[float, float]:
        return self._get_safe_array(self.line_2d, "GetDirection", 1)

    def get_origin(self) -> tuple[float, float]:
        return self._get_safe_array(self.line_2d, "GetOrigin", 1)

    def set_data(self, i_x: float, i_y: float, i_x_direction: float, i_y_direction: float) -> 'Line2D':
        self.line_2d.SetData(i_x, i_y, i_x_direction, i_y_direction)
        return self

    def __repr__(self):
        return f'Line2D(name="{self.name()}")'