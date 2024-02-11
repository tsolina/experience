from experience.system.any_object import AnyObject

class PageSetup(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.page_setup = com

    def banner(self, value: str = None) -> str:
        if value is not None:
            self.page_setup.Banner = value
            return self
        return self.page_setup.Banner

    def banner_position(self, value: int = None) -> int:
        if value is not None:
            self.page_setup.BannerPosition = value
            return self
        return self.page_setup.BannerPosition

    def banner_size(self, value: float = None) -> float:
        if value is not None:
            self.page_setup.BannerSize = value
            return self
        return self.page_setup.BannerSize

    def bottom(self, value: float = None) -> float:
        if value is not None:
            self.page_setup.Bottom = value
            return self
        return self.page_setup.Bottom

    def bottom_margin(self, value: float = None) -> float:
        if value is not None:
            self.page_setup.BottomMargin = value
            return self
        return self.page_setup.BottomMargin

    def color(self, value: int = None) -> int:
        if value is not None:
            self.page_setup.Color = value
            return self
        return self.page_setup.Color

    def dpi(self, value: float = None) -> float:
        if value is not None:
            self.page_setup.Dpi = value
            return self
        return self.page_setup.Dpi

    def gamma(self, value: float = None) -> float:
        if value is not None:
            self.page_setup.Gamma = value
            return self
        return self.page_setup.Gamma

    def left(self, value: float = None) -> float:
        if value is not None:
            self.page_setup.Left = value
            return self
        return self.page_setup.Left

    def left_margin(self, value: float = None) -> float:
        if value is not None:
            self.page_setup.LeftMargin = value
            return self
        return self.page_setup.LeftMargin

    def line_cap(self, value: int = None) -> int:
        if value is not None:
            self.page_setup.LineCap = value
            return self
        return self.page_setup.LineCap

    def line_type_overlapping_check(self, value: bool = None) -> bool:
        if value is not None:
            self.page_setup.LineTypeOverlappingCheck = value
            return self
        return self.page_setup.LineTypeOverlappingCheck

    def line_type_specification(self, value: int = None) -> int:
        if value is not None:
            self.page_setup.LineTypeSpecification = value
            return self
        return self.page_setup.LineTypeSpecification

    def line_width_specification(self, value: int = None) -> int:
        if value is not None:
            self.page_setup.LineWidthSpecification = value
            return self
        return self.page_setup.LineWidthSpecification

    def logo(self, value: str = None) -> str:
        if value is not None:
            self.page_setup.Logo = value
            return self
        return self.page_setup.Logo

    def logo_visibility(self, value: bool = None) -> bool:
        if value is not None:
            self.page_setup.LogoVisibility = value
            return self
        return self.page_setup.LogoVisibility

    def maximum_size(self, value: bool = None) -> bool:
        if value is not None:
            self.page_setup.MaximumSize = value
            return self
        return self.page_setup.MaximumSize

    def orientation(self, value: int = None) -> int:
        if value is not None:
            self.page_setup.Orientation = value
            return self
        return self.page_setup.Orientation

    def paper_height(self, value: float = None) -> float:
        if value is not None:
            self.page_setup.PaperHeight = value
            return self
        return self.page_setup.PaperHeight

    def paper_size(self, value: int = None) -> int:
        if value is not None:
            self.page_setup.PaperSize = value
            return self
        return self.page_setup.PaperSize

    def paper_width(self, value: float = None) -> float:
        if value is not None:
            self.page_setup.PaperWidth = value
            return self
        return self.page_setup.PaperWidth

    def print_rendering_mode(self, value: int = None) -> int:
        if value is not None:
            self.page_setup.PrintRenderingMode = value
            return self
        return self.page_setup.PrintRenderingMode

    def quality(self, value: int = None) -> int:
        if value is not None:
            self.page_setup.Quality = value
            return self
        return self.page_setup.Quality

    def right_margin(self, value: float = None) -> float:
        if value is not None:
            self.page_setup.RightMargin = value
            return self
        return self.page_setup.RightMargin

    def rotation(self, value: float = None) -> int:
        if value is not None:
            self.page_setup.Rotation = value
            return self
        return self.page_setup.Rotation

    def scaling_1_to_1(self, value: bool = None) -> bool:
        if value is not None:
            self.page_setup.Scaling1To1 = value
            return self
        return self.page_setup.Scaling1To1

    def text_blanking(self, value: bool = None) -> bool:
        if value is not None:
            self.page_setup.TextBlanking = value
            return self
        return self.page_setup.TextBlanking

    def text_scaling(self, value: bool = None) -> bool:
        if value is not None:
            self.page_setup.TextScaling = value
            return self
        return self.page_setup.TextScaling

    def top_margin(self, value: float = None) -> float:
        if value is not None:
            self.page_setup.TopMargin = value
            return self
        return self.page_setup.TopMargin

    def use_3d_accuracy(self, value: bool = None) -> bool:
        if value is not None:
            self.page_setup.Use3DAccuracy = value
            return self
        return self.page_setup.Use3DAccuracy

    def use_image_size(self, value: bool = None) -> bool:
        if value is not None:
            self.page_setup.UseImageSize = value
            return self
        return self.page_setup.UseImageSize

    def white_vectors_in_black(self, value: bool = None) -> bool:
        if value is not None:
            self.page_setup.WhiteVectorsInBlack = value
            return self
        return self.page_setup.WhiteVectorsInBlack

    def zoom(self, value: float = None) -> float:
        if value is not None:
            self.page_setup.Zoom = value
            return self
        return self.page_setup.Zoom

    def __repr__(self):
        return f'PageSetup(name="{ self.name()}")'
