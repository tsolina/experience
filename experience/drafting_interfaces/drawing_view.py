from typing import TYPE_CHECKING, Union

from experience.system import AnyObject
from experience.drafting_interfaces.drafting_types import *
from experience.drafting_interfaces import DrawingAreaFills, DrawingComponents, DrawingPictures, DrawingThreads
from experience.cat_annotation_interfaces import DrawingArrows, DrawingCoordDims, DrawingDimensions, DrawingTables, DrawingText, DrawingTexts, DrawingWeldings, DrawingGDTs

if TYPE_CHECKING:
    from experience.cat_sketcher_interfaces import Factory2D
    from experience.cat_annotation_interfaces import DrawingText
    from experience.mecmod_interfaces import GeometricElements
    from experience.product_structure_client_interfaces import VPMReference
    from experience.drafting_interfaces import DrawingGenView

class DrawingView(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingView
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_view = com

    def angle(self, value: float = None) -> Union['DrawingView', float]:
        if value is not None:
            self.drawing_view.Angle = value
            return self
        return self.drawing_view.Angle


    def area_fills(self) -> DrawingAreaFills:
        return DrawingAreaFills(self.drawing_view.DrawingAreaFills)


    def arrows(self) -> DrawingArrows:
        return DrawingArrows(self.drawing_view.Arrows)


    def components(self) -> DrawingComponents:
        return DrawingComponents(self.drawing_view.Components)


    def coord_dims(self) -> DrawingCoordDims:
        return DrawingCoordDims(self.drawing_view.DrawingCoordDims)


    def dimensions(self) -> DrawingDimensions:
        return DrawingDimensions(self.drawing_view.Dimensions)


    def drawing_gen_view(self) -> 'DrawingGenView':
        from experience.drafting_interfaces import DrawingGenView
        return AnyObject(self.drawing_view.DrawingGenView).as_pyclass(DrawingGenView)

#vpm_ref = VPMReference(sheet.views().item(3).drawing_gen_view()._com.GetAssociatedRootProduct())
    # def get_associated_root_product(self) -> 'VPMReference':
    #     from experience.product_structure_client_interfaces import VPMReference
    #     return VPMReference(self.drawing_gen_view()._com.GetAssociatedRootProduct())
    #     #return VPMReference(self.drawing_view.DrawingGenView.GetAssociatedRootProduct())

    def factory_2d(self) -> 'Factory2D':
        from experience.cat_sketcher_interfaces import Factory2D
        return Factory2D(self.drawing_view.Factory2D)

    def frame_visualization(self, value: bool = None) -> Union['DrawingView', bool]:
        if value is not None:
            self.drawing_view.FrameVisualization = value
            return self
        return self.drawing_view.FrameVisualization

    # @property
    # def generative_behavior(self) -> DrawingViewGenerativeBehavior:
    #     return DrawingViewGenerativeBehavior(self.drawing_view.GenerativeBehavior)

    # @property
    # def generative_links(self) -> DrawingViewGenerativeLinks:
    #     return DrawingViewGenerativeLinks(self.drawing_view.GenerativeLinks)


    def gdts(self) -> DrawingGDTs:
        return self.drawing_view.GDTs


    def geometric_elements(self) -> 'GeometricElements':
        from experience.mecmod_interfaces import GeometricElements
        return GeometricElements(self.drawing_view.GeometricElements)

    def is_relation_activated(self) -> bool:
        return self.drawing_view.IsRelationActivated

    def lock_status(self, value: bool = None) -> Union['DrawingView', bool]:
        if value is not None:
            self.drawing_view.LockStatus = value
            return self
        return self.drawing_view.LockStatus


    def pictures(self) -> DrawingPictures:
        return DrawingPictures(self.drawing_view.Pictures)

    def reference_view(self, value: 'DrawingView' = None) -> 'DrawingView':
        if value is not None:
            self.drawing_view.ReferenceView = value
            return self
        return DrawingView(self.drawing_view.ReferenceView)

    def scale(self, value: float = None) -> Union['DrawingView', float]:
        if value is not None:
            self.drawing_view.Scale = value
            return self
        return self.drawing_view.Scale

    def scale2(self, value: float = None) -> Union['DrawingView', float]:
        if value is not None:
            self.drawing_view.Scale2 = value
            return self
        return self.drawing_view.Scale2


    def tables(self) -> DrawingTables:
        return DrawingTables(self.drawing_view.Tables)


    def texts(self) -> DrawingTexts:
        return DrawingTexts(self.drawing_view.Texts)


    def threads(self) -> DrawingThreads:
        return DrawingThreads(self.drawing_view.Threads)

    def view_type(self) -> CatDrawingViewType:
        return CatDrawingViewType.item(self.drawing_view.ViewType)


    def weldings(self) -> DrawingWeldings:
        return DrawingWeldings(self.drawing_view.Weldings)

    def x(self, value: float = None) -> Union['DrawingView', float]:
        if value is not None:
            self.drawing_view.x = value
            return self
        return self.drawing_view.x

    def x_axis_data(self, value: float = None) -> Union['DrawingView', float]:
        if value is not None:
            self.drawing_view.xAxisData = value
            return self
        return self.drawing_view.xAxisData

    def y(self, value: float = None) -> Union['DrawingView', float]:
        if value is not None:
            self.drawing_view.y = value
            return self
        return self.drawing_view.y

    def y_axis_data(self, value: float = None) -> Union['DrawingView', float]:
        if value is not None:
            self.drawing_view.yAxisData = value
            return self
        return self.drawing_view.yAxisData

    def activate(self) -> 'DrawingView':
        self.drawing_view.Activate()
        return self

    def add_view_text(self) -> 'DrawingText':
        return DrawingText(self.drawing_view.Activate())

    def aligned_with_reference_view(self) -> 'DrawingView':
        self.drawing_view.AlignedWithReferenceView()
        return self

    # def get_projection_plane(self, o_x_1: float, o_y_1: float, o_z_1: float, o_x_2: float, o_y_2: float, o_z_2: float) -> tuple:
    #     return self.drawing_view.GetProjectionPlane(o_x_1, o_y_1, o_z_1, o_x_2, o_y_2, o_z_2)
    def get_projection_plane(self) -> tuple[float, float, float, float, float, float]:
        return self._get_multi([self.drawing_view], ('DrawingView', 'GetProjectionPlane'), ('Double', 'Double', 'Double', 'Double', 'Double', 'Double'))
    
    # def get_view_name(self, i_view_name_prefix: str, i_view_name_ident: str, i_view_name_suffix: str) -> tuple:
    #     return self.drawing_view.GetViewName(i_view_name_prefix, i_view_name_ident, i_view_name_suffix)
    def get_view_name(self) -> tuple[str, str, str]:
        return self._get_multi([self.drawing_view], ('DrawingView', 'GetViewName'), ('str', 'str', 'str'))

    def get_view_text(self) -> 'DrawingText':
        return DrawingText(self.drawing_view.DravingText())

    def insert_view_angle(self, i_first: int, io_text: 'DrawingText') -> tuple:
        return self.drawing_view.InsertViewAngle(i_first, io_text.com_object)

    def insert_view_scale(self, i_first: int, io_text: 'DrawingText') -> tuple:
        return self.drawing_view.InsertViewScale(i_first, io_text.com_object)

    def is_generative(self) -> bool:
        return self.drawing_view.IsGenerative()

    def isolate(self) -> 'DrawingView':
        self.drawing_view.Isolate()
        return self

    def save_edition(self) -> 'DrawingView':
        self.drawing_view.SaveEdition()
        return self

    def set_projection_plane(self, i_x_1: float, i_y_1: float, i_z_1: float, i_x_2: float, i_y_2: float, i_z_2: float) -> 'DrawingView':
        self.drawing_view.SetProjectionPlane(i_x_1, i_y_1, i_z_1, i_x_2, i_y_2, i_z_2)
        return self

    def set_view_name(self, i_view_name_prefix: str, i_view_name_ident: str, i_view_name_suffix: str) -> 'DrawingView':
        self.drawing_view.SetViewName(i_view_name_prefix, i_view_name_ident, i_view_name_suffix)
        return self

    def size(self) -> tuple[float, float, float, float]:

        vba_function_name = "size"
        vba_code = """
        Public Function size(drawing_view)
            Dim oXY(4)
            drawing_view.Size oXY
            size = oXY
        End Function
        """

        system_service = self.application.system_service
        value = system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

        # we don't return value directly as CATIA returns for example
        # "(-15.0, 30.0, -15.0, 30.0, None)" I don't know what the additional
        # value None at the end represents.
        return value[0], value[1], value[2], value[3]

    def un_aligned_with_reference_view(self) -> 'DrawingView':
        self.drawing_view.UnAlignedWithReferenceView()
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
