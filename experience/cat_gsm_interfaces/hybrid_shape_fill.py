from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeFill(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeFill
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_fill = com

    def advanced_tolerant_mode(self, value: int = None) -> Union['HybridShapeFill', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fill.AdvancedTolerantMode = value
            return self
        return self.hybrid_shape_fill.AdvancedTolerantMode

    def constraint(self, value: Reference = None) -> Union['HybridShapeFill', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fill.Constraint = value._com
            return self
        return Reference(self.hybrid_shape_fill.Constraint)

    def continuity(self, value: int = None) -> Union['HybridShapeFill', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fill.Continuity = value
            return self
        return self.hybrid_shape_fill.Continuity

    def detection(self, value: int = None) -> Union['HybridShapeFill', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fill.Detection = value
            return self
        return self.hybrid_shape_fill.Detection

    def maximum_deviation_value(self, value: float = None) -> Union['HybridShapeFill', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fill.MaximumDeviationValue = value
            return self
        return self.hybrid_shape_fill.MaximumDeviationValue

    def plane_only_mode(self, value: bool = None) -> Union['HybridShapeFill', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fill.PlaneOnlyMode = value
            return self
        return self.hybrid_shape_fill.PlaneOnlyMode

    def tolerant_mode(self, value: bool = None) -> Union['HybridShapeFill', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fill.TolerantMode = value
            return self
        return self.hybrid_shape_fill.TolerantMode

    def add_bound(self, i_boundary: Reference) -> 'HybridShapeFill':
        self.hybrid_shape_fill.AddBound(i_boundary._com)
        return self

    def add_support_at_bound(self, i_boundary: Reference, i_support: Reference) -> 'HybridShapeFill':
        self.hybrid_shape_fill.AddSupportAtBound(i_boundary._com, i_support._com)
        return self

    def append_constraint(self, i_constraint: Reference) -> 'HybridShapeFill':
        self.hybrid_shape_fill.AppendConstraint(i_constraint._com)
        return self

    def get_bound_at_position(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_fill.GetBoundAtPosition(i_pos))

    def get_bound_position(self, i_boundary: Reference) -> int:
        return self.hybrid_shape_fill.GetBoundPosition(i_boundary.com)

    def get_bound_size(self) -> int:
        return self.hybrid_shape_fill.GetBoundSize()

    def get_boundary_continuity(self, i_pos: int) -> int:
        return self.hybrid_shape_fill.GetBoundaryContinuity(i_pos)

    def get_constraint_at_position(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_fill.GetConstraintAtPosition(i_pos))

    def get_constraints_size(self) -> int:
        return self.hybrid_shape_fill.GetConstraintsSize()

    def get_support_at_position(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_fill.GetSupportAtPosition(i_pos))

    def insert_bound_after_position(self, i_boundary: Reference, i_pos: int) -> 'HybridShapeFill':
        self.hybrid_shape_fill.InsertBoundAfterPosition(i_boundary._com, i_pos)
        return self

    def remove_all_bound(self) -> 'HybridShapeFill':
        self.hybrid_shape_fill.RemoveAllBound()
        return self

    def remove_all_constraints(self) -> 'HybridShapeFill':
        self.hybrid_shape_fill.RemoveAllConstraints()
        return self

    def remove_bound_at_position(self, i_pos: int) -> 'HybridShapeFill':
        self.hybrid_shape_fill.RemoveBoundAtPosition(i_pos)
        return self

    def remove_constraint(self, i_pos: int) -> 'HybridShapeFill':
        self.hybrid_shape_fill.RemoveConstraint(i_pos)
        return self

    def remove_support_at_position(self, i_pos: int) -> 'HybridShapeFill':
        self.hybrid_shape_fill.RemoveSupportAtPosition(i_pos)
        return self

    def replace_bound_at_position(self, i_boundary: Reference, i_pos: int) -> 'HybridShapeFill':
        self.hybrid_shape_fill.ReplaceBoundAtPosition(i_boundary.com, i_pos)
        return self

    def replace_constraint(self, i_pos: int, i_constraint: Reference) -> 'HybridShapeFill':
        self.hybrid_shape_fill.ReplaceConstraint(i_pos, i_constraint._com)
        return self

    def replace_support_at_position(self, i_support: Reference, i_pos: int) -> 'HybridShapeFill':
        self.hybrid_shape_fill.ReplaceSupportAtPosition(i_support._com, i_pos)
        return self

    def set_boundary_continuity(self, i_continuity: int, i_pos: int) -> 'HybridShapeFill':
        self.hybrid_shape_fill.SetBoundaryContinuity(i_continuity, i_pos)
        return self

    def __repr__(self):
        return f'HybridShapeFill(name="{self.name}")'