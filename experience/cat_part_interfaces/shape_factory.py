from typing import Union, Optional, TYPE_CHECKING

from experience.system import AnyObject
from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import Body, Factory
from experience.cat_part_interfaces.cat_part_types import *
from experience.cat_part_interfaces import Add
from experience.cat_part_interfaces import Assemble
from experience.cat_part_interfaces import AutoDraft
from experience.cat_part_interfaces import AutoFillet
from experience.cat_part_interfaces import Chamfer
from experience.cat_part_interfaces import CircPattern
from experience.cat_part_interfaces import CloseSurface
from experience.cat_part_interfaces import ConstRadEdgeFillet
from experience.cat_part_interfaces import Defeaturing
from experience.cat_part_interfaces import Draft
from experience.cat_part_interfaces import FaceFillet
from experience.cat_part_interfaces import Groove
from experience.cat_part_interfaces import Hole
from experience.cat_part_interfaces import Intersect
from experience.cat_part_interfaces import Mirror
from experience.cat_part_interfaces import Pad
from experience.cat_part_interfaces import Partition
from experience.cat_part_interfaces import Pocket
from experience.cat_part_interfaces import RectPattern
from experience.cat_part_interfaces import Remove
from experience.cat_part_interfaces import RemoveFace
from experience.cat_part_interfaces import ReplaceFace
from experience.cat_part_interfaces import Rib
from experience.cat_part_interfaces import Scaling
from experience.cat_part_interfaces import SewSurface
from experience.cat_part_interfaces import Shaft
from experience.cat_part_interfaces import Shell
from experience.cat_part_interfaces import Slot
from experience.cat_part_interfaces import SolidCombine
from experience.cat_part_interfaces import Split
from experience.cat_part_interfaces import Stiffener
from experience.cat_part_interfaces import ThickSurface
from experience.cat_part_interfaces import Thickness
from experience.cat_part_interfaces import Thread
from experience.cat_part_interfaces import Trim
from experience.cat_part_interfaces import TritangentFillet
from experience.cat_part_interfaces import UserPattern
from experience.cat_part_interfaces import VarRadEdgeFillet

if TYPE_CHECKING:
    from experience.cat_sketcher_interfaces import Sketch
    from experience.cat_gsm_interfaces import HybridShapeSymmetry

