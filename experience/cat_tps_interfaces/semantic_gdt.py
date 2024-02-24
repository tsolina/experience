from experience.system import AnyObject
from experience.cat_tps_interfaces import CompositeTolerance, SemanticGDTFrameExtension, FreeState, MaterialCondition, MedianFeature, ParticularTolElem, ProjectedToleranceZone, ShiftedProfileTolerance
from experience.cat_tps_interfaces import SemanticGDTNxDisplay, TPSParallelOnScreen, TangentPlane, TolerancePerUnitBasisRestrictiveValue, ToleranceUnitBasisValue, ToleranceZone

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from experience.cat_tps_interfaces import AssociatedRefFrame

class SemanticGDT(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SemanticGDT
    """

    def __init__(self, com):
        super().__init__(com)
        self.semantic_gdt = com


    def associated_ref_frame(self) -> 'AssociatedRefFrame':
        from experience.cat_tps_interfaces import AssociatedRefFrame
        return AssociatedRefFrame(self.semantic_gdt.AssociatedRefFrame())


    def composite_tolerance(self) -> CompositeTolerance:
        return CompositeTolerance(self.semantic_gdt.CompositeTolerance())


    def frame_extension(self, i_frame_extent_index: int) -> SemanticGDTFrameExtension:
        return SemanticGDTFrameExtension(self.semantic_gdt.FrameExtension())


    def free_state(self) -> FreeState:
        return FreeState(self.semantic_gdt.FreeState())

    def has_a_centered_element(self) -> bool:
        return self.semantic_gdt.HasACenteredElement()

    def has_a_frame_extension(self) -> int:
        return self.semantic_gdt.HasAFrameExtension()

    def has_a_free_state(self) -> bool:
        return self.semantic_gdt.HasAFreeState()

    def has_a_material_condition(self) -> bool:
        return self.semantic_gdt.HasAMaterialCondition()

    def has_a_particular_tol_elem(self) -> bool:
        return self.semantic_gdt.HasAParticularTolElem()

    def has_a_tangent_plane(self) -> bool:
        return self.semantic_gdt.HasATangentPlane()

    def has_a_tolerance_per_unit_basis_restrictive_value(self) -> bool:
        return self.semantic_gdt.HasATolerancePerUnitBasisRestrictiveValue()

    def is_a_composite_tolerance(self) -> bool:
        return self.semantic_gdt.IsACompositeTolerance()

    def is_a_projected_tolerance_zone(self) -> bool:
        return self.semantic_gdt.IsAProjectedToleranceZone()

    def is_a_shifted_profile_tolerance(self) -> bool:
        return self.semantic_gdt.IsAShiftedProfileTolerance()

    def is_a_tolerance_unit_basis_value(self) -> bool:
        return self.semantic_gdt.IsAToleranceUnitBasisValue()

    def is_a_tolerance_zone(self) -> bool:
        return self.semantic_gdt.IsAToleranceZone()

    def is_an_associated_ref_frame(self) -> bool:
        return self.semantic_gdt.IsAnAssociatedRefFrame()

    def is_applied_on_multiple_entities(self) -> bool:
        return self.semantic_gdt.IsAppliedOnMultipleEntities()


    def material_condition(self) -> MaterialCondition:
        return MaterialCondition(self.semantic_gdt.MaterialCondition())


    def median_feature(self) -> MedianFeature:
        return MedianFeature(self.semantic_gdt.MedianFeature())


    def nx_display(self) -> SemanticGDTNxDisplay:
        return SemanticGDTNxDisplay(self.semantic_gdt.NxDisplay())


    def particular_tol_elem(self) -> ParticularTolElem:
        return ParticularTolElem(self.semantic_gdt.ParticularTolElem())


    def projected_tolerance_zone(self) -> ProjectedToleranceZone:
        return ProjectedToleranceZone(self.semantic_gdt.ProjectedToleranceZone())


    def shifted_profile_tolerance(self) -> ShiftedProfileTolerance:
        return ShiftedProfileTolerance(self.semantic_gdt.ShiftedProfileTolerance())


    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        return TPSParallelOnScreen(self.semantic_gdt.TPSParallelOnScreen())


    def tangent_plane(self) -> TangentPlane:
        return TangentPlane(self.semantic_gdt.TangentPlane())


    def tolerance_per_unit_basis_restrictive_value(self) -> TolerancePerUnitBasisRestrictiveValue:
        return TolerancePerUnitBasisRestrictiveValue(self.semantic_gdt.TolerancePerUnitBasisRestrictiveValue())


    def tolerance_unit_basis_value(self) -> ToleranceUnitBasisValue:
        return ToleranceUnitBasisValue(self.semantic_gdt.ToleranceUnitBasisValue())


    def tolerance_zone(self) -> ToleranceZone:
        return ToleranceZone(self.semantic_gdt.ToleranceZone())