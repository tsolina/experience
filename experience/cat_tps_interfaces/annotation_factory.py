from typing import TYPE_CHECKING

#from pycatia.mec_mod_interfaces.factory import Factory
from experience.cat_tps_interfaces import Noa, UserSurface
from experience.mecmod_interfaces.factory import Factory
from experience.types import cat_variant

if TYPE_CHECKING:
    from experience.cat_tps_interfaces import Annotation

class AnnotationFactory(Factory):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Factory
                |                         AnnotationFactory
    """

    def __init__(self, com):
        super().__init__(com)
        self.annotation_factory = com


    def create_datum(self, i_surf: UserSurface) -> 'Annotation':
        from experience.cat_tps_interfaces import Annotation
        return Annotation(self.annotation_factory.CreateDatum(i_surf._com))


    def create_datum_reference_frame(self) -> 'Annotation': #i_type: int
        from experience.cat_tps_interfaces import Annotation
        return Annotation(self.annotation_factory.CreateDatumReferenceFrame())


    def create_datum_target(self, i_surf: UserSurface, i_datum: 'Annotation') -> 'Annotation':
        from experience.cat_tps_interfaces import Annotation
        return Annotation(self.annotation_factory.CreateDatumTarget(i_surf._com, i_datum._com))


    def create_evaluate_datum(self, i_surf: UserSurface, i_x: float, i_y: float, i_z: float, i_with_leader: bool) -> 'Annotation':
        from experience.cat_tps_interfaces import Annotation
        return Annotation(self.annotation_factory.CreateEvoluateDatum(i_surf._com, i_x, i_y, i_z, i_with_leader))


    def create_evaluate_text(self, i_surf: UserSurface, i_x: float, i_y: float, i_z: float, i_with_leader: bool) -> 'Annotation':
        from experience.cat_tps_interfaces import Annotation
        return Annotation(self.annotation_factory.CreateEvoluateText(i_surf._com, i_x, i_y, i_z, i_with_leader))


    def create_flag_note(self, i_surf: UserSurface) -> 'Annotation':
        from experience.cat_tps_interfaces import Annotation
        return Annotation(self.annotation_factory.CreateFlagNote(i_surf._com))


    def create_non_semantic_dimension(self, i_surf: UserSurface, i_dimension_type: cat_variant, i_linear_dim_sub_type: cat_variant) -> 'Annotation':
        from experience.cat_tps_interfaces import Annotation
        return Annotation(self.annotation_factory.CreateNonSemanticDimension(i_surf._com, i_dimension_type, i_linear_dim_sub_type))


    def create_roughness(self, i_surf: UserSurface) -> 'Annotation':
        from experience.cat_tps_interfaces import Annotation
        return Annotation(self.annotation_factory.CreateRoughness(i_surf._com))


    def create_semantic_dimension(self, i_surf: UserSurface, i_type: cat_variant, i_sub_type: cat_variant) -> 'Annotation':
        from experience.cat_tps_interfaces import Annotation
        return Annotation(self.annotation_factory.CreateSemanticDimension(i_surf._com, i_type, i_sub_type))


    def create_text(self, i_surf: UserSurface) -> 'Annotation':
        from experience.cat_tps_interfaces import Annotation
        return Annotation(self.annotation_factory.CreateText(i_surf._com))


    def create_text_noa(self, i_surf: UserSurface) -> Noa:
        return Noa(self.annotation_factory.CreateTextNOA(i_surf._com))


    def create_text_note_object_attribute(self, i_surf: UserSurface, i_noa_type: str) -> Noa:
        return Noa(self.annotation_factory.CreateTextNoteObjectAttribute(i_surf._com, i_noa_type))


    def create_text_on_annot(self, i_text: str, i_annot: 'Annotation') -> 'Annotation':
        from experience.cat_tps_interfaces import Annotation
        return Annotation(self.annotation_factory.CreateTextOnAnnot(i_text, i_annot._com))


    def create_tolerance_with_drf(self, i_index: cat_variant, i_surf: UserSurface, i_drf: 'Annotation') -> 'Annotation':
        from experience.cat_tps_interfaces import Annotation
        return Annotation(self.annotation_factory.CreateToleranceWithDRF(i_index, i_surf._com, i_drf._com))


    def create_tolerance_without_drf(self, i_index: cat_variant, i_surf: UserSurface) -> 'Annotation':
        from experience.cat_tps_interfaces import Annotation
        return Annotation(self.annotation_factory.CreateToleranceWithoutDRF(i_index, i_surf._com))


    def instantiate_noa(self, i_noa: Noa, i_surf: UserSurface) -> 'Annotation': #NOA?
        from experience.cat_tps_interfaces import Annotation
        return Annotation(self.annotation_factory.InstanciateNOA(i_noa._com, i_surf._com))