from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class HybridShapeExtrapol(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeExtrapol
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_extrapol = com

    def border_type(self, value: int = None) -> Union['HybridShapeExtrapol', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrapol.BorderType = value
            return self
        return self.hybrid_shape_extrapol.BorderType

    def boundary(self, i_pos: int, value: Reference = None) -> Union['HybridShapeExtrapol', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrapol.SetBoundary(i_pos, value._com)
            return self
        return Reference(self.hybrid_shape_extrapol.GetBoundary(i_pos))

    def constant_length_mode(self, value: bool = None) -> Union['HybridShapeExtrapol', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrapol.ConstantLengthMode = value
            return self
        return self.hybrid_shape_extrapol.ConstantLengthMode

    def continuity_type(self, i_pos: int, value: int = None) -> Union['HybridShapeExtrapol', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrapol.SetContinuityType(i_pos, value)
            return self
        return self.hybrid_shape_extrapol.GetContinuityType(i_pos)

    def elem_to_extrapol(self, value: Reference = None) -> Union['HybridShapeExtrapol', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrapol.ElemToExtrapol = value._com
            return self
        return Reference(self.hybrid_shape_extrapol.ElemToExtrapol)

    def elem_until(self, i_pos: int, value: Reference = None) -> Union['HybridShapeExtrapol', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrapol.SetElemUntil(i_pos, value._com)
            return self
        return Reference(self.hybrid_shape_extrapol.GetElemUntil(i_pos))

    def extend_edges_mode(self, value: bool = None) -> Union['HybridShapeExtrapol', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrapol.ExtendEdgesMode = value
            return self
        return self.hybrid_shape_extrapol.ExtendEdgesMode

    def extrapol_both_sides_identically(self, value: bool = None) -> Union['HybridShapeExtrapol', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrapol.ExtrapolBothSidesIdentically = value
            return self
        return self.hybrid_shape_extrapol.ExtrapolBothSidesIdentically

    def length(self, i_pos: int) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_extrapol.GetLength(i_pos))

    def limit_type(self, i_pos: int, value: int = None) -> Union['HybridShapeExtrapol', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrapol.SetLimitType(i_pos, value)
            return self
        return self.hybrid_shape_extrapol.GetLimitType(i_pos)

    def propagation_mode(self, value: int = None) -> Union['HybridShapeExtrapol', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrapol.PropagationMode = value
            return self
        return self.hybrid_shape_extrapol.PropagationMode

    def support(self, value: Reference = None) -> Union['HybridShapeExtrapol', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrapol.Support = value._com
            return self
        return Reference(self.hybrid_shape_extrapol.Support)

    def get_internal_edges_element(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_extrapol.GetInternalEdgesElement(i_pos))

    def get_number_of_extrapolations(self) -> int:
        return self.hybrid_shape_extrapol.GetNumberOfExtrapolations()

    def is_assemble(self) -> bool:
        return self.hybrid_shape_extrapol.IsAssemble()

    def remove_all_extrapolations_except_the_first_one(self) -> 'HybridShapeExtrapol':
        self.hybrid_shape_extrapol.RemoveAllExtrapolationsExceptTheFirstOne()
        return self

    def remove_all_internal_edges_element(self) -> 'HybridShapeExtrapol':
        self.hybrid_shape_extrapol.RemoveAllInternalEdgesElement()
        return self

    def remove_extrapolation(self, i_pos: int) -> 'HybridShapeExtrapol':
        self.hybrid_shape_extrapol.RemoveExtrapolation(i_pos)
        return self

    def set_assemble(self, i_assemble: bool) -> 'HybridShapeExtrapol':
        self.hybrid_shape_extrapol.SetAssemble(i_assemble)
        return self

    def set_length_d(self, i_pos: int, i_length: float) -> 'HybridShapeExtrapol':
        self.hybrid_shape_extrapol.SetLengthD(i_pos, i_length)
        return self

    def __repr__(self):
        return f'HybridShapeExtrapol(name="{self.name}")'