from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces.shape import Shape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import RealParam

class Scaling2(Shape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         Scaling2
    """

    def __init__(self, com):
        super().__init__(com)
        self.scaling2 = com

    def center(self, value: Reference = None) -> Union['Scaling2', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.scaling2.Center = value._com
            return self
        return Reference(self.scaling2.Center)

    def ratio(self) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.scaling2.Ratio)

    def ration_value(self, value: float = None) -> Union['Scaling2', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.scaling2.RatioValue = value
            return self
        return Reference(self.scaling2.RatioValue)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'