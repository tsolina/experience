from experience.system import AnyObject
from experience.cat_tps_interfaces import CompositeTolerance, ControledRadius, DatumSimple, DatumTarget, DefaultAnnotation, Dimension3D, DimensionLimit, DimensionPattern
from experience.cat_tps_interfaces import EnvelopCondition, FlagNote, FreeState, MaterialCondition, Noa, NumericalDisplayFormat, ParticularTolElem, ProjectedToleranceZone, ReferenceFrame
from experience.cat_tps_interfaces import Roughness, ShiftedProfileTolerance, TangentPlane, Text, TolerancePerUnitBasisRestrictiveValue, ToleranceUnitBasisValue, ToleranceZone, TPSView

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from experience.cat_tps_interfaces import AssociatedRefFrame

class Annotation(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Annotation
    """

    def __init__(self, com):
        super().__init__(com)
        self.annotation = com

    def super_type(self) -> str:
        return self.annotation.SuperType

    def tps_status(self) -> str:
        return self.annotation.TPSStatus

    def type(self) -> str:
        return self.annotation.Type

    def z(self, value: float) -> 'Annotation':
        self.annotation.Z = value
        return self

    def add_leader(self) -> 'Annotation':
        self.annotation.AddLeader()
        return self

    def apply_referenced_geom_colour(self, i_releated_r: int, i_releated_g: int, i_releated_b: int) -> 'Annotation':
        self.annotation.ApplyReferencedGeomColor(i_releated_r, i_releated_g, i_releated_b)
        return self

    def apply_referenced_init_colour(self) -> 'Annotation':
        self.annotation.ApplyReferencedInitColor()
        return self


    def associated_ref_frame(self) -> 'AssociatedRefFrame':
        from experience.cat_tps_interfaces import AssociatedRefFrame
        return AssociatedRefFrame(self.annotation.AssociatedRefFrame())


    def composite_tolerance(self) -> CompositeTolerance:
        return CompositeTolerance(self.annotation.CompositeTolerance())


    def controlled_radius(self) -> ControledRadius:
        return ControledRadius(self.annotation.ControledRadius())


    def datum_simple(self) -> DatumSimple:
        return DatumSimple(self.annotation.DatumSimple())


    def datum_target(self) -> DatumTarget:
        return DatumTarget(self.annotation.DatumTarget())


    def default_annotation(self) -> DefaultAnnotation:
        return DefaultAnnotation(self.annotation.DefaultAnnotation())


    def dimension_3d(self) -> Dimension3D:
        return Dimension3D(self.annotation.Dimension3D())


    def dimension_limit(self) -> DimensionLimit:
        return DimensionLimit(self.annotation.DimensionLimit())


    def dimension_pattern(self) -> DimensionPattern:
        return DimensionPattern(self.annotation.DimensionPattern())


    def envelop_condition(self) -> EnvelopCondition:
        return EnvelopCondition(self.annotation.EnvelopeCondition())


    def flag_note(self) -> FlagNote:
        return FlagNote(self.annotation.FlagNote())


    def free_state(self) -> FreeState:
        return FreeState(self.annotation.FreeState())

    def get_geometrical_component_name(self, i_index: float) -> str:
        return self.annotation.GetGeometricalComponentName(i_index)

    def get_Nbr_of_geometrical_component(self) -> float:
        return self.annotation.GetNbrGeometricalComponent()

    def get_surfaces(self, o_safe_array: tuple) -> tuple:
        # return self.annotation.GetSurfaces(o_safe_array)
        return self.annotation.GetSurfaces()

    def get_surfaces_count(self) -> float:
        return self.annotation.GetSurfacesCount()

    def has_a_controlled_radius(self) -> bool:
        return self.annotation.HasAControledRadius()

    def has_a_free_state(self) -> bool:
        return self.annotation.HasAFreeState()

    def has_a_material_condition(self) -> bool:
        return self.annotation.HasAMaterialCondition()

    def has_a_particular_tol_elem(self) -> bool:
        return self.annotation.HasAParticularTolElem()

    def has_a_tolerance_per_unit_basis_restrictive_value(self) -> bool:
        return self.annotation.HasATolerancePerUnitBasisRestrictiveValue()

    def has_an_envelop_condition(self) -> bool:
        return self.annotation.HasAnEnvelopCondition()

    def has_dimension_limit(self) -> bool:
        return self.annotation.HasDimensionLimit()

    def is_a_composite_tolerance(self) -> bool:
        return self.annotation.IsACompositeTolerance()

    def is_a_default_annotation(self) -> bool:
        return self.annotation.IsADefaultAnnotation()

    def is_a_dimension_pattern(self) -> bool:
        return self.annotation.IsADimensionPattern()

    def is_a_projected_tolerance_zone(self) -> bool:
        return self.annotation.IsAProjectedToleranceZone()

    def is_a_shifted_profile_tolerance(self) -> bool:
        return self.annotation.IsAShiftedProfileTolerance()

    def is_a_tangent_plane(self) -> bool:
        return self.annotation.IsATangentPlane()

    def is_a_tolerance_unit_basis_value(self) -> bool:
        return self.annotation.IsAToleranceUnitBasisValue()

    def is_a_tolerance_zone(self) -> bool:
        return self.annotation.IsAToleranceZone()

    def is_an_associated_ref_frame(self) -> bool:
        return self.annotation.IsAnAssociatedRefFrame()


    def material_condition(self) -> MaterialCondition:
        return MaterialCondition(self.annotation.MaterialCondition())

    def modify_visualisation(self) -> 'Annotation':
        self.annotation.ModifyVisu()
        return self


    def noa(self) -> Noa:
        return Noa(self.annotation.Noa())


    def numerical_display_format(self) -> NumericalDisplayFormat:
        return NumericalDisplayFormat(self.annotation.NumericalDisplayFormat())


    def particular_tol_elem(self) -> ParticularTolElem:
        return ParticularTolElem(self.annotation.ParticularTolElem())


    def projected_tolerance_zone(self) -> ProjectedToleranceZone:
        return ProjectedToleranceZone(self.annotation.ProjectedToleranceZone())


    def reference_frame(self) -> ReferenceFrame:
        return ReferenceFrame(self.annotation.ReferenceFrame())


    def roughness(self) -> Roughness:
        return Roughness(self.annotation.Roughness())

    def set_geometrical_component_name(i_index: float, i_new_name: str, i_check_name_unicity_option: bool) -> 'Annotation':
        self.annotation.SetGeometricalComponentName(i_index, i_new_name, i_check_name_unicity_option)
        return self

    def set_xy(self, i_x: float, i_y: float) -> 'Annotation':
        self.annotation.SetXY(i_x, i_y)
        return self


    def shifted_profile_tolerance(self) -> ShiftedProfileTolerance:
        return ShiftedProfileTolerance(self.annotation.ShiftedProfileTolerance())


    def tangent_plane(self) -> TangentPlane:
        return TangentPlane(self.annotation.TangentPlane())


    def text(self) -> Text:
        return Text(self.annotation.Text())


    def tolerance_per_unit_basis_restrictive_value(self) -> TolerancePerUnitBasisRestrictiveValue:
        return TolerancePerUnitBasisRestrictiveValue(self.annotation.TolerancePerUnitBasisRestrictiveValue())


    def tolerance_unit_basis_value(self) -> ToleranceUnitBasisValue:
        return ToleranceUnitBasisValue(self.annotation.ToleranceUnitBasisValue())


    def tolerance_zone(self) -> ToleranceZone:
        return ToleranceZone(self.annotation.ToleranceZone())

    def transfert_to_view(self, i_view: TPSView) -> 'Annotation':
        self.annotation.TransfertToView(i_view.com_object)
        return self

    def __repr__(self):
        return f'Annotation(name="{self.name}")'
