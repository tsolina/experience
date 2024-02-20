from typing import Union
from experience.system import AnyObject
from experience.cat_annotation_interfaces.annotation_types import *

class DrawingTextProperties(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 DrawingTextProperties
    """

    def __init__(self, com):
        super().__init__()
        self.drawing_text_properties = com

    def anchor_point(self, value: CatTextAnchorPosition = None) -> Union['DrawingTextProperties', CatTextAnchorPosition]:
        if value is not None:
            self.drawing_text_properties.AnchorPoint = int(value)
            return self
        return CatTextAnchorPosition.item(self.drawing_text_properties.AnchorPoint)

    def blanking(self, value: CatBlankingMode = None) ->  Union['DrawingTextProperties', CatBlankingMode]:
        if value is not None:
            self.drawing_text_properties.Blanking = int(value)
            return self
        return CatBlankingMode.item(self.drawing_text_properties.Blanking)

    def bold(self, value: int = None) ->  Union['DrawingTextProperties', int]:
        if value is not None:
            self.drawing_text_properties.Bold = value
            return self
        return self.drawing_text_properties.Bold

    def color(self, value: int = None) ->  Union['DrawingTextProperties', int]:
        if value is not None:
            self.drawing_text_properties.Color = value
            return self
        return self.drawing_text_properties.Color

    def font_name(self, value: str = None) ->  Union['DrawingTextProperties', str]:
        if value is not None:
            self.drawing_text_properties.FontName = value
            return self
        return self.drawing_text_properties.FontName

    def font_size(self, value: float = None) ->  Union['DrawingTextProperties', float]:
        if value is not None:
            self.drawing_text_properties.FontSize = value
            return self
        return self.drawing_text_properties.FontSize

    def frame_type(self, value: CatTextFrameType = None) ->  Union['DrawingTextProperties', CatTextFrameType]:
        if value is not None:
            self.drawing_text_properties.FrameType = int(value)
            return self
        return CatTextFrameType.item(self.drawing_text_properties.FrameType)

    def italic(self, value: int = None) ->  Union['DrawingTextProperties', int]:
        if value is not None:
            self.drawing_text_properties.Italic = value
            return self
        return self.drawing_text_properties.Italic

    def justification(self, value: CatJustification = None) ->  Union['DrawingTextProperties', CatJustification]:
        if value is not None:
            self.drawing_text_properties.Justification = int(value)
            return self
        return CatJustification.item(self.drawing_text_properties.Justification)

    def kerning(self, value: int = None) ->  Union['DrawingTextProperties', int]:
        if value is not None:
            self.drawing_text_properties.Kerning = value
            return self
        return self.drawing_text_properties.Kerning

    def mirror(self, value: CatTextFlipMode = None) ->  Union['DrawingTextProperties', CatTextFlipMode]:
        if value is not None:
            self.drawing_text_properties.Mirror = int(value)
            return self
        return CatTextFlipMode.item(self.drawing_text_properties.Mirror)

    def overline(self, value: int = None) ->  Union['DrawingTextProperties', int]:
        if value is not None:
            self.drawing_text_properties.Overline = value
            return self
        return self.drawing_text_properties.Overline

    def strike_thru(self, value: int = None) ->  Union['DrawingTextProperties', int]:
        if value is not None:
            self.drawing_text_properties.StrikeThru = value
            return self
        return self.drawing_text_properties.StrikeThru

    def subscript(self, value: int = None) ->  Union['DrawingTextProperties', int]:
        if value is not None:
            self.drawing_text_properties.Subscript = value
            return self
        return self.drawing_text_properties.Subscript

    def superscript(self, value: int = None) ->  Union['DrawingTextProperties', int]:
        if value is not None:
            self.drawing_text_properties.Superscript = value
            return self
        return self.drawing_text_properties.Superscript

    def underline(self, value: int = None) -> Union['DrawingTextProperties', int]:
        if value is not None:
            self.drawing_text_properties.Underline = value
            return self
        return self.drawing_text_properties.Underline

    def activate_frame(self, i_type: CatTextFrameType) -> 'DrawingTextProperties':
        self.drawing_text_properties.ActivateFrame(int(i_type))
        return self

    def update(self) -> 'DrawingTextProperties':
        self.drawing_text_properties.Update()
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
