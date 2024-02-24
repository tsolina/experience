from experience.system import AnyObject
from experience.cat_tps_interfaces import CoordDim, DatumSimple, DatumTarget, DefaultAnnotation, Dimension3D
from experience.cat_tps_interfaces import FlagNote, Noa, ReferenceFrame
from experience.cat_tps_interfaces import Roughness, SemanticGDT, Text, TPSView, Weld
from experience.cat_tps_interfaces import NonSemanticGDT, TPSHyperLinkManager, NonSemanticDatum, NonSemanticDatumTarget, NonSemanticDimension

class Annotation2(AnyObject):
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

    def z(self, value: float) -> 'Annotation2':
        self.annotation.Z = value
        return self

    def add_leader(self) -> 'Annotation2':
        self.annotation.AddLeader()
        return self


    def coordinated_dimension(self) -> CoordDim:
        return CoordDim(self.annotation.CoordinatedDimension())


    def datum_simple(self) -> DatumSimple:
        return DatumSimple(self.annotation.DatumSimple())


    def datum_target(self) -> DatumTarget:
        return DatumTarget(self.annotation.DatumTarget())

 
    def default_annotation(self) -> DefaultAnnotation:
        return DefaultAnnotation(self.annotation.DefaultAnnotation())


    def dimension_3d(self) -> Dimension3D:
        return Dimension3D(self.annotation.Dimension3D())


    def flag_note(self) -> FlagNote:
        return FlagNote(self.annotation.FlagNote())

    def get_geometrical_component_name(self, i_index: float) -> str:
        return self.annotation.GetGeometricalComponentName(i_index)

    def get_Nbr_of_geometrical_component(self) -> float:
        return self.annotation.GetNbrGeometricalComponent()

    def get_surfaces(self, o_safe_array: tuple) -> tuple:
        # return self.annotation.GetSurfaces(o_safe_array)
        return self.annotation.GetSurfaces()

    def get_surfaces_count(self) -> float:
        return self.annotation.GetSurfacesCount()

    def has_a_visualization_dimension(self) -> bool:
        return self.annotation.HasAVisualizationDimension()


    def hyper_link_manager(self) -> bool:
        return TPSHyperLinkManager(self.annotation.HyperLinkManager())

    def is_a_consumable_annotation(self) -> bool:
        return self.annotation.IsAConsumableAnnotation()

    def is_a_default_annotation(self) -> bool:
        return self.annotation.IsADefaultAnnotation()

    def modify_visualisation(self) -> 'Annotation2':
        self.annotation.ModifyVisu()
        return self


    def noa(self) -> Noa:
        return Noa(self.annotation.Noa())


    def non_semantic_datum(self) -> NonSemanticDatum:
        return NonSemanticDatum(self.annotation.NonSemanticDatum())


    def non_semantic_datum_target(self) -> NonSemanticDatumTarget:
        return NonSemanticDatumTarget(self.annotation.NonSemanticDatumTarget())


    def non_semantic_dimension(self) -> NonSemanticDimension:
        return NonSemanticDimension(self.annotation.NonSemanticDimension())


    def non_semantic_gdt(self) -> NonSemanticGDT:
        return NonSemanticGDT(self.annotation.NonSemanticGDT())


    def reference_frame(self) -> ReferenceFrame:
        return ReferenceFrame(self.annotation.ReferenceFrame())


    def roughness(self) -> Roughness:
        return Roughness(self.annotation.Roughness())


    def semantic_gdt(self) -> SemanticGDT:
        return SemanticGDT(self.annotation.SemanticGDT())

    def set_geometrical_component_name(self, i_index: float, i_new_name: str, i_check_name_unicity_option: bool) -> 'Annotation2':
        self.annotation.SetGeometricalComponentName(i_index, i_new_name, i_check_name_unicity_option)
        return self

    def set_xy(self, i_x: float, i_y: float) -> 'Annotation2':
        self.annotation.SetXY(i_x, i_y)
        return self

    def text(self) -> Text:
        return Text(self.annotation.Text())

    def transfert_to_view(self, i_view: TPSView) -> 'Annotation2':
        self.annotation.TransfertToView(i_view.com_object)
        return self

    def visualization_dimension(self) -> Dimension3D:
        return Dimension3D(self.annotation.VisualizationDimension())

    def weld(self) -> Weld:
        return Weld(self.annotation.Weld())