from typing import Union, TYPE_CHECKING

from experience.drafting_2d_interfaces.drafting_2d_types import CatVisuIn3DMode
from experience.drafting_interfaces.drafting_types import CatSheetProjectionMethod
from experience.inf_interfaces.inf_types import CatPaperOrientation, CatPaperSize, CatRenderingMode
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.drafting_interfaces import DrawingPageSetup, PrintArea
    from experience.drafting_2d_interfaces.layout_2d_views import Layout2DViews

class Layout2DSheet(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Layout2DSheet
    """

    def __init__(self, com):
        super().__init__(com)
        self.layout_2d_sheet = com

    def orientation(self, value: CatPaperOrientation = None) -> Union['Layout2DSheet', CatPaperOrientation]:
        if value is not None:
            self.layout_2d_sheet.Orientation = int(value)
            return self
        return CatPaperOrientation.item(self.layout_2d_sheet.Orientation)
        
    def page_setup(self) -> 'DrawingPageSetup':
        from experience.drafting_interfaces.drawing_page_setup import DrawingPageSetup
        return DrawingPageSetup(self.layout_2d_sheet.PageSetup)
    
    def paper_height(self, value: float = None) -> Union['Layout2DSheet', float]:
        if value is not None:
            self.layout_2d_sheet.PaperHeight = value
            return self
        return self.layout_2d_sheet.PaperHeight
    
    def paper_name(self, value: str = None) -> Union['Layout2DSheet', str]:
        if value is not None:
            self.layout_2d_sheet.PaperName = value
            return self
        return self.layout_2d_sheet.PaperName
    
    def paper_size(self, value: CatPaperSize = None) -> Union['Layout2DSheet', CatPaperSize]:
        if value is not None:
            self.layout_2d_sheet.PaperSize = int(value)
            return self
        return CatPaperSize.item(self.layout_2d_sheet.PaperSize)
    
    def paper_width(self, value: float = None) -> Union['Layout2DSheet', float]:
        if value is not None:
            self.layout_2d_sheet.PaperWidth = value
            return self
        return self.layout_2d_sheet.PaperWidth
    
    def print_area(self, value: 'PrintArea' = None) -> Union['Layout2DSheet', 'PrintArea']:
        if value is not None:
            self.layout_2d_sheet.PrintArea = value._com
            return self
        from experience.drafting_interfaces.print_area import PrintArea
        return PrintArea(self.layout_2d_sheet.PrintArea)
    
    def projection_method(self, value: CatSheetProjectionMethod = None) -> Union['Layout2DSheet', CatSheetProjectionMethod]:
        if value is not None:
            self.layout_2d_sheet.ProjectionMethod = int(value)
            return self
        return CatSheetProjectionMethod.item(self.layout_2d_sheet.ProjectionMethod)
    
    def sheet_scale(self, value: float = None) -> Union['Layout2DSheet', float]:
        if value is not None:
            self.layout_2d_sheet.SheetScale = value
            return self
        return self.layout_2d_sheet.SheetScale
    
    def sheet_style(self, i_sheet_style_name: str) -> 'Layout2DSheet':
        self.layout_2d_sheet.SheetStyle(i_sheet_style_name)
        return self
    
    def views(self) -> 'Layout2DViews':
        from experience.drafting_2d_interfaces.layout_2d_views import Layout2DViews
        return Layout2DViews(self.layout_2d_sheet.Views)
    
    def visu_in_3d(self, value: CatVisuIn3DMode = None) -> Union['Layout2DSheet', CatVisuIn3DMode]:
        if value is not None:
            self.layout_2d_sheet.VisuIn3D = int(value)
            return self
        return CatVisuIn3DMode.item(self.layout_2d_sheet.VisuIn3D)
    
    def activate(self) -> 'Layout2DSheet':
        self.layout_2d_sheet.Activate()
        return self
    
    def is_detail(self) -> bool:
        return self.layout_2d_sheet.IsDetail()

    def print_out(self, i_rendering_mode: CatRenderingMode) -> 'Layout2DSheet':
        self.layout_2d_sheet.PrintOut(int(i_rendering_mode))
        return self
    
    def print_out2(self) -> 'Layout2DSheet':
        self.layout_2d_sheet.PrintOut2()
        return self
    
    def print_to_file(self, file_name: str, i_rendering_mode: CatRenderingMode) -> 'Layout2DSheet':
        self.layout_2d_sheet.PrintToFile(file_name, i_rendering_mode)
        return self
    
    def print_to_file2(self, file_name: str) -> 'Layout2DSheet':
        self.layout_2d_sheet.PrintToFile2(file_name)
        return self
    
    def reorder_views(self, i_ordered_views: list) -> 'Layout2DSheet':
        self.layout_2d_sheet.reorder_Views(i_ordered_views)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
