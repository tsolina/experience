from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeAssemble(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeAssemble
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_assemble = com

    def invert(self, value: bool = None) -> Union['HybridShapeAssemble', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_assemble.Invert = value
            return self
        return self.hybrid_shape_assemble.Invert

    def add_element(self, i_element: Reference) -> 'HybridShapeAssemble':
        """ perform the action and return self"""
        self.hybrid_shape_assemble.AddElement(i_element._com)
        return self

    def add_sub_element(self, i_sub_element: Reference) -> 'HybridShapeAssemble':
        """ perform the action and return self"""
        self.hybrid_shape_assemble.AddSubElement(i_sub_element._com)
        return self

    def append_federated_element(self, i_element: Reference) -> 'HybridShapeAssemble':
        """ perform the action and return self"""
        self.hybrid_shape_assemble.AppendFederatedElement(i_element._com)
        return self

    def get_angular_tolerance(self) -> float:
        return self.hybrid_shape_assemble.GetAngularTolerance()

    def get_angular_tolerance_mode(self) -> bool:
        return self.hybrid_shape_assemble.GetAngularToleranceMode()

    def get_connex(self) -> bool:
        return self.hybrid_shape_assemble.GetConnex()

    def get_deviation(self) -> float:
        return self.hybrid_shape_assemble.GetDeviation()

    def get_element(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_assemble.GetElement(i_rank))

    def get_elements_size(self) -> int:
        return self.hybrid_shape_assemble.GetElementsSize()

    def get_federated_element(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_assemble.GetFederatedElement(i_rank))

    def get_federated_elements_size(self) -> int:
        return self.hybrid_shape_assemble.GetFederatedElementsSize()

    def get_federation_propagation(self) -> int:
        return self.hybrid_shape_assemble.GetFederationPropagation()
    
    def get_healing_mode(self) -> bool:
        return self.hybrid_shape_assemble.GetHealingMode()

    def get_manifold(self) -> bool:
        return self.hybrid_shape_assemble.GetManifold()

    def get_simplify(self) -> bool:
        return self.hybrid_shape_assemble.GetSimplify()

    def get_sub_element(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_assemble.GetSubElement(i_rank))

    def get_sub_elements_size(self) -> int:
        return self.hybrid_shape_assemble.GetSubElementsSize()

    def get_suppress_mode(self) -> bool:
        return self.hybrid_shape_assemble.GetSuppressMode()

    def get_tangency_continuity(self) -> bool:
        return self.hybrid_shape_assemble.GetTangencyContinuity()

    def remove_element(self, i_rank: int) -> 'HybridShapeAssemble':
        """ perform the action and return self"""
        self.hybrid_shape_assemble.RemoveElement(i_rank)
        return self

    def remove_federated_element(self, i_rank: int) -> 'HybridShapeAssemble':
        """ perform the action and return self"""
        self.hybrid_shape_assemble.RemoveFederatedElement(i_rank)
        return self

    def remove_sub_element(self, i_rank: int) -> 'HybridShapeAssemble':
        """ perform the action and return self"""
        self.hybrid_shape_assemble.RemoveSubElement(i_rank)
        return self

    def replace_element(self, i_pos: int, i_element: Reference) -> 'HybridShapeAssemble':
        """ perform the action and return self"""
        self.hybrid_shape_assemble.ReplaceElement(i_pos, i_element._com)
        return self

    def set_angular_tolerance(self, i_value: float) -> 'HybridShapeAssemble':
        """ perform the action and return self"""
        self.hybrid_shape_assemble.SetAngularTolerance(i_value)
        return self

    def set_angular_tolerance_mode(self, i_value: bool) -> 'HybridShapeAssemble':
        """ perform the action and return self"""
        self.hybrid_shape_assemble.SetAngularToleranceMode(i_value)
        return self

    def set_connex(self, i_connex: bool) -> 'HybridShapeAssemble':
        """ perform the action and return self"""
        self.hybrid_shape_assemble.SetConnex(i_connex)
        return self

    def set_deviation(self, ideviation: float) -> 'HybridShapeAssemble':
        """ perform the action and return self"""
        self.hybrid_shape_assemble.SetDeviation(ideviation)
        return self       

    def set_federation_propagation(self, i_mode: int) -> 'HybridShapeAssemble':
        """ perform the action and return self"""
        self.hybrid_shape_assemble.SetFederationPropagation(i_mode)
        return self

    def set_manifold(self, i_manifold: bool) -> 'HybridShapeAssemble':
        """ perform the action and return self"""
        self.hybrid_shape_assemble.SetManifold(i_manifold)
        return self

    def set_simplify(self, i_simplify: bool) -> 'HybridShapeAssemble':
        """ perform the action and return self"""
        self.hybrid_shape_assemble.SetSimplify(i_simplify)
        return self

    def set_suppress_mode(self, i_suppress_mode: bool) -> 'HybridShapeAssemble':
        """ perform the action and return self"""
        self.hybrid_shape_assemble.SetSuppressMode(i_suppress_mode)
        return self

    def set_tangency_continuity(self, i_tangency_continuity: bool) -> 'HybridShapeAssemble':
        """ perform the action and return self"""
        self.hybrid_shape_assemble.SetTangencyContinuity(i_tangency_continuity)
        return self

    def __repr__(self):
        return f'HybridShapeAssemble(name="{ self.name }")'