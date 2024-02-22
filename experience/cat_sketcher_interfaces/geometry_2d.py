from typing import Union

from experience.cat_sketcher_interfaces import GeometricElement

class Geometry2D(GeometricElement):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SketcherInterfaces.GeometricElement
                |                         Geometry2D
    """

    def __init__(self, com):
        super().__init__(com)
        self.geometry_2d = com

    def construction(self, value: bool = None) -> Union['Geometry2D', bool]:
        if value is not None:
            self.geometry_2d.Construction = value
            return self
        return self.geometry_2d.Construction

    def report_name(self, value: int = None) -> Union['Geometry2D', int]:
        if value is not None:
            self.geometry_2d.ReportName = value
            return self
        return self.geometry_2d.ReportName

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'