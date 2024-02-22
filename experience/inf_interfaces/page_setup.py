from typing import Union
from experience.system.any_object import AnyObject

from experience.inf_interfaces.inf_types import *

class PageSetup(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.page_setup = com

    def banner(self, value: str = None) -> Union['PageSetup', str]:
        if value is not None:
            self.page_setup.Banner = value
            return self
        return self.page_setup.Banner

    def banner_position(self, value: CatBannerPosition = None) -> Union['PageSetup', CatBannerPosition]:
        if value is not None:
            self.page_setup.BannerPosition = int(value)
            return self
        return CatBannerPosition.item(self.page_setup.BannerPosition)

    def banner_size(self, value: float = None) -> Union['PageSetup', float]:
        if value is not None:
            self.page_setup.BannerSize = value
            return self
        return self.page_setup.BannerSize

    def bottom(self, value: float = None) -> Union['PageSetup', float]:
        if value is not None:
            self.page_setup.Bottom = value
            return self
        return self.page_setup.Bottom

    def bottom_margin(self, value: float = None) -> Union['PageSetup', float]:
        if value is not None:
            self.page_setup.BottomMargin = value
            return self
        return self.page_setup.BottomMargin

    def color(self, value: CatPrintColor = None) -> Union['PageSetup', CatPrintColor]:
        if value is not None:
            self.page_setup.Color = int(value)
            return self
        return CatPrintColor.item(self.page_setup.Color)

    def dpi(self, value: float = None) -> Union['PageSetup', float]:
        if value is not None:
            self.page_setup.Dpi = value
            return self
        return self.page_setup.Dpi

    def gamma(self, value: float = None) -> Union['PageSetup', float]:
        if value is not None:
            self.page_setup.Gamma = value
            return self
        return self.page_setup.Gamma

    def left(self, value: float = None) -> Union['PageSetup', float]:
        if value is not None:
            self.page_setup.Left = value
            return self
        return self.page_setup.Left

    def left_margin(self, value: float = None) -> Union['PageSetup', float]:
        if value is not None:
            self.page_setup.LeftMargin = value
            return self
        return self.page_setup.LeftMargin

    def line_cap(self, value: CatPrintLineCap = None) -> Union['PageSetup', CatPrintLineCap]:
        if value is not None:
            self.page_setup.LineCap = int(value)
            return self
        return CatPrintLineCap.item(self.page_setup.LineCap)

    def line_type_overlapping_check(self, value: bool = None) -> Union['PageSetup', bool]:
        if value is not None:
            self.page_setup.LineTypeOverlappingCheck = value
            return self
        return self.page_setup.LineTypeOverlappingCheck

    def line_type_specification(self, value: CatPrintLineSpecification = None) -> Union['PageSetup', CatPrintLineSpecification]:
        if value is not None:
            self.page_setup.LineTypeSpecification = int(value)
            return self
        return CatPrintLineSpecification.item(self.page_setup.LineTypeSpecification)

    def line_width_specification(self, value: CatPrintLineSpecification = None) -> Union['PageSetup', CatPrintLineSpecification]:
        if value is not None:
            self.page_setup.LineWidthSpecification = value
            return self
        return self.page_setup.LineWidthSpecification

    def logo(self, value: str = None) -> Union['PageSetup', str]:
        if value is not None:
            self.page_setup.Logo = value
            return self
        return self.page_setup.Logo

    def logo_visibility(self, value: bool = None) -> Union['PageSetup', bool]:
        if value is not None:
            self.page_setup.LogoVisibility = value
            return self
        return self.page_setup.LogoVisibility

    def maximum_size(self, value: bool = None) -> Union['PageSetup', bool]:
        if value is not None:
            self.page_setup.MaximumSize = value
            return self
        return self.page_setup.MaximumSize

    def orientation(self, value: CatPaperOrientation = None) -> Union['PageSetup', CatPaperOrientation]:
        if value is not None:
            self.page_setup.Orientation = int(value)
            return self
        return CatPaperOrientation.item(self.page_setup.Orientation)

    def paper_height(self, value: float = None) -> Union['PageSetup', float]:
        if value is not None:
            self.page_setup.PaperHeight = value
            return self
        return self.page_setup.PaperHeight

    def paper_size(self, value: CatPaperSize = None) -> Union['PageSetup', CatPaperSize]:
        if value is not None:
            self.page_setup.PaperSize = int(value)
            return self
        return CatPaperSize.item(self.page_setup.PaperSize)

    def paper_width(self, value: float = None) -> Union['PageSetup', float]:
        if value is not None:
            self.page_setup.PaperWidth = value
            return self
        return self.page_setup.PaperWidth

    def print_rendering_mode(self, value: CatPrintRenderingMode = None) -> Union['PageSetup', CatPrintRenderingMode]:
        if value is not None:
            self.page_setup.PrintRenderingMode = int(value)
            return self
        return CatPrintRenderingMode.item(self.page_setup.PrintRenderingMode)

    def quality(self, value: CatPrintQuality = None) -> Union['PageSetup', CatPrintQuality]:
        if value is not None:
            self.page_setup.Quality = int(value)
            return self
        return CatPrintQuality.item(self.page_setup.Quality)

    def right_margin(self, value: float = None) -> Union['PageSetup', float]:
        if value is not None:
            self.page_setup.RightMargin = value
            return self
        return self.page_setup.RightMargin

    def rotation(self, value: CatImageRotation = None) -> Union['PageSetup', CatImageRotation]:
        if value is not None:
            self.page_setup.Rotation = int(value)
            return self
        return CatImageRotation.item(self.page_setup.Rotation)

    def scaling_1_to_1(self, value: bool = None) -> Union['PageSetup', bool]:
        if value is not None:
            self.page_setup.Scaling1To1 = value
            return self
        return self.page_setup.Scaling1To1

    def text_blanking(self, value: bool = None) -> Union['PageSetup', bool]:
        if value is not None:
            self.page_setup.TextBlanking = value
            return self
        return self.page_setup.TextBlanking

    def text_scaling(self, value: bool = None) -> Union['PageSetup', bool]:
        if value is not None:
            self.page_setup.TextScaling = value
            return self
        return self.page_setup.TextScaling

    def top_margin(self, value: float = None) -> Union['PageSetup', float]:
        if value is not None:
            self.page_setup.TopMargin = value
            return self
        return self.page_setup.TopMargin

    def use_3d_accuracy(self, value: bool = None) -> Union['PageSetup', bool]:
        if value is not None:
            self.page_setup.Use3DAccuracy = value
            return self
        return self.page_setup.Use3DAccuracy

    def use_image_size(self, value: bool = None) -> Union['PageSetup', bool]:
        if value is not None:
            self.page_setup.UseImageSize = value
            return self
        return self.page_setup.UseImageSize

    def white_vectors_in_black(self, value: bool = None) -> Union['PageSetup', bool]:
        if value is not None:
            self.page_setup.WhiteVectorsInBlack = value
            return self
        return self.page_setup.WhiteVectorsInBlack

    def zoom(self, value: float = None) -> Union['PageSetup', float]:
        if value is not None:
            self.page_setup.Zoom = value
            return self
        return self.page_setup.Zoom

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'