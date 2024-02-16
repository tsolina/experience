from typing import Union, Optional, TYPE_CHECKING

from experience.cat_sketcher_interfaces import Geometry2D

if TYPE_CHECKING:
    from experience.cat_sketcher_interfaces import Line2D, Point2D

class Axis2D(Geometry2D):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SketcherInterfaces.GeometricElement
                |                         SketcherInterfaces.Geometry2D
                |                             Axis2D
    """

    def __init__(self, com):
        super().__init__(com)
        self.axis_2d = com

    def horizontal_reference(self) -> 'Line2D':
        from experience.cat_sketcher_interfaces import Line2D
        return Line2D(self.axis_2d.HorizontalReference)

    def origin(self) -> 'Point2D':
        from experience.cat_sketcher_interfaces import Point2D
        return Point2D(self.axis_2d.Origin)

    def vertical_reference(self) -> 'Line2D':
        from experience.cat_sketcher_interfaces import Line2D
        return Line2D(self.axis_2d.VerticalReference)

    def __repr__(self):
        return f'Axis2D(name="{self.name()}")'