class ShapeFactory(Factory):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Factory
                |                         ShapeFactory
    """

    def __init__(self, com):
        super().__init__(com)
        self.shape_factory = com

    def add_new_add(self, i_body_to_add: Body) -> Add:
        return Add(self.shape_factory.AddNewAdd(i_body_to_add._com))

    def add_new_affinity2(self, x_ratio: float, y_ratio: float, z_ratio: float) -> AnyObject:
        return AnyObject(self.shape_factory.AddNewAffinity2(x_ratio, y_ratio, z_ratio))

    def add_new_assemble(self, i_body_to_assemble: Body) -> Assemble:
        return Assemble(self.shape_factory.AddNewAssemble(i_body_to_assemble._com))

    def add_new_auto_draft(self, i_draft_angle: float) -> AutoDraft:
        return AutoDraft(self.shape_factory.AddNewAutoDraft(i_draft_angle))

    def add_new_auto_fillet(self, i_fillet_radius: float, i_round_radius: float) -> AutoFillet:
        return AutoFillet(self.shape_factory.AddNewAutoFillet(i_fillet_radius, i_round_radius))

    def add_new_axis_to_axis2(self, i_reference: Reference, i_target: Reference) -> AnyObject:
        return AnyObject(self.shape_factory.AddNewAxisToAxis2(i_reference._com, i_target._com))

    def add_new_blend(self) -> AnyObject:
        return AnyObject(self.shape_factory.AddNewBlend())

    def add_new_chamfer(
            self, i_object_to_chamfer: Reference, i_propagation: CatChamferPropagation, i_mode: CatChamferMode,
            i_orientation: CatChamferOrientation, i_length1: float, i_length2_or_angle: float) -> Chamfer:
        return Chamfer(
            self.shape_factory.AddNewChamfer(
                i_object_to_chamfer._com, int(i_propagation), int(i_mode),
                int(i_orientation), i_length1, i_length2_or_angle))
    
    def add_new_circ_pattern(self, i_shape_to_copy: AnyObject, i_nb_of_copies_in_radial_dir: int,
                             i_nb_of_copies_in_angular_dir: int, i_step_in_radial_dir: float,
                             i_step_in_angular_dir: float, i_shape_to_copy_position_along_radial_dir: int,
                             i_shape_to_copy_position_along_angular_dir: int, i_rotation_center: Reference,
                             i_rotation_axis: Reference, i_is_reversed_rotation_axis: bool, i_rotation_angle: float,
                             i_is_radius_aligned: bool) -> CircPattern:
        return CircPattern(
            self.shape_factory.AddNewCircPattern(i_shape_to_copy._com, i_nb_of_copies_in_radial_dir,
                                                 i_nb_of_copies_in_angular_dir, i_step_in_radial_dir,
                                                 i_step_in_angular_dir, i_shape_to_copy_position_along_radial_dir,
                                                 i_shape_to_copy_position_along_angular_dir,
                                                 i_rotation_center._com, i_rotation_axis._com,
                                                 i_is_reversed_rotation_axis, i_rotation_angle, i_is_radius_aligned))

    def add_new_circ_patternof_list(self, i_shape_to_copy: AnyObject, i_nb_of_copies_in_radial_dir: int,
                                    i_nb_of_copies_in_angular_dir: int, i_step_in_radial_dir: float,
                                    i_step_in_angular_dir: float, i_shape_to_copy_position_along_radial_dir: int,
                                    i_shape_to_copy_position_along_angular_dir: int, i_rotation_center: Reference,
                                    i_rotation_axis: Reference, i_is_reversed_rotation_axis: bool,
                                    i_rotation_angle: float, i_is_radius_aligned: bool) -> CircPattern:
        return CircPattern(
            self.shape_factory.AddNewCircPatternofList(i_shape_to_copy._com, i_nb_of_copies_in_radial_dir,
                                                       i_nb_of_copies_in_angular_dir, i_step_in_radial_dir,
                                                       i_step_in_angular_dir, i_shape_to_copy_position_along_radial_dir,
                                                       i_shape_to_copy_position_along_angular_dir,
                                                       i_rotation_center._com, i_rotation_axis._com,
                                                       i_is_reversed_rotation_axis, i_rotation_angle,
                                                       i_is_radius_aligned))

    def add_new_close_surface(self, i_close_element: Reference) -> CloseSurface:
        return CloseSurface(self.shape_factory.AddNewCloseSurface(i_close_element._com))

    def add_new_defeaturing(self) -> Defeaturing:
        return Defeaturing(self.shape_factory.AddNewDefeaturing())

    def add_new_draft(
            self,
            i_face_to_draft: Reference,
            i_neutral: Reference,
            i_neutral_mode: CatDraftNeutralPropagationMode,
            i_parting: Reference,
            i_dir_x: float,
            i_dir_y: float,
            i_dir_z: float,
            i_mode: CatDraftMode,
            i_angle: float,
            i_multiselection_mode: CatDraftMultiselectionMode) -> Draft:
        return Draft(
            self.shape_factory.AddNewDraft(
                i_face_to_draft._com,
                i_neutral._com,
                int(i_neutral_mode),
                i_parting._com,
                i_dir_x,
                i_dir_y,
                i_dir_z,
                int(i_mode),
                i_angle,
                int(i_multiselection_mode)
            )
        )

    def add_new_edge_fillet_with_constant_radius(self, i_edge_to_fillet: Reference, i_propag_mode: CatFilletEdgePropagation,
                                                 i_radius: float) -> ConstRadEdgeFillet:
        return ConstRadEdgeFillet(
            self.shape_factory.AddNewEdgeFilletWithConstantRadius(i_edge_to_fillet._com, int(i_propag_mode), i_radius))

    def add_new_edge_fillet_with_varying_radius(self, i_edge_to_fillet: Reference, i_propag_mode: CatFilletEdgePropagation,
                                                i_variation_mode: CatFilletVariation, i_default_radius: float) -> VarRadEdgeFillet:
        return VarRadEdgeFillet(
            self.shape_factory.AddNewEdgeFilletWithVaryingRadius(i_edge_to_fillet._com, int(i_propag_mode),
                                                                 int(i_variation_mode), i_default_radius))

    def add_new_face_fillet(self, i_f1: Reference, i_f2: Reference, i_radius: float) -> FaceFillet:
        return FaceFillet(self.shape_factory.AddNewFaceFillet(i_f1._com, i_f2._com, i_radius))

    def add_new_gsd_circ_pattern(self, i_shape_to_copy: AnyObject, i_nb_of_copies_in_radial_dir: int,
                                 i_nb_of_copies_in_angular_dir: int, i_step_in_radial_dir: float,
                                 i_step_in_angular_dir: float, i_shape_to_copy_position_along_radial_dir: int,
                                 i_shape_to_copy_position_along_angular_dir: int, i_rotation_center: Reference,
                                 i_rotation_axis: Reference, i_is_reversed_rotation_axis: bool, i_rotation_angle: float,
                                 i_is_radius_aligned: bool, i_complete_crown: bool, i_type: float) -> CircPattern:
        return CircPattern(
            self.shape_factory.AddNewGSDCircPattern(i_shape_to_copy._com, i_nb_of_copies_in_radial_dir,
                                                    i_nb_of_copies_in_angular_dir, i_step_in_radial_dir,
                                                    i_step_in_angular_dir, i_shape_to_copy_position_along_radial_dir,
                                                    i_shape_to_copy_position_along_angular_dir,
                                                    i_rotation_center._com, i_rotation_axis._com,
                                                    i_is_reversed_rotation_axis, i_rotation_angle, i_is_radius_aligned,
                                                    i_complete_crown, i_type))

    def add_new_gsd_rect_pattern(self, i_shape_to_copy: AnyObject, i_nb_of_copies_in_dir1: int,
                                 i_nb_of_copies_in_dir2: int, i_step_in_dir1: float, i_step_in_dir2: float,
                                 i_shape_to_copy_position_along_dir1: int, i_shape_to_copy_position_along_dir2: int,
                                 i_dir1: Reference, i_dir2: Reference, i_is_reversed_dir1: bool,
                                 i_is_reversed_dir2: bool, i_rotation_angle: float, i_type: float) -> RectPattern:
        return RectPattern(self.shape_factory.AddNewGSDRectPattern(i_shape_to_copy._com, i_nb_of_copies_in_dir1,
                                                                   i_nb_of_copies_in_dir2, i_step_in_dir1,
                                                                   i_step_in_dir2, i_shape_to_copy_position_along_dir1,
                                                                   i_shape_to_copy_position_along_dir2,
                                                                   i_dir1._com, i_dir2._com,
                                                                   i_is_reversed_dir1, i_is_reversed_dir2,
                                                                   i_rotation_angle, i_type))

    def add_new_groove(self, i_sketch: 'Sketch') -> Groove:
        return Groove(self.shape_factory.AddNewGroove(i_sketch._com))

    def add_new_groove_from_ref(self, i_profile_elt: Reference) -> Groove:
        return Groove(self.shape_factory.AddNewGrooveFromRef(i_profile_elt._com))

    def add_new_hole(self, i_support: Reference, i_depth: float) -> Hole:
        return Hole(self.shape_factory.AddNewHole(i_support._com, i_depth))

    def add_new_hole_from_point(self, i_x: float, i_y: float, i_z: float, i_support: Reference, i_depth: float) -> Hole:
        return Hole(self.shape_factory.AddNewHoleFromPoint(i_x, i_y, i_z, i_support._com, i_depth))

    def add_new_hole_from_ref_point(self, i_origin: Reference, i_support: Reference, i_depth: float) -> Hole:
        return Hole(self.shape_factory.AddNewHoleFromRefPoint(i_origin._com, i_support._com, i_depth))

    def add_new_hole_from_sketch(self, i_sketch: 'Sketch', i_depth: float) -> Hole:
        return Hole(self.shape_factory.AddNewHoleFromSketch(i_sketch._com, i_depth))

    def add_new_hole_with2_constraints(self, i_x: float, i_y: float, i_z: float, i_edge1: Reference, i_edge2: Reference,
                                       i_support: Reference, i_depth: float) -> Hole:
        return Hole(self.shape_factory.AddNewHoleWith2Constraints(i_x, i_y, i_z, i_edge1._com, i_edge2._com,
                                                                  i_support._com, i_depth))

    def add_new_hole_with_constraint(self, i_x: float, i_y: float, i_z: float, i_edge: Reference, i_support: Reference,
                                     i_depth: float) -> Hole:
        return Hole(self.shape_factory.AddNewHoleWithConstraint(i_x, i_y, i_z, i_edge._com, i_support._com, i_depth))

    def add_new_intersect(self, i_body_to_intersect: Body) -> Intersect:
        return Intersect(self.shape_factory.AddNewIntersect(i_body_to_intersect._com))

    def add_new_loft(self) -> AnyObject:
        return AnyObject(self.shape_factory.AddNewLoft())
    
    def add_new_manu_or_auto_partition(self, i_volume_to_be_partitioned: Reference, i_auto_mode: bool,
                                       i_cutting_element: Reference, i_limit: CatPartitionLimitType) -> Partition:
        return Partition(self.shape_factory.AddNewManuOrAutoPartition(i_volume_to_be_partitioned._com, i_auto_mode, 
                                                                      i_cutting_element._com, int(i_limit)))

    def add_new_mirror(self, i_mirroring_element: Reference) -> Mirror:
        return Mirror(self.shape_factory.AddNewMirror(i_mirroring_element._com))

    def add_new_pad(self, i_sketch: 'Sketch', i_height: float) -> Pad:
        return Pad(self.shape_factory.AddNewPad(i_sketch._com, i_height))

    def add_new_pad_from_ref(self, i_profile_elt: Reference, i_height: float) -> Pad:
        return Pad(self.shape_factory.AddNewPadFromRef(i_profile_elt._com, i_height))
    
    def add_new_partition(self, i_splitting_element: Reference, i_split_side: CatSplitSide) -> Split:
        return Partition(self.shape_factory.AddNewPartition(i_splitting_element._com, int(i_split_side)))

    def add_new_pocket(self, i_sketch: 'Sketch', i_height: float) -> Pocket:
        return Pocket(self.shape_factory.AddNewPocket(i_sketch._com, i_height))

    def add_new_pocket_from_ref(self, i_profile_elt: Reference, i_height: float) -> Pocket:
        return Pocket(self.shape_factory.AddNewPocketFromRef(i_profile_elt._com, i_height))

    def add_new_rect_pattern(self, i_shape_to_copy: AnyObject, i_nb_of_copies_in_dir1: int, i_nb_of_copies_in_dir2: int,
                             i_step_in_dir1: float, i_step_in_dir2: float, i_shape_to_copy_position_along_dir1: int,
                             i_shape_to_copy_position_along_dir2: int, i_dir1: Reference, i_dir2: Reference,
                             i_is_reversed_dir1: bool, i_is_reversed_dir2: bool,
                             i_rotation_angle: float) -> RectPattern:
        return RectPattern(self.shape_factory.AddNewRectPattern(i_shape_to_copy._com, i_nb_of_copies_in_dir1,
                                                                i_nb_of_copies_in_dir2, i_step_in_dir1, i_step_in_dir2,
                                                                i_shape_to_copy_position_along_dir1,
                                                                i_shape_to_copy_position_along_dir2, i_dir1._com,
                                                                i_dir2._com, i_is_reversed_dir1,
                                                                i_is_reversed_dir2, i_rotation_angle))

    def add_new_rect_patternof_list(self, i_shape_to_copy: AnyObject, i_nb_of_copies_in_dir1: int,
                                    i_nb_of_copies_in_dir2: int, i_step_in_dir1: float, i_step_in_dir2: float,
                                    i_shape_to_copy_position_along_dir1: int, i_shape_to_copy_position_along_dir2: int,
                                    i_dir1: Reference, i_dir2: Reference, i_is_reversed_dir1: bool,
                                    i_is_reversed_dir2: bool, i_rotation_angle: float) -> RectPattern:
        return RectPattern(
            self.shape_factory.AddNewRectPatternofList(i_shape_to_copy._com, i_nb_of_copies_in_dir1,
                                                       i_nb_of_copies_in_dir2, i_step_in_dir1, i_step_in_dir2,
                                                       i_shape_to_copy_position_along_dir1,
                                                       i_shape_to_copy_position_along_dir2, i_dir1._com,
                                                       i_dir2._com, i_is_reversed_dir1, i_is_reversed_dir2,
                                                       i_rotation_angle))

    def add_new_remove(self, i_body_to_remove: Body) -> Remove:
        return Remove(self.shape_factory.AddNewRemove(i_body_to_remove._com))

    def add_new_remove_face(self, i_keep_faces: Reference, i_remove_faces: Reference) -> RemoveFace:
        return RemoveFace(self.shape_factory.AddNewRemoveFace(i_keep_faces._com, i_remove_faces._com))

    def add_new_removed_blend(self) -> AnyObject:
        return AnyObject(self.shape_factory.AddNewRemovedBlend())

    def add_new_removed_loft(self) -> AnyObject:
        return AnyObject(self.shape_factory.AddNewRemovedLoft())

    def add_new_replace_face(self, i_split_plane: Reference, i_remove_face: Reference,
                             i_splitting_side: CatSplitSide) -> ReplaceFace:
        return ReplaceFace(
            self.shape_factory.AddNewReplaceFace(i_split_plane._com, i_remove_face._com, int(i_splitting_side)))

    def add_new_rib(self, i_sketch: 'Sketch', i_center_curve: 'Sketch') -> Rib:
        return Rib(self.shape_factory.AddNewRib(i_sketch._com, i_center_curve._com))

    def add_new_rib_from_ref(self, i_profile: Reference, i_center_curve: Reference) -> Rib:
        return Rib(self.shape_factory.AddNewRibFromRef(i_profile._com, i_center_curve._com))

    def add_new_scaling(self, i_scaling_reference: Reference, i_factor: float) -> Scaling:
        return Scaling(self.shape_factory.AddNewScaling(i_scaling_reference._com, i_factor))

    def add_new_rotate2(self, i_axis: Reference, i_angle: float) -> AnyObject:
        return AnyObject(self.shape_factory.AddNewRotate2(i_axis._com, i_angle))

    def add_new_sew_surface(self, i_sewing_element: Reference, i_sewing_side: CatSplitSide) -> SewSurface:
        return SewSurface(self.shape_factory.AddNewSewSurface(i_sewing_element._com, int(i_sewing_side)))

    def add_new_shaft(self, i_sketch: 'Sketch') -> Shaft:
        return Shaft(self.shape_factory.AddNewShaft(i_sketch._com))

    def add_new_shaft_from_ref(self, i_profile_elt: Reference) -> Shaft:
        return Shaft(self.shape_factory.AddNewShaftFromRef(i_profile_elt._com))

    def add_new_shell(self, i_face_to_remove: Reference, i_internal_thickness: float,
                      i_external_thickness: float) -> Shell:
        return Shell(
            self.shape_factory.AddNewShell(i_face_to_remove._com, i_internal_thickness, i_external_thickness))

    def add_new_slot(self, i_sketch: 'Sketch', i_center_curve: 'Sketch') -> Slot:
        return Slot(self.shape_factory.AddNewSlot(i_sketch._com, i_center_curve._com))

    def add_new_slot_from_ref(self, i_profile: Reference, i_center_curve: Reference) -> Slot:
        return Slot(self.shape_factory.AddNewSlotFromRef(i_profile._com, i_center_curve._com))

    def add_new_solid_combine(self, i_profile_elt_first: Reference, i_profile_elt_second: Reference) -> SolidCombine:
        return SolidCombine(self.shape_factory.AddNewSolidCombine(i_profile_elt_first._com, i_profile_elt_second._com))

    def add_new_solid_edge_fillet_with_constant_radius(self, i_edge_to_fillet: Reference, i_propag_mode: CatFilletEdgePropagation,
                                                       i_radius: float) -> ConstRadEdgeFillet:
        return ConstRadEdgeFillet(
            self.shape_factory.AddNewSolidEdgeFilletWithConstantRadius(i_edge_to_fillet._com, int(i_propag_mode), i_radius))

    def add_new_solid_edge_fillet_with_varying_radius(self, i_edge_to_fillet: Reference, i_propag_mode: CatFilletEdgePropagation,
                                                      i_variation_mode: CatFilletVariation,
                                                      i_default_radius: float) -> VarRadEdgeFillet:
        return VarRadEdgeFillet(
            self.shape_factory.AddNewSolidEdgeFilletWithVaryingRadius(i_edge_to_fillet._com, int(i_propag_mode),
                                                                      int(i_variation_mode), i_default_radius))

    def add_new_solid_face_fillet(self, i_f1: Reference, i_f2: Reference, i_radius: float) -> FaceFillet:
        return FaceFillet(self.shape_factory.AddNewSolidFaceFillet(i_f1._com, i_f2._com, i_radius))

    def add_new_solid_tritangent_fillet(self, i_f1: Reference, i_f2: Reference,
                                        i_removed_face: Reference) -> TritangentFillet:
        return TritangentFillet(
            self.shape_factory.AddNewSolidTritangentFillet(i_f1._com, i_f2._com, i_removed_face._com))

    def add_new_split(self, i_splitting_element: Reference, i_split_side: CatSplitSide) -> Split:
        return Split(self.shape_factory.AddNewSplit(i_splitting_element._com, int(i_split_side)))

    def add_new_stiffener(self, i_sketch: 'Sketch') -> Stiffener:
        return Stiffener(self.shape_factory.AddNewStiffener(i_sketch._com))

    def add_new_stiffener_from_ref(self, i_profile_elt: Reference) -> Stiffener:
        return Stiffener(self.shape_factory.AddNewStiffenerFromRef(i_profile_elt._com))

    def add_new_surface_edge_fillet_with_constant_radius(self, i_edge_to_fillet: Reference, i_propag_mode: CatFilletEdgePropagation,
                                                         i_radius: float) -> ConstRadEdgeFillet:
        return ConstRadEdgeFillet(
            self.shape_factory.AddNewSurfaceEdgeFilletWithConstantRadius(i_edge_to_fillet._com, int(i_propag_mode),
                                                                         i_radius))

    def add_new_surface_edge_fillet_with_varying_radius(self, i_edge_to_fillet: Reference, i_propag_mode: CatFilletEdgePropagation,
                                                        i_variation_mode: CatFilletVariation,
                                                        i_default_radius: float) -> VarRadEdgeFillet:
        return VarRadEdgeFillet(
            self.shape_factory.AddNewSurfaceEdgeFilletWithVaryingRadius(i_edge_to_fillet._com, int(i_propag_mode),
                                                                        int(i_variation_mode), i_default_radius))

    def add_new_surface_face_fillet(self, i_f1: Reference, i_f2: Reference, i_radius: float) -> FaceFillet:
        return FaceFillet(self.shape_factory.AddNewSurfaceFaceFillet(i_f1._com, i_f2._com, i_radius))

    def add_new_surface_tritangent_fillet(self, i_f1: Reference, i_f2: Reference,
                                          i_removed_face: Reference) -> TritangentFillet:
        return TritangentFillet(self.shape_factory.AddNewSurfaceTritangentFillet(i_f1._com, i_f2._com,
                                                                                 i_removed_face._com))

    def add_new_surfacic_auto_fillet(self, i_fillet_radius: float) -> AutoFillet:
        return AutoFillet(self.shape_factory.AddNewSurfacicAutoFillet(i_fillet_radius))

    def add_new_surfacic_circ_pattern(self, i_shape_to_copy: AnyObject, i_nb_of_copies_in_radial_dir: int,
                                      i_nb_of_copies_in_angular_dir: int, i_step_in_radial_dir: float,
                                      i_step_in_angular_dir: float, i_shape_to_copy_position_along_radial_dir: int,
                                      i_shape_to_copy_position_along_angular_dir: int, i_rotation_center: Reference,
                                      i_rotation_axis: Reference, i_is_reversed_rotation_axis: bool,
                                      i_rotation_angle: float, i_is_radius_aligned: bool,
                                      i_complete_crown: bool) -> CircPattern:
        return CircPattern(
            self.shape_factory.AddNewSurfacicCircPattern(i_shape_to_copy._com, i_nb_of_copies_in_radial_dir,
                                                         i_nb_of_copies_in_angular_dir, i_step_in_radial_dir,
                                                         i_step_in_angular_dir,
                                                         i_shape_to_copy_position_along_radial_dir,
                                                         i_shape_to_copy_position_along_angular_dir,
                                                         i_rotation_center._com, i_rotation_axis._com,
                                                         i_is_reversed_rotation_axis, i_rotation_angle,
                                                         i_is_radius_aligned, i_complete_crown))

    def add_new_surfacic_rect_pattern(self, i_shape_to_copy: AnyObject, i_nb_of_copies_in_dir1: int,
                                      i_nb_of_copies_in_dir2: int, i_step_in_dir1: float, i_step_in_dir2: float,
                                      i_shape_to_copy_position_along_dir1: int,
                                      i_shape_to_copy_position_along_dir2: int, i_dir1: Reference, i_dir2: Reference,
                                      i_is_reversed_dir1: bool, i_is_reversed_dir2: bool,
                                      i_rotation_angle: float) -> RectPattern:
        return RectPattern(
            self.shape_factory.AddNewSurfacicRectPattern(i_shape_to_copy._com, i_nb_of_copies_in_dir1,
                                                         i_nb_of_copies_in_dir2, i_step_in_dir1, i_step_in_dir2,
                                                         i_shape_to_copy_position_along_dir1,
                                                         i_shape_to_copy_position_along_dir2, i_dir1._com,
                                                         i_dir2._com, i_is_reversed_dir1, i_is_reversed_dir2,
                                                         i_rotation_angle))

    def add_new_surfacic_sew_surface(self, i_type: int, i_support_surface: Reference, i_sewing_element: Reference,
                                     i_sewing_side: CatSplitSide) -> SewSurface:
        return SewSurface(self.shape_factory.AddNewSurfacicSewSurface(i_type, i_support_surface._com,
                                                                      i_sewing_element._com, int(i_sewing_side)))

    def add_new_surfacic_user_pattern(self, i_shape_to_copy: AnyObject, i_nb_of_copies: int) -> UserPattern:
        return UserPattern(self.shape_factory.AddNewSurfacicUserPattern(i_shape_to_copy._com, i_nb_of_copies))

    def add_new_symmetry_2(self, i_reference: Reference) -> 'HybridShapeSymmetry':
        from experience.cat_gsm_interfaces import HybridShapeSymmetry
        return HybridShapeSymmetry(self.shape_factory.AddNewSymmetry2(i_reference._com))

    def add_new_thick_surface(self, i_offset_element: Reference, i_isens_offset: int, i_top_offset: float,
                              i_bot_offset: float) -> ThickSurface:
        return ThickSurface(
            self.shape_factory.AddNewThickSurface(i_offset_element._com, i_isens_offset, i_top_offset, i_bot_offset))

    def add_new_thickness(self, i_face_to_thicken: Reference, i_offset: float) -> Thickness:
        return Thickness(self.shape_factory.AddNewThickness(i_face_to_thicken._com, i_offset))

    def add_new_thread_with_out_ref(self) -> Thread:
        return Thread(self.shape_factory.AddNewThreadWithOutRef())

    def add_new_thread_with_ref(self, i_lateral_face: Reference, i_limit_face: Reference) -> Thread:
        return Thread(self.shape_factory.AddNewThreadWithRef(i_lateral_face._com, i_limit_face._com))

    def add_new_trim(self, i_body_to_trim: Body) -> Trim:
        return Trim(self.shape_factory.AddNewTrim(i_body_to_trim._com))

    def add_new_tritangent_fillet(self, i_f1: Reference, i_f2: Reference,
                                  i_removed_face: Reference) -> TritangentFillet:
        return TritangentFillet(
            self.shape_factory.AddNewTritangentFillet(i_f1._com, i_f2._com, i_removed_face._com))

    def add_new_user_pattern(self, i_shape_to_copy: AnyObject, i_nb_of_copies: int) -> UserPattern:
        return UserPattern(self.shape_factory.AddNewUserPattern(i_shape_to_copy._com, i_nb_of_copies))

    def add_new_user_patternof_list(self, i_shape_to_copy: AnyObject, i_nb_of_copies: int) -> UserPattern:
        return UserPattern(self.shape_factory.AddNewUserPatternofList(i_shape_to_copy._com, i_nb_of_copies))

    def add_new_volume_add(self, i_body1: Reference, i_body2: Reference, i_type: float) -> Add:
        return Add(self.shape_factory.AddNewVolumeAdd(i_body1._com, i_body2._com, i_type))

    def add_new_volume_close_surface(self, i_close_element: Reference) -> CloseSurface:
        return CloseSurface(self.shape_factory.AddNewVolumeCloseSurface(i_close_element._com))

    def add_new_volume_intersect(self, i_body1: Reference, i_body2: Reference, i_type: float) -> Intersect:
        return Intersect(self.shape_factory.AddNewVolumeIntersect(i_body1._com, i_body2._com, i_type))

    def add_new_volume_remove(self, i_body1: Reference, i_body2: Reference, i_type: float) -> Remove:
        return Remove(self.shape_factory.AddNewVolumeRemove(i_body1._com, i_body2._com, i_type))

    def add_new_volume_sew_surface(self, i_type: int, i_support_volume: Reference, i_sewing_element: Reference,
                                   i_sewing_side: CatSplitSide) -> SewSurface:
        return SewSurface(
            self.shape_factory.AddNewVolumeSewSurface(i_type, i_support_volume._com, i_sewing_element._com, int(i_sewing_side)))

    def add_new_volume_shell(self, i_face_to_remove: Reference, i_internal_thickness: float,
                             i_external_thickness: float, i_volume_support: Reference) -> Shell:
        return Shell(self.shape_factory.AddNewVolumeShell(i_face_to_remove._com, i_internal_thickness,
                                                          i_external_thickness, i_volume_support._com))

    def add_new_volume_thick_surface(self, i_offset_element: Reference, i_isens_offset: int, i_top_offset: float,
                                     i_bot_offset: float) -> ThickSurface:
        return ThickSurface(
            self.shape_factory.AddNewVolumeThickSurface(i_offset_element._com, i_isens_offset, i_top_offset,i_bot_offset))

    def add_new_volume_thickness(self, i_face_to_thicken: Reference, i_offset: float, i_type: int,
                                 i_volume_support: Reference) -> Thickness:
        return Thickness(self.shape_factory.AddNewVolumeThickness(i_face_to_thicken._com, i_offset, i_type,
                                                                  i_volume_support._com))

    def add_new_volume_trim(self, i_support_volume: Reference, i_cutting_volume: Reference) -> Trim:
        return Trim(self.shape_factory.AddNewVolumeTrim(i_support_volume._com, i_cutting_volume._com))

    def add_new_volumic_draft(self, i_face_to_draft: Reference, i_neutral: Reference, i_neutral_mode: CatDraftNeutralPropagationMode,
                              i_parting: Reference, i_dir_x: float, i_dir_y: float, i_dir_z: float, i_mode: CatDraftMode,
                              i_angle: float, i_multiselection_mode: CatDraftMultiselectionMode, i_type: int,
                              i_volume_support: Reference) -> Draft:
        return Draft(
            self.shape_factory.AddNewVolumicDraft(i_face_to_draft._com, i_neutral._com, int(i_neutral_mode),
                                                  i_parting._com, i_dir_x, i_dir_y, i_dir_z, int(i_mode), i_angle,
                                                  int(i_multiselection_mode), i_type, i_volume_support._com))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'