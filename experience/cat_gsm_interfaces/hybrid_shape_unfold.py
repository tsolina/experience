from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeUnfold(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeUnfold
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_unfold = com

    def direction_to_unfold(self, value: Reference = None) -> Union['HybridShapeUnfold', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_unfold.DirectionToUnfold = value._com
            return self
        return Reference(self.hybrid_shape_unfold.DirectionToUnfold)

    def edge_to_tear_positioning_orientation(self, value: int = None) -> Union['HybridShapeUnfold', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_unfold.EdgeToTearPositioningOrientation = value
            return self
        return self.hybrid_shape_unfold.EdgeToTearPositioningOrientation

    def origin_to_unfold(self, value: Reference = None) -> Union['HybridShapeUnfold', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_unfold.OriginToUnfold = value._com
            return self
        return Reference(self.hybrid_shape_unfold.OriginToUnfold)

    def surface_to_unfold(self, value: Reference = None) -> Union['HybridShapeUnfold', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_unfold.SurfaceToUnfold = value._com
            return self
        return Reference(self.hybrid_shape_unfold.SurfaceToUnfold)

    def surface_type(self, value: int = None) -> Union['HybridShapeUnfold', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_unfold.SurfaceType = value
            return self
        return self.hybrid_shape_unfold.SurfaceType

    def target_orientation_mode(self, value: int = None) -> Union['HybridShapeUnfold', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_unfold.TargetOrientationMode = value
            return self
        return self.hybrid_shape_unfold.TargetOrientationMode

    def target_plane(self, value: Reference = None) -> Union['HybridShapeUnfold', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_unfold.TargetPlane = value._com
            return self
        return Reference(self.hybrid_shape_unfold.TargetPlane)

    def add_edge_to_tear(self, i_element: Reference) -> 'HybridShapeUnfold':
        self.hybrid_shape_unfold.AddEdgeToTear(i_element._com)
        return self

    def add_element_to_transfer(self, i_element: Reference, i_type_of_transfer: int) -> 'HybridShapeUnfold':
        self.hybrid_shape_unfold.AddElementToTransfer(i_element._com, i_type_of_transfer)
        return self

    def get_edge_to_tear(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_unfold.GetEdgeToTear(i_rank))

    def get_element_to_transfer(self, i_rank: int) -> tuple[Reference, int]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com, i_rank], ("HybridShapeUnfold","GetElementToTransfer","Long"), ("Reference", "Long"))

    def remove_edge_to_tear(self, i_rank: int) -> 'HybridShapeUnfold':
        self.hybrid_shape_unfold.RemoveEdgeToTear(i_rank)
        return self

    def remove_element_to_transfer(self, i_rank: int) -> 'HybridShapeUnfold':
        self.hybrid_shape_unfold.RemoveElementToTransfer(i_rank)
        return self

    def replace_elements_to_transfer(self, i_rank: int, i_element: Reference) -> 'HybridShapeUnfold':
        self.hybrid_shape_unfold.ReplaceElementsToTransfer(i_rank, i_element._com)
        return self

    def __repr__(self):
        return f'HybridShapeUnfold(name="{self.name}")'