from typing import Union
from experience.system import AnyObject

from experience.cat_annotation_interfaces.annotation_types import *

from experience.types.enum_item import EnumItem
class AnnotationValueIndex(EnumItem):
    main_value = 1
    dual_value = 2

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

    def fake_dim_type(self, value: CatDimFake = None) -> Union['DrawingDimValue', CatDimFake]:
        if value is not None:
            self.drawing_dim_value.FakeDimType = int(value)
            return self
        return CatDimFake.item(self.drawing_dim_value.FakeDimType)

    def scoring_mode(self, value: CatDimScore = None) -> Union['DrawingDimValue', CatDimScore]:
        if value is not None:
            self.drawing_dim_value.ScoringMode = int(value)
            return self
        return CatDimScore.item(self.drawing_dim_value.ScoringMode)

    def value(self) -> float:
        return self.drawing_dim_value.Value

    def value_framed_element(self, value: CatDimFramedElement = None) -> Union['DrawingDimValue', CatDimFramedElement]:
        if value is not None:
            self.drawing_dim_value.ValueFramedElement = int(value)
            return self
        return CatDimFramedElement.item(self.drawing_dim_value.ValueFramedElement)

    def value_framed_group(self, value: CatDimFramedGroup = None) -> Union['DrawingDimValue', CatDimFramedGroup]:
        if value is not None:
            self.drawing_dim_value.ValueFramedGroup = int(value)
            return self
        return CatDimFramedGroup.item(self.drawing_dim_value.ValueFramedGroup)

    def get_bault_text(self, i_index: AnnotationValueIndex) -> tuple[str, str, str, str]:
        return self._get_multi([self.drawing_dim_value, int(i_index)], ('DrawingDimValue', 'GetBaultText', 'Long'), ('String', 'String', 'String', 'String'))

    def get_display_unit(self, i_index: AnnotationValueIndex) -> int:
        return self.drawing_dim_value.GetDisplayUnit(int(i_index))

    def get_fake_dim_value(self, i_index: AnnotationValueIndex) -> str:
        return self.drawing_dim_value.GetFakeDimValue(int(i_index))

    def get_format_display_factor(self, i_index: AnnotationValueIndex) -> int:
        return self.drawing_dim_value.GetFormatDisplayFactor(int(i_index))

    def get_format_name(self, i_index: AnnotationValueIndex) -> str:
        return self.drawing_dim_value.GetFormatName(int(i_index))

    def get_format_precision(self, i_index: AnnotationValueIndex) -> float:
        return self.drawing_dim_value.GetFormatPrecision(int(i_index))

    def get_format_type(self, i_index: AnnotationValueIndex) -> int:
        return self.drawing_dim_value.GetFormatType(int(i_index))

    def get_format_unit(self, i_index: AnnotationValueIndex) -> int:
        return self.drawing_dim_value.GetFormatUnit(int(i_index))

    def get_ps_text(self, i_index: AnnotationValueIndex) -> tuple[str, str]: # to test
        return self._get_multi([self.drawing_dim_value, int(i_index)], ('DrawingDimValue', 'GetPSText', 'Long'), ('String', 'String'))

    def get_scored_element(self, i_index: AnnotationValueIndex) -> bool:
        return self.drawing_dim_value.GetScoredElement(int(i_index))

    def set_bault_text(self, i_index: AnnotationValueIndex, i_before: str, i_after: str, i_upper: str, i_lower: str) -> 'DrawingDimValue':
        self.drawing_dim_value.SetBaultText(int(i_index), i_before, i_after, i_upper, i_lower)
        return self

    def set_fake_dim_value(self, i_index: AnnotationValueIndex, i_fake_dim_value: str) -> 'DrawingDimValue':
        self.drawing_dim_value.SetFakeDimValue(int(i_index), i_fake_dim_value)
        return self

    def set_format_display_factor(self, i_index: AnnotationValueIndex, i_frm_dsp_fact: int) -> 'DrawingDimValue':
        self.drawing_dim_value.SetFormatDisplayFactor(int(i_index), i_frm_dsp_fact)
        return self

    def set_format_name(self, i_index: AnnotationValueIndex, i_frm_name: str) -> 'DrawingDimValue':
        self.drawing_dim_value.SetFormatName(int(i_index), i_frm_name)
        return self

    def set_format_precision(self, i_index: AnnotationValueIndex, i_frm_precision: float) -> 'DrawingDimValue':
        self.drawing_dim_value.SetFormatPrecision(int(i_index), i_frm_precision)
        return self

    def set_format_type(self, i_index: AnnotationValueIndex, i_frm_type: int) -> 'DrawingDimValue':
        self.drawing_dim_value.SetFormatType(int(i_index), i_frm_type)
        return self

    def set_format_unit(self, i_index: AnnotationValueIndex, i_frm_unit: int) -> 'DrawingDimValue':
        self.drawing_dim_value.SetFormatUnit(int(i_index), i_frm_unit)
        return self

    def set_ps_text(self, i_index: AnnotationValueIndex, i_prefix: str, i_suffix: str) -> 'DrawingDimValue':
        self.drawing_dim_value.SetPSText(int(i_index), i_prefix, i_suffix)
        return self

    def set_scored_element(self, i_index: AnnotationValueIndex, i_scored_element: bool) -> 'DrawingDimValue':
        return self.drawing_dim_value.SetScoredElement(int(i_index), i_scored_element)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
