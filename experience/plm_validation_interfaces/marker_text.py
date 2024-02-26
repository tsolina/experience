from typing import Union
from experience.plm_validation_interfaces import Marker

class MarkerText(Marker):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMValidationIDLItf.Marker
                |                         MarkerText
    """

    def __init__(self, com):
        super().__init__(com)
        self.marker_text = com

    def text(self, value: str = None) -> Union['MarkerText', str]:
        if str is not None:
            self.marker_text.Text = value
            return self
        return self.marker_text.Text
    
    def text_font(self, value: str = None) -> Union['MarkerText', str]:
        if str is not None:
            self.marker_text.TextFont = value
            return self
        return self.marker_text.TextFont
    
    def text_size(self, value: float = None) -> Union['MarkerText', float]:
        if str is not None:
            self.marker_text.TextSize = value
            return self
        return self.marker_text.TextSize