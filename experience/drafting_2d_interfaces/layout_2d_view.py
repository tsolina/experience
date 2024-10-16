from typing import Union, TYPE_CHECKING

from experience.drafting_2d_interfaces.drafting_2d_types import CatView2DModeVisu, CatVisuBackgroundMode, CatVisuIn3DMode
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.drafting_interfaces import DrawingAreaFills, DrawingComponents, DrawingPictures, DrawingThreads
    from experience.cat_annotation_interfaces import DrawingArrows, DrawingCoordDims, DrawingDimensions, DrawingGDTs, DrawingTables, DrawingTexts, DrawingWeldings
    from experience.cat_annotation_interfaces.drawing_text import DrawingText
    from experience.cat_sketcher_interfaces.factory_2d import Factory2D
    from experience.mecmod_interfaces.geometric_elements import GeometricElements

class Layout2DView(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Layout2DView
    """

    def __init__(self, com):
        super().__init__(com)
        self.layout_2d_view = com

    def angle(self, value: float = None) -> Union['Layout2DView', float]:
        if value is not None:
            self.layout_2d_view.Angle = value
            return self
        return self.layout_2d_view.Angle
    
    def area_fills(self) -> 'DrawingAreaFills':
        from experience.drafting_interfaces.drawing_area_fills import DrawingAreaFills
        return DrawingAreaFills(self.layout_2d_view.AreaFills)
    
    def arrows(self) -> 'DrawingArrows':
        from experience.cat_annotation_interfaces.drawing_arrows import DrawingArrows
        return DrawingArrows(self.layout_2d_view.Arrows)
    
    def components(self) -> 'DrawingComponents':
        from experience.drafting_interfaces.drawing_components import DrawingComponents
        return DrawingComponents(self.layout_2d_view.Components)
    
    def coord_dims(self) -> 'DrawingCoordDims':
        from experience.cat_annotation_interfaces.drawing_coord_dims import DrawingCoordDims
        return DrawingCoordDims(self.layout_2d_view.CoordDims)
    
    def dimensions(self) -> 'DrawingDimensions':
        from experience.cat_annotation_interfaces.drawing_dimensions import DrawingDimensions
        return DrawingDimensions(self.layout_2d_view.Dimensions)
    
    def factory_2d(self) -> 'Factory2D':
        from experience.cat_sketcher_interfaces.factory_2d import Factory2D
        return Factory2D(self.layout_2d_view.Factory2D)
    
    def frame_visualization(self, value: bool = None) -> Union['Layout2DView', bool]:
        if value is not None:
            self.layout_2d_view.FrameVisualization = value
            return self
        return self.layout_2d_view.FrameVisualization
    
    def gdts(self) -> 'DrawingGDTs':
        from experience.cat_annotation_interfaces.drawing_gdts import DrawingGDTs
        return DrawingGDTs(self.layout_2d_view.GDTs)
    
    def geometric_elements(self) -> 'GeometricElements':
        from experience.mecmod_interfaces.geometric_elements import GeometricElements
        return GeometricElements(self.layout_2d_view.GeometricElements)
    
    def is_relation_activated(self) -> bool:
        return self.layout_2d_view.IsRelationActivated
    
    def lock_status(self, value: bool = None) -> Union['Layout2DView', bool]:
        if value is not None:
            self.layout_2d_view.LockStatus = value
            return self
        return self.layout_2d_view.LockStatus
    
    def pictures(self) -> 'DrawingPictures':
        from experience.drafting_interfaces.drawing_pictures import DrawingPictures
        return DrawingPictures(self.layout_2d_view.Pictures)
    
    def reference_view(self, value: 'Layout2DView' = None) -> 'Layout2DView':
        if value is not None:
            self.layout_2d_view.ReferenceView = value._com
            return self
        return Layout2DView(self.layout_2d_view.ReferenceView)
    
    def tables(self) -> 'DrawingTables':
        from experience.cat_annotation_interfaces.drawing_tables import DrawingTables
        return DrawingTables(self.layout_2d_view.Tables)
    
    def texts(self) -> 'DrawingTexts':
        from experience.cat_annotation_interfaces.drawing_texts import DrawingTexts
        return DrawingTexts(self.layout_2d_view.Texts)
    
    def threads(self) -> 'DrawingThreads':
        from experience.drafting_interfaces.drawing_threads import DrawingThreads
        return DrawingThreads(self.layout_2d_view.Threads)
    
    def view_scale(self, value: float = None) -> Union['Layout2DView', float]:
        if value is not None:
            self.layout_2d_view.ViewScale = value
            return self
        return self.layout_2d_view.ViewScale
    
    def visu_2d_mode(self, value: CatView2DModeVisu = None) -> Union['Layout2DView', CatView2DModeVisu]:
        if value is not None:
            self.layout_2d_view.Visu2DMode = int(value)
            return self
        return CatView2DModeVisu.item(self.layout_2d_view.Visu2DMode)
    
    def visu_background(self, value: CatVisuBackgroundMode = None) -> Union['Layout2DView', CatVisuBackgroundMode]:
        if value is not None:
            self.layout_2d_view.VisuBackground = int(value)
            return self
        return CatVisuBackgroundMode.item(self.layout_2d_view.VisuBackground)
    
    def visu_in_3d(self, value: CatVisuIn3DMode = None) -> Union['Layout2DView', CatVisuIn3DMode]:
        if value is not None:
            self.layout_2d_view.VisuIn3D = int(value)
            return self
        return CatVisuIn3DMode.item(self.layout_2d_view.VisuIn3D)
    
    def weldings(self) -> 'DrawingWeldings':
        from experience.cat_annotation_interfaces.drawing_weldings import DrawingWeldings
        return DrawingWeldings(self.layout_2d_view.Weldings)
    
    def x(self, value: float = None) -> Union['Layout2DView', float]:
        if value is not None:
            self.layout_2d_view.x = value
            return self
        return self.layout_2d_view.x
    
    def y(self, value: float = None) -> Union['Layout2DView', float]:
        if value is not None:
            self.layout_2d_view.y = value
            return self
        return self.layout_2d_view.y
    
    def activate(self) -> 'Layout2DView':
        self.layout_2d_view.Activate()
        return self
    
    def add_view_text(self) -> 'DrawingText':
        from experience.cat_annotation_interfaces.drawing_text import DrawingText
        return DrawingText(self.layout_2d_view.AddViewText())
    
    def aligned_with_reference_view(self) -> 'Layout2DView':
        self.layout_2d_view.AlignedWithReferenceView()
        return self
    
    def get_reference_plane(self) -> tuple:
        #to test if this return is enough
        return self.layout_2d_view.GetReferencePlane()
    
    def get_view_name(self) -> tuple[str, str, str]:
        '''
        prefix, ident, suffix
        '''
        return self._get_multi([self.layout_2d_view], ("Layout2DView", "GetViewName"), ("String", "String", "String"))
    
    def get_view_text(self) -> 'DrawingText':
        from experience.cat_annotation_interfaces.drawing_text import DrawingText
        return DrawingText(self.layout_2d_view.GetViewText())
    
    def invert_reference_plane_definition(self) -> 'Layout2DView':
        self.layout_2d_view.InvertReferencePlaneDefinition()
        return self
    
    def is_reference_plane_inverted(self) -> bool:
        return self.layout_2d_view.IsReferencePlaneInverted()
    
    def save_edition(self) -> 'Layout2DView':
        self.layout_2d_view.SaveEdition()
        return self
    
    def set_reference_plane(self, i_ref_path: list, i_context_path: list) -> 'Layout2DView':
        self.layout_2d_view.SetReferencePlane(i_ref_path, i_context_path)
        return self

    def set_view_name(self, i_view_name_prefix: str, i_view_name_ident: str, i_view_name_suffix: str) -> 'Layout2DView':
        self.layout_2d_view.SetViewName(i_view_name_prefix, i_view_name_ident, i_view_name_suffix)
        return self
    
    def size(self) -> tuple[float, float, float, float]:
        '''
        xmin, xmax, ymin, ymax
        '''
        return self._get_safe_array(self.layout_2d_view, "Size", 3)
    
    def unaligned_with_reference_view(self) -> 'Layout2DView':
        self.layout_2d_view.UnAlignedWithReferenceView()
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'