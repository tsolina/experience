from typing import TYPE_CHECKING

from experience.system import AnyObject
from experience.cat_tps_interfaces import AnnotationFactory, AnnotationFactory2, CaptureFactory, Captures, TPSHyperLinkManager, TPSView, TPSViewFactory, Annotations, TPSViews

if TYPE_CHECKING:
    from experience.mecmod_interfaces import Part

class AnnotationSet(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AnnotationSet
    """

    def __init__(self, com):
        super().__init__(com)
        self.annotation_set = com

    def active_view(self, value: TPSView = None) -> TPSView:
        if value is not None:
            self.annotation_set.ActiveView = value
            return self
        return TPSView(self.annotation_set.ActiveView)


    def an_empty_annotations_list(self) -> Annotations:
        return Annotations(self.annotation_set.AnEmptyAnnotationsList)


    def annotation_factory(self) -> AnnotationFactory:
        # from experience.cat_tps_interfaces.annotation_factory import AnnotationFactory
        return AnnotationFactory(self.annotation_set.AnnotationFactory)


    def annotation_factory_2(self) -> AnnotationFactory2:
        return AnnotationFactory2(self.annotation_set.AnnotationFactory2)

    def annotation_set_purpose(self) -> str:
        return self.annotation_set.AnnotationSetPurpose

    def annotation_set_type(self) -> int:
        return self.annotation_set.AnnotationSetType


    def annotations(self) -> Annotations:
        return Annotations(self.annotation_set.Annotations)


    def capture_factory(self) -> CaptureFactory:
        return CaptureFactory(self.annotation_set.CaptureFactory)


    def captures(self) -> Captures:
        return Captures(self.annotation_set.Captures)

    def kind_of_set(self) -> str:
        return self.annotation_set.KindOfSet

    def standard(self) -> str:
        return self.annotation_set.Standard

    def switch_on(self, value: bool = None) -> bool:
        if value is not None:
            self.annotation_set.SwitchOn = value
            return self
        return self.annotation_set.SwitchOn


    def tps_view_factory(self) -> TPSViewFactory:
        return TPSViewFactory(self.annotation_set.TPSViewFactory)


    def tps_views(self) -> TPSViews:
        return TPSViews(self.annotation_set.TPSViews)

    def apply_result_with_link_when_copy_set_to(self) ->'AnnotationSet':
        self.annotation_set.ApplyResultWithLinkWhenCopySetTo()
        return self

    def apply_view_re_use_when_copy_set_to(self) -> 'AnnotationSet':
        self.annotation_set.ApplyViewReUseWhenCopySetTo()
        return self

    def global_copy_set_to(self, i_destination_part: 'Part') -> str:
        from experience.mecmod_interfaces import Part
        return self.annotation_set.GlobalCopySetTo(i_destination_part._com)

    def global_copy_set_to_with_filter(self, i_destination_part: 'Part', i_capture_filter_name: str) -> str:
        from experience.mecmod_interfaces import Part
        return self.annotation_set.GlobalCopySetToWithFilter(i_destination_part, i_capture_filter_name)

    def global_copy_set_to_with_filter_with_transformation(self, i_destination_part: 'Part', i_transfo: tuple, i_capture_filter_name: str) -> str:
        from experience.mecmod_interfaces import Part
        return self.annotation_set.GlobalCopySetToWithFilterWithTransformation(i_destination_part, i_transfo, i_capture_filter_name)

    def global_copy_set_to_with_transformation(self, i_destination_part: 'Part', i_transfo: tuple) -> str:
        from experience.mecmod_interfaces import Part
        return self.annotation_set.GlobalCopySetToWithTransformation(i_destination_part._com, i_transfo)


    def hyper_link_manager(self) -> TPSHyperLinkManager:
        return self.annotation_set.HyperLinkManager()

    def isolate_links_of_noa(self) -> 'AnnotationSet':
        self.annotation_set.IsolateLinksOfNOA()
        return self

    def logical_global_copy_set_to(self, ipi_target_3dsr: 'Part', i_list_of_bodies_and_geometrical_sets: tuple, ib_import_once: bool) -> str:
        return self.annotation_set.LogicalGlobalCopySetTo(ipi_target_3dsr, i_list_of_bodies_and_geometrical_sets, ib_import_once)

    def logical_global_copy_set_to_with_filter(self, ipi_target_3dsr: 'Part', i_list_of_bodies_and_geometrical_sets: tuple, ib_import_once: bool, i_capture_filter_name: str) -> str:
        return self.annotation_set.LogicalGlobalCopySetTo(ipi_target_3dsr, i_list_of_bodies_and_geometrical_sets, ib_import_once, i_capture_filter_name)

    def read_iso_default_properties(self, o_iso_defaults: tuple) -> int:
        return self.annotation_set.ReadISODefaultProperties(o_iso_defaults)

    def repair_delete_invalid_fta_features(options_to_repair_delete: int) -> 'AnnotationSet':
        self.annotation_set.RepairDeleteInvalidFTAFeatures(options_to_repair_delete)
        return self

    def __repr__(self):
        return f'AnnotationSet(name="{self.name()}")'
