from typing import Union
from experience.system import AnyObject

class DrawingDimValue(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingDimValue
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_dim_value = com

    def fake_dim_type(self, value: int = None) -> Union['DrawingDimValue', int]:
        if value is not None:
            self.drawing_dim_value.FakeDimType = value
            return self
        return self.drawing_dim_value.FakeDimType

    def scoring_mode(self, value: int = None) -> Union['DrawingDimValue', int]:
        if value is not None:
            self.drawing_dim_value.ScoringMode = value
            return self
        return self.drawing_dim_value.ScoringMode

    def value(self) -> float:
        return self.drawing_dim_value.Value

    def value_framed_element(self, value: int = None) -> Union['DrawingDimValue', int]:
        if value is not None:
            self.drawing_dim_value.ValueFramedElement = value
            return self
        return self.drawing_dim_value.ValueFramedElement

    def value_framed_group(self, value: int = None) -> Union['DrawingDimValue', int]:
        if value is not None:
            self.drawing_dim_value.ValueFramedGroup = value
            return self
        return self.drawing_dim_value.ValueFramedGroup

    def get_bault_text(self, i_index: int) -> tuple[str, str, str, str]:
        return self._get_multi([self.drawing_dim_value, i_index], ('DrawingDimValue', 'GetBaultText', 'Long'), ('String', 'String', 'String', 'String'))

    def get_display_unit(self, i_index: int) -> int:
        return self.drawing_dim_value.GetDisplayUnit(i_index)

    def get_fake_dim_value(self, i_index: int) -> str:
        return self.drawing_dim_value.GetFakeDimValue(i_index)

    def get_format_display_factor(self, i_index: int) -> int:
        return self.drawing_dim_value.GetFormatDisplayFactor(i_index)

    def get_format_name(self, i_index: int) -> str:
        return self.drawing_dim_value.GetFormatName(i_index)

    def get_format_precision(self, index: int) -> float:
        return self.drawing_dim_value.GetFormatPrecision(index)

    def get_format_type(self, i_index: int) -> int:
        return self.drawing_dim_value.GetFormatType(i_index)

    def get_format_unit(self, i_index: int) -> int:
        return self.drawing_dim_value.GetFormatUnit(i_index)

    def get_ps_text(self, i_index: int) -> tuple[str, str]: # to test
        return self._get_multi([self.drawing_dim_value, i_index], ('DrawingDimValue', 'GetPSText', 'Long'), ('String', 'String'))

    def get_scored_element(self, i_index: int) -> bool:
        return self.drawing_dim_value.GetScoredElement(i_index)

    def set_bault_text(self, i_index: int, i_before: str, i_after: str, i_upper: str, i_lower: str) -> 'DrawingDimValue':
        self.drawing_dim_value.SetBaultText(i_index, i_before, i_after, i_upper, i_lower)
        return self

    def set_fake_dim_value(self, i_index: int, i_fake_dim_value: str) -> 'DrawingDimValue':
        self.drawing_dim_value.SetFakeDimValue(i_index, i_fake_dim_value)
        return self

    def set_format_display_factor(self, i_index: int, i_frm_dsp_fact: int) -> 'DrawingDimValue':
        self.drawing_dim_value.SetFormatDisplayFactor(i_index, i_frm_dsp_fact)
        return self

    def set_format_name(self, i_index: int, i_frm_name: str) -> 'DrawingDimValue':
        self.drawing_dim_value.SetFormatName(i_index, i_frm_name)
        return self

    def set_format_precision(self, i_index: int, i_frm_precision: float) -> 'DrawingDimValue':
        self.drawing_dim_value.SetFormatPrecision(i_index, i_frm_precision)
        return self

    def set_format_type(self, i_index: int, i_frm_type: int) -> 'DrawingDimValue':
        self.drawing_dim_value.SetFormatType(i_index, i_frm_type)
        return self

    def set_format_unit(self, i_index: int, i_frm_unit: int) -> 'DrawingDimValue':
        self.drawing_dim_value.SetFormatUnit(i_index, i_frm_unit)
        return self

    def set_ps_text(self, i_index: int, i_prefix: str, i_suffix: str) -> 'DrawingDimValue':
        self.drawing_dim_value.SetPSText(i_index, i_prefix, i_suffix)
        return self

    def set_scored_element(self, i_index: int, i_scored_element: bool) -> 'DrawingDimValue':
        return self.drawing_dim_value.SetScoredElement(i_index, i_scored_element)

    def __repr__(self):
        return f'DrawingDimValue(name="{self.name()}")'
