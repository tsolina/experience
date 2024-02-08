from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Line
from experience.inf_interfaces import Reference

class HybridShapeLineBiTangent(Line):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Line
                |                             HybridShapeLineBiTangent
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_line_bi_tangent = com

    def curve1(self, value: Reference = None) -> Union['HybridShapeLineBiTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_bi_tangent.Curve1 = value._com
            return self
        return Reference(self.hybrid_shape_line_bi_tangent.Curve1)

    def element2(self, value: Reference = None) -> Union['HybridShapeLineBiTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_bi_tangent.Element2 = value._com
            return self
        return Reference(self.hybrid_shape_line_bi_tangent.Element2)

    def support(self, value: Reference = None) -> Union['HybridShapeLineBiTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_bi_tangent.Support = value._com
            return self
        return Reference(self.hybrid_shape_line_bi_tangent.Support)

    def get_choice_no(self) -> tuple[int, int, int, int, int]:
        self.hybrid_shape_line_bi_tangent.GetChoiceNo()
        return self

    def get_length_type(self) -> int:
        return self.hybrid_shape_line_bi_tangent.GetLengthType()

    def set_choice_no(self, val1: int, val2: int, val3: int, val4: int, val5: int) -> 'HybridShapeLineBiTangent':
        self.hybrid_shape_line_bi_tangent.SetChoiceNo(val1, val2, val3, val4, val5)
        return self

    def set_length_type(self, i_type: int) -> 'HybridShapeLineBiTangent':
        self.hybrid_shape_line_bi_tangent.SetLengthType(i_type)
        return self

    def __repr__(self):
        return f'HybridShapeLineBiTangent(name="{self.name}")'