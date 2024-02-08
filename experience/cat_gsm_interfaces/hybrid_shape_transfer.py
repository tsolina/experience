from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeTransfer(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeTransfer
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_transfer = com

    def element_to_transfer(self, value: Reference = None) -> Union['HybridShapeTransfer', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_transfer.ElementToTransfer = value._com
            return self
        return Reference(self.hybrid_shape_transfer.ElementToTransfer)

    def surface_to_unfold(self, value: Reference = None) -> Union['HybridShapeTransfer', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_transfer.SurfaceToUnfold = value._com
            return self
        return Reference(self.hybrid_shape_transfer.SurfaceToUnfold)

    def type_of_transfer(self, value: int = None) -> Union['HybridShapeTransfer', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_transfer.TypeOfTransfer = value
            return self
        return self.hybrid_shape_transfer.TypeOfTransfer

    def unfold_type(self, value: int = None) -> Union['HybridShapeTransfer', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_transfer.UnfoldType = value
            return self
        return self.hybrid_shape_transfer.UnfoldType

    def unfolded_surface(self, value: Reference = None) -> Union['HybridShapeTransfer', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_transfer.UnfoldedSurface = value._com
            return self
        return Reference(self.hybrid_shape_transfer.UnfoldedSurface)

    def __repr__(self):
        return f'HybridShapeTransfer(name="{self.name}")'