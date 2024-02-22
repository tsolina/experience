from experience.cat_sketcher_interfaces import Curve2D

class Hyperbola2D(Curve2D):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SketcherInterfaces.GeometricElement
                |                         SketcherInterfaces.Geometry2D
                |                             SketcherInterfaces.Curve2D
                |                                 Hyperbola2D
    """

    def __init__(self, com):
        super().__init__(com)
        self.hyperbola_2d = com

    def imaginary_radius(self) -> float:
        return self.hyperbola_2d.ImaginaryRadius
    
    def radius(self) -> float:
        return self.hyperbola_2d.Radius

    def get_axis(self) -> tuple[float, float]:
        return self._get_safe_array(self.hyperbola_2d, "GetAxis", 1)

    def get_center(self) -> tuple[float, float]:
        return self._get_safe_array(self.hyperbola_2d, "GetCenter", 1)

    def set_data(self, i_center_x: float, i_center_y: float, i_axis_x: float, i_axis_y: float, i_major_radius: float, i_minor_radius: float) -> 'Hyperbola2D':
        self.hyperbola_2d.SetData(i_center_x, i_center_y, i_axis_x, i_axis_y, i_major_radius, i_minor_radius)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'