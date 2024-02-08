from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeSymmetry(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeSymmetry
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_symmetry = com

    def creation_mode(self, value: bool = None) -> Union['HybridShapeSymmetry', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_symmetry.CreationMode = value
            return self
        return self.hybrid_shape_symmetry.CreationMode

    def elem_to_symmetry(self, value: Reference = None) -> Union['HybridShapeSymmetry', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_symmetry.ElemToSymmetry = value._com
            return self
        return Reference(self.hybrid_shape_symmetry.ElemToSymmetry)

    def reference(self, value: Reference = None) -> Union['HybridShapeSymmetry', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_symmetry.Reference = value._com
            return self
        return Reference(self.hybrid_shape_symmetry.Reference)

    def volume_result(self, value: bool = None) -> Union['HybridShapeSymmetry', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_symmetry.VolumeResult = value
            return self
        return self.hybrid_shape_symmetry.VolumeResult

    def __repr__(self):
        return f'HybridShapeSymmetry(name="{self.name}")'