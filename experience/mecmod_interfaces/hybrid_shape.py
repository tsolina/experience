from typing import TYPE_CHECKING

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.mecmod_interfaces import HybridBody


class HybridShape(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     HybridShape
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape = com

    def thickness(self) -> 'HybridShape':
        return HybridShape(self.hybrid_shape.Thickness)

    def append_hybrid_shape(self, i_hybrid_shape: 'HybridShape') -> 'HybridShape':
        self.hybrid_shape.AppendHybridShape(i_hybrid_shape._com)
        return self

    def compute(self) -> 'HybridShape':
        self.hybrid_shape.Compute()
        return self
    
    def append_to(self, i_set: 'HybridBody') -> 'HybridShape':
        i_set.append_hybrid_shape(self)
        return self

    def __repr__(self):
        return f'HybridShape(name="{self.name}")'