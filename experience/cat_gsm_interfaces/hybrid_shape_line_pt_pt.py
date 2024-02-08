from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Line
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class HybridShapeLinePtPt(Line):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Line
                |                             HybridShapeLinePtPt
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_line_pt_pt = com

    def begin_offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_line_pt_pt.BeginOffset)

    def end_offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_line_pt_pt.EndOffset)

    def pt_extremity(self, value: Reference = None) -> Union['HybridShapeLinePtPt', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_pt_pt.PtExtremity = value._com
            return self
        return Reference(self.hybrid_shape_line_pt_pt.PtExtremity)

    def pt_origin(self, value: Reference = None) -> Union['HybridShapeLinePtPt', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_pt_pt.PtOrigine = value._com
            return self
        return Reference(self.hybrid_shape_line_pt_pt.PtOrigine)

    def support(self, value: Reference = None) -> Union['HybridShapeLinePtPt', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_pt_pt.Support = value._com
            return self
        return Reference(self.hybrid_shape_line_pt_pt.Support)
  
    def remove_support(self) -> 'HybridShapeLinePtPt':
        self.hybrid_shape_line_pt_pt.RemoveSupport()
        return self
    
    def length_type(self, value: int = None) -> Union['HybridShapeLinePtPt', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_pt_pt.SetLengthType(value)
            return self
        return self.hybrid_shape_line_pt_pt.GetLengthType()
    
    def symmetrical_extension(self, value: bool = None) -> Union['HybridShapeLinePtPt', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_pt_pt.SetSymmetricalExtension(value)
            return self
        return self.hybrid_shape_line_pt_pt.GetSymmetricalExtension()

    def __repr__(self):
        return f'HybridShapeLinePtPt(name="{self.name}")'