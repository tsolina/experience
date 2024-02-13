from typing import Union
from experience.system import AnyObject


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

    def anchor_point(self, value: int = None) -> Union['DrawingTextProperties', int]:
        if value is not None:
            self.drawing_text_properties.AnchorPoint = value
            return self
        return self.drawing_text_properties.AnchorPoint

    def blanking(self, value: int = None) ->  Union['DrawingTextProperties', int]:
        if value is not None:
            self.drawing_text_properties.Blanking = value
            return self
        return self.drawing_text_properties.Blanking

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

    def frame_type(self, value: int = None) ->  Union['DrawingTextProperties', int]:
        if value is not None:
            self.drawing_text_properties.FrameType = value
            return self
        return self.drawing_text_properties.FrameType

    def italic(self, value: int = None) ->  Union['DrawingTextProperties', int]:
        if value is not None:
            self.drawing_text_properties.Italic = value
            return self
        return self.drawing_text_properties.Italic

    def justification(self, value: int = None) ->  Union['DrawingTextProperties', int]:
        if value is not None:
            self.drawing_text_properties.Justification = value
            return self
        return self.drawing_text_properties.Justification

    def kerning(self, value: int = None) ->  Union['DrawingTextProperties', int]:
        if value is not None:
            self.drawing_text_properties.Kerning = value
            return self
        return self.drawing_text_properties.Kerning

    def mirror(self, value: int = None) ->  Union['DrawingTextProperties', int]:
        if value is not None:
            self.drawing_text_properties.Mirror = value
            return self
        return self.drawing_text_properties.Mirror

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

    def activate_frame(self, i_type: int) -> 'DrawingTextProperties':
        self.drawing_text_properties.ActivateFrame(i_type)
        return self

    def update(self) -> 'DrawingTextProperties':
        self.drawing_text_properties.Update()
        return self

    def __repr__(self):
        return f'DrawingTextProperties(name="{self.name()}")'
