import os
from pathlib import Path
from typing import TYPE_CHECKING

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.drafting_interfaces import DrawingPageSetup, DrawingView, DrawingViews, PrintArea

class DrawingSheet(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingSheet
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_sheet = com

    def gen_views_pos_mode(self, value: int = None) -> int:
        if value is not None:
            self.drawing_sheet.GenViewsPosMode = value
            return self
        return self.drawing_sheet.GenViewsPosMode

    def orientation(self, value: int = None) -> int:
        """
        enum CatPaperOrientation {
        catPaperPortrait,
        catPaperLandscape,
        catPaperBestFit
        } 
        """
        if value is not None:
            self.drawing_sheet.Orientation = value
            return self
        return self.drawing_sheet.Orientation


    def page_setup(self) -> 'DrawingPageSetup':
        from experience.drafting_interfaces import DrawingPageSetup
        return DrawingPageSetup(self.drawing_sheet.PageSetup)

    def paper_size(self, value: int = None) -> int:
        """
        enum CatPaperSize {
        catPaperLetter,
        catPaperLegal,
        catPaperA0,
        catPaperA1,
        catPaperA2,
        catPaperA3,
        catPaperA4,
        catPaperA,
        catPaperB,
        catPaperC,
        catPaperD,
        catPaperE,
        catPaperF,
        catPaperUser
        } 
        """
        if value is not None:
            self.drawing_sheet.PaperSize = value
            return self
        return self.drawing_sheet.PaperSize


    def print_area(self) -> 'PrintArea':
        from experience.drafting_interfaces import PrintArea
        return PrintArea(self.drawing_sheet.PrintArea)

    def projection_method(self, value: int = None) -> int:
        """
        enum CatSheetProjectionMethod {
        catFirstAngle,
        catThirdAngle
        } 
        """
        if value is not None:
            self.drawing_sheet.ProjectionMethod = value
            return self
        return self.drawing_sheet.ProjectionMethod

    def scale(self, value: float = None) -> float:
        if value is not None:
            self.drawing_sheet.Scale = value
            return self
        return self.drawing_sheet.Scale

    def scale2(self, value: float = None) -> float:
        if value is not None:
            self.drawing_sheet.Scale2 = value
            return self
        return self.drawing_sheet.Scale2

    def sheet_style(self, i_sheet_style_name: str) -> 'DrawingSheet':
        self.drawing_sheet.SheetStyle(i_sheet_style_name)
        return self


    def views(self) -> 'DrawingViews':
        from experience.drafting_interfaces import DrawingViews
        return DrawingViews(self.drawing_sheet.Views)
    
    def active_view(self) -> 'DrawingView':
        from experience.drafting_interfaces import DrawingView
        return self.views().active_view()

    def activate(self) -> 'DrawingSheet':
        self.drawing_sheet.Activate()
        return self

    def force_update(self) -> 'DrawingSheet':
        self.drawing_sheet.ForceUpdate()
        return self

    def generate_dimensions(self) -> 'DrawingSheet':
        self.drawing_sheet.GenerateDimensions()
        return self

    def get_paper_height(self) -> float:
        return self.drawing_sheet.GetPaperHeight()

    def get_paper_width(self) -> float:
        return self.drawing_sheet.GetPaperWidth()

    def is_detail(self) -> bool:
        return self.drawing_sheet.IsDetail()

    def isolate(self) -> 'DrawingSheet':
        self.drawing_sheet.Isolate()
        return self

    def print_out(self) -> 'DrawingSheet':
        self.drawing_sheet.PrintOut()
        return self

    def print_to_file(self, file_name: Path, overwrite=False) -> 'DrawingSheet':
        if not isinstance(file_name, Path):
            file_name = Path(file_name)

        if str(file_name.parent) == '.':
            self.logger.warning('Full path to print file expected. Assuming current working directory.')
            file_name = Path(os.getcwd(), file_name)

        if not file_name.parent.is_dir():
            raise NotADirectoryError(f'Directory {file_name.parent} is not a directory.')

        if overwrite is False and file_name.is_file():
            raise FileExistsError(f'File: {file_name} already exists. '
                                  f'Set overwrite=True if you want to overwrite.')

        # pycatia prefers full path names :-)
        if not file_name.is_absolute():
            self.logger.warning('To prevent unexpected behaviour, be explicit and use absolute filenames.')

        self.drawing_sheet.PrintToFile(file_name)
        return self

    def set_as_detail(self) -> 'DrawingSheet':
        self.drawing_sheet.SetAsDetail()
        return self

    def set_paper_height(self, o_paper_height: float) -> 'DrawingSheet':
        self.drawing_sheet.SetPaperHeight(o_paper_height)
        return self

    def set_paper_width(self, o_paper_width: float) -> 'DrawingSheet':
        self.drawing_sheet.SetPaperWidth(o_paper_width)
        return self

    def update(self) -> 'DrawingSheet':
        self.drawing_sheet.Update()
        return self

    def reorder_views(self, i_ordered_views: tuple) -> 'DrawingSheet':
        self.drawing_sheet.reorder_Views(i_ordered_views)
        return self

    def __repr__(self):
        return f'DrawingSheet(name="{self.name()}")'
