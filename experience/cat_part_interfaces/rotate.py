from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.cat_part_interfaces.cat_part_types import *
from experience.mecmod_interfaces import Shape


if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle
    from experience.mecmod_interfaces.hybrid_shape import HybridShape

class Rotate(Shape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         Rotate
    """

    def __init__(self, com):
        super().__init__(com)
        self.rotate = com

    def angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return self.rotate.Angle
    
    def angle_value(self, value: float = None) -> Union['Rotate', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.rotate.AngleValue = value
            return self
        return self.rotate.AngleValue
    
    def axis(self, value: Reference = None) -> Union['Rotate', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.rotate.Axis = value._com
            return self
        return self.rotate.Axis
    
    def hybrid_shape(self) -> 'HybridShape':
        from experience.mecmod_interfaces import HybridShape
        return HybridShape(self.rotate.HybridShape)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'