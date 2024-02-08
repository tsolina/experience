from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Line
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class HybridShapeLineNormal(Line):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Line
                |                             HybridShapeLineNormal
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_line_normal = com

    def begin_offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_line_normal.BeginOffset)

    def end_offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_line_normal.EndOffset)

    def orientation(self, value: int = None) -> Union['HybridShapeLineNormal', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_normal.Orientation = value
            return self
        return self.hybrid_shape_line_normal.Orientation

    def point(self, value: Reference = None) -> Union['HybridShapeLineNormal', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_normal.Point = value._com
            return self
        return Reference(self.hybrid_shape_line_normal.Point)

    def surface(self, value: Reference = None) -> Union['HybridShapeLineNormal', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_normal.Surface = value._com
            return self
        return Reference(self.hybrid_shape_line_normal.Surface)
    
    def length_type(self, value: int = None) -> Union['HybridShapeLineNormal', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_normal.SetLengthType(value)
            return self
        return self.hybrid_shape_line_normal.GetLengthType()  
    
    def symmetrical_extension(self, value: bool = None) -> Union['HybridShapeLineNormal', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_normal.SetSymmetricalExtension(value)
            return self
        return self.hybrid_shape_line_normal.GetSymmetricalExtension()  

    def __repr__(self):
        return f'HybridShapeLineNormal(name="{self.name}")'