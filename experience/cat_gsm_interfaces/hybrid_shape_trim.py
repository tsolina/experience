from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeTrim(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeTrim
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_trim = com

    def automatic_extrapolation_mode(self, value: bool = None) -> Union['HybridShapeTrim', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_trim.AutomaticExtrapolationMode = value
            return self
        return self.hybrid_shape_trim.AutomaticExtrapolationMode

    def connex(self, value: bool = None) -> Union['HybridShapeTrim', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_trim.Connex = value
            return self
        return self.hybrid_shape_trim.Connex

    def first_elem(self, value: Reference = None) -> Union['HybridShapeTrim', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_trim.FirstElem = value._com
            return self
        return Reference(self.hybrid_shape_trim.FirstElem)

    def first_orientation(self, value: int = None) -> Union['HybridShapeTrim', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_trim.FirstOrientation = value
            return self
        return self.hybrid_shape_trim.FirstOrientation

    def intersection_computation(self, value: bool = None) -> Union['HybridShapeTrim', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_trim.IntersectionComputation = value
            return self
        return self.hybrid_shape_trim.IntersectionComputation

    def keep_all_pieces(self, value: bool = None) -> Union['HybridShapeTrim', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_trim.KeepAllPieces = value
            return self
        return self.hybrid_shape_trim.KeepAllPieces

    def manifold(self, value: bool = None) -> Union['HybridShapeTrim', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_trim.Manifold = value
            return self
        return self.hybrid_shape_trim.Manifold

    def mode(self, value: int = None) -> Union['HybridShapeTrim', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_trim.Mode = value
            return self
        return self.hybrid_shape_trim.Mode

    def second_elem(self, value: Reference = None) -> Union['HybridShapeTrim', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_trim.SecondElem = value._com
            return self
        return Reference(self.hybrid_shape_trim.SecondElem)

    def second_orientation(self, value: int = None) -> Union['HybridShapeTrim', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_trim.SecondOrientation = value
            return self
        return self.hybrid_shape_trim.SecondOrientation

    def simplify(self, value: bool = None) -> Union['HybridShapeTrim', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_trim.Simplify = value
            return self
        return self.hybrid_shape_trim.Simplify

    def support(self, value: Reference = None) -> Union['HybridShapeTrim', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_trim.Support = value._com
            return self
        return Reference(self.hybrid_shape_trim.Support)

    def add_element_to_keep(self, i_element: Reference) -> 'HybridShapeTrim':
        self.hybrid_shape_trim.AddElementToKeep(i_element._com)
        return self

    def add_element_to_remove(self, i_element: Reference) -> 'HybridShapeTrim':
        self.hybrid_shape_trim.AddElementToRemove(i_element._com)
        return self

    def add_piece_cutter(self, i_rank: int, i_cutter_elem: int, i_orientation: int) -> 'HybridShapeTrim':
        self.hybrid_shape_trim.AddPieceCutter(i_rank, i_cutter_elem, i_orientation)
        return self

    def get_elem(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_trim.GetElem(i_rank))

    def get_kept_elem(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_trim.GetKeptElem(i_rank))

    def get_nb_elem(self) -> int:
        return self.hybrid_shape_trim.GetNbElem()

    def get_nb_elements_to_keep(self) -> int:
        return self.hybrid_shape_trim.GetNbElementsToKeep()

    def get_nb_elements_to_remove(self) -> int:
        return self.hybrid_shape_trim.GetNbElementsToRemove()

    def get_next_orientation(self, i_rank: int) -> int:
        return self.hybrid_shape_trim.GetNextOrientation(i_rank)

    def get_piece_cutter(self, i_rank: int, i_cutter_index: int, o_cutter_elem_idx: int, o_orientation: int) -> tuple:
        ### need working vba example to implement this function ###
        return self.hybrid_shape_trim.GetPieceCutter(i_rank, i_cutter_index, o_cutter_elem_idx, o_orientation)

    def get_piece_discrimination_index(self, i_rank: int) -> int:
        ### need working vba example to implement this function ###
        return self.hybrid_shape_trim.GetPieceDiscriminationIndex(i_rank)

    def get_piece_nb_cutters(self, i_rank: int) -> int:
        return self.hybrid_shape_trim.GetPieceNbCutters(i_rank)

    def get_portion_to_keep(self, i_rank: int) -> int:
        return self.hybrid_shape_trim.GetPortionToKeep(i_rank)

    def get_previous_orientation(self, i_rank: int) -> int:
        return self.hybrid_shape_trim.GetPreviousOrientation(i_rank)

    def get_removed_elem(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_trim.GetRemovedElem(i_rank))

    def invert_first_orientation(self) -> None:
        return self.hybrid_shape_trim.InvertFirstOrientation()

    def invert_second_orientation(self) -> None:
        return self.hybrid_shape_trim.InvertSecondOrientation()

    def remove_element_to_keep(self, i_rank: int) -> 'HybridShapeTrim':
        self.hybrid_shape_trim.RemoveElementToKeep(i_rank)
        return self

    def remove_element_to_remove(self, i_rank: int) -> 'HybridShapeTrim':
        self.hybrid_shape_trim.RemoveElementToRemove(i_rank)
        return self

    def remove_piece_cutter(self, i_rank: int, i_cutter_index: int) -> 'HybridShapeTrim':
        self.hybrid_shape_trim.RemovePieceCutter(i_rank, i_cutter_index)
        return self

    def set_elem(self, i_rank: int, i_elem: Reference) -> 'HybridShapeTrim':
        self.hybrid_shape_trim.SetElem(i_rank, i_elem._com)
        return self

    def set_next_orientation(self, i_rank: int, i_orientation: int) -> 'HybridShapeTrim':
        self.hybrid_shape_trim.SetNextOrientation(i_rank, i_orientation)
        return self

    def set_piece_discrimination_index(self, i_rank: int, i_index: int) -> 'HybridShapeTrim':
        self.hybrid_shape_trim.SetPieceDiscriminationIndex(i_rank, i_index)
        return self

    def set_portion_to_keep(self, i_rank: int, i_portion_number: int) -> 'HybridShapeTrim':
        self.hybrid_shape_trim.SetPortionToKeep(i_rank, i_portion_number)
        return self

    def set_previous_orientation(self, i_rank: int, i_orientation: int) -> 'HybridShapeTrim':
        self.hybrid_shape_trim.SetPreviousOrientation(i_rank, i_orientation)
        return self

    def __repr__(self):
        return f'HybridShapeTrim(name="{self.name}")'