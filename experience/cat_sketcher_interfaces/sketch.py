from typing import Union, Optional, TYPE_CHECKING

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.mecmod_interfaces import Constraints, GeometricElements
    from experience.cat_sketcher_interfaces import Axis2D, Factory2D, Line2D

class Sketch(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Sketch
    """

    def __init__(self, com):
        super().__init__(com)
        self.sketch = com

    def absolute_axis(self) -> 'Axis2D':
        from experience.cat_sketcher_interfaces import Axis2D
        return Axis2D(self.sketch.AbsoluteAxis)

    def center_line(self, value: 'Line2D' = None) -> Union['Sketch', 'Line2D']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.sketch.CenterLine = value._com
            return self
        from experience.cat_sketcher_interfaces import Line2D
        return Line2D(self.sketch.CenterLine)

    def constraints(self) -> 'Constraints':
        from experience.mecmod_interfaces import Constraints
        return Constraints(self.sketch.Constraints)

    def factory_2d(self) -> 'Factory2D':
        from experience.cat_sketcher_interfaces import Factory2D
        return Factory2D(self.sketch.Factory2D)

    def geometric_elements(self) -> 'GeometricElements':
        from experience.mecmod_interfaces import GeometricElements
        return GeometricElements(self.sketch.GeometricElements)

    def close_edition(self) -> 'Sketch':
        self.sketch.CloseEdition()
        return self

    def evaluate(self) -> 'Sketch':
        self.sketch.Evaluate()
        return self

    def get_absolute_axis_data(self) -> tuple[float, float, float, float, float, float, float, float, float]:
        return self._get_safe_array(self._com, "GetAbsoluteAxisData", 8)

    def inverse_orientation(self) -> 'Sketch':
        self.sketch.InverseOrientation()
        return self

    def open_edition(self) -> 'Factory2D':
        from experience.cat_sketcher_interfaces import Factory2D
        return Factory2D(self.sketch.OpenEdition())

    def set_absolute_axis_data(self, i_axis_data: tuple) -> 'Sketch':
        self.sketch.SetAbsoluteAxisData(i_axis_data)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'