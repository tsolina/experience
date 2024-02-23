from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import Shape

class SurfaceBasedShape(Shape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         SurfaceBasedShape
    """

    def __init__(self, com):
        super().__init__(com)
        self.surface_based_shape = com

    def surface(self, value: Reference = None) -> Union['SurfaceBasedShape', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.surface_based_shape.Surface = value._com
            return self
        return Reference(self.surface_based_shape.Surface)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'