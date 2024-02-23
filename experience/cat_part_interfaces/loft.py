from typing import TYPE_CHECKING
from experience.mecmod_interfaces.shape import Shape

if TYPE_CHECKING:
    from experience.mecmod_interfaces import HybridShape

class Loft(Shape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         Loft
    """

    def __init__(self, com):
        super().__init__(com)
        self.loft = com

    def hybrid_shape(self) -> HybridShape:
        from experience.mecmod_interfaces import HybridShape
        return HybridShape(self.loft.HybridShape)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'