from typing import TYPE_CHECKING

#from pycatia.mec_mod_interfaces.factory import Factory
# from experience.cat_tps_interfaces import Annotation2, UserSurface
from experience.drafting_interfaces import DrawingComponent
from experience.types import cat_variant

from experience.mecmod_interfaces import Factory

if TYPE_CHECKING:
    from experience.cat_tps_interfaces import Annotation2, UserSurface

class AnnotationFactory2(Factory):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Factory
                |                         AnnotationFactory2
    """

    def __init__(self, com):
        super().__init__(com)
        self.annotation_factory_2 = com

    def create_coord_dimension(self, i_surf: 'UserSurface') -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateCoordDimension(i_surf._com))

    def create_datum(self, i_surf: 'UserSurface') -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateDatum(i_surf._com))

    def create_datum_reference_frame(self) -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateDatumReferenceFrame())

    def create_datum_target(self, i_surf: 'UserSurface', i_datum: 'Annotation2') -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateDatumTarget(i_surf._com, i_datum._com))

    def create_ditto_noa(self, i_surf: 'UserSurface', i_noa_type: str, i_ditto: DrawingComponent, i_stick_to_geometry_option: bool) -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateDittoNOA(i_surf._com, i_noa_type, i_ditto._com, i_stick_to_geometry_option))

    def create_evaluate_datum(self, i_surf: 'UserSurface', i_x: float, i_y: float, i_z: float, i_with_leader: bool) -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateEvoluateDatum(i_surf._com, i_x, i_y, i_z, i_with_leader))

    def create_evaluate_text(self, i_surf: 'UserSurface', i_x: float, i_y: float, i_z: float, i_with_leader: bool) -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateEvoluateText(i_surf._com, i_x, i_y, i_z, i_with_leader))

    def create_flag_note(self, i_surf: 'UserSurface') -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateFlagNote(i_surf._com))

    def create_gdt(self, i_surf: 'UserSurface') -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateGDT(i_surf._com))

    def create_non_semantic_dimension(self, i_surf: 'UserSurface', i_type: cat_variant, i_sub_type: cat_variant) -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateNonSemanticDimension(i_surf._com, i_type, i_sub_type))

    def create_roughness(self, i_surf: 'UserSurface') -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateRoughness(i_surf._com))

    def create_semantic_dimension(self, i_surf: 'UserSurface', i_type: cat_variant, i_sub_type: cat_variant) -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateSemanticDimension(i_surf._com, i_type, i_sub_type))

    def create_text(self, i_surf: 'UserSurface') -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateText(i_surf._com))

    def create_text_noa(self, i_surf: 'UserSurface') -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateTextNOA(i_surf._com))

    def create_text_note_object_attribute(self, i_surf: 'UserSurface', i_noa_type: str) -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateTextNoteObjectAttribute(i_surf._com, i_noa_type))

    def create_text_on_annot(self, i_text: str, i_annot: 'Annotation2') -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateTextOnAnnot(i_text, i_annot._com))

    def create_tolerance_with_drf(self, i_index: cat_variant, i_surf: 'UserSurface', i_drf: 'Annotation2') -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateToleranceWithDRF(i_index, i_surf._com, i_drf._com))

    def create_tolerance_without_drf(self, i_index: cat_variant, i_surf: 'UserSurface') -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateToleranceWithoutDRF(i_index, i_surf._com))

    def create_weld(self, i_surf: 'UserSurface') -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.CreateWeld(i_surf._com))

    def instantiate_noa(self, i_noa: 'Annotation2', i_surf: 'UserSurface') -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.annotation_factory_2.InstanciateNOA(i_noa._com, i_surf._com))

    def __repr__(self):
        return f'AnnotationFactory2(name="{self.name}")'
