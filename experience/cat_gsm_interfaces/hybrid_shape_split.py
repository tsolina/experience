from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeSplit(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeSplit
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_split = com

    def automatic_extrapolation_mode(self, value: bool = None) -> Union['HybridShapeSplit', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_split.AutomaticExtrapolationMode = value
            return self
        return self.hybrid_shape_split.AutomaticExtrapolationMode

    def both_sides_mode(self, value: bool = None) -> Union['HybridShapeSplit', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_split.BothSidesMode = value
            return self
        return self.hybrid_shape_split.BothSidesMode

    def cutting_elem(self, value: Reference = None) -> Union['HybridShapeSplit', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_split.CuttingElem = value._com
            return self
        return Reference(self.hybrid_shape_split.CuttingElem)

    def elem_to_cut(self, value: Reference = None) -> Union['HybridShapeSplit', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_split.ElemToCut = value._com
            return self
        return Reference(self.hybrid_shape_split.ElemToCut)

    def extrapolation_type(self, value: int = None) -> Union['HybridShapeSplit', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_split.ExtrapolationType = value
            return self
        return self.hybrid_shape_split.ExtrapolationType

    def intersection_computation(self, value: bool = None) -> Union['HybridShapeSplit', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_split.IntersectionComputation = value
            return self
        return self.hybrid_shape_split.IntersectionComputation

    def orientation(self, value: int = None) -> Union['HybridShapeSplit', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_split.Orientation = value
            return self
        return self.hybrid_shape_split.Orientation

    def support(self, value: Reference = None) -> Union['HybridShapeSplit', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_split.Support = value._com
            return self
        return Reference(self.hybrid_shape_split.Support)

    def volume_result(self, value: int = None) -> Union['HybridShapeSplit', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_split.VolumeResult = value
            return self
        return self.hybrid_shape_split.VolumeResult

    def add_cutting_elem(self, i_elem: Reference, i_orientation: int) -> 'HybridShapeSplit':
        self.hybrid_shape_split.AddCuttingElem(i_elem._com, i_orientation)
        return self

    def add_element_to_keep(self, i_element: Reference) -> 'HybridShapeSplit':
        self.hybrid_shape_split.AddElementToKeep(i_element._com)
        return self

    def add_element_to_remove(self, i_element: Reference) -> 'HybridShapeSplit':
        self.hybrid_shape_split.AddElementToRemove(i_element._com)
        return self

    def get_cutting_elem(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_split.GetCuttingElem(i_rank))

    def get_intersection(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_split.GetIntersection(i_rank))

    def get_kept_elem(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_split.GetKeptElem(i_rank))

    def get_nb_cutting_elem(self) -> int:
        return self.hybrid_shape_split.GetNbCuttingElem()

    def get_nb_elements_to_keep(self) -> int:
        return self.hybrid_shape_split.GetNbElementsToKeep()

    def get_nb_elements_to_remove(self) -> int:
        return self.hybrid_shape_split.GetNbElementsToRemove()

    def get_orientation(self, i_rank: int) -> int:
        return self.hybrid_shape_split.GetOrientation(i_rank)

    def get_other_side(self) -> Reference:
        return Reference(self.hybrid_shape_split.GetOtherSide())

    def get_removed_elem(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_split.GetRemovedElem(i_rank))

    def invert_orientation(self) -> 'HybridShapeSplit':
        self.hybrid_shape_split.InvertOrientation()
        return self

    def remove_cutting_elem(self, i_elem: Reference) -> 'HybridShapeSplit':
        self.hybrid_shape_split.RemoveCuttingElem(i_elem._com)
        return self

    def remove_element_to_keep(self, i_rank: int) -> 'HybridShapeSplit':
        self.hybrid_shape_split.RemoveElementToKeep(i_rank)
        return self

    def remove_element_to_remove(self, i_rank: int) -> 'HybridShapeSplit':
        self.hybrid_shape_split.RemoveElementToRemove(i_rank)
        return self

    def set_orientation(self, i_rank: int, i_orientation: int) -> 'HybridShapeSplit':
        self.hybrid_shape_split.SetOrientation(i_rank, i_orientation)
        return self

    def __repr__(self):
        return f'HybridShapeSplit(name="{self.name}")'