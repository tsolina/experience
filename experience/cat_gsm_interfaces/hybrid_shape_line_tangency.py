from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Line
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class HybridShapeLineTangency(Line):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Line
                |                             HybridShapeLineTangency
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_line_tangency = com

    def begin_offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_line_tangency.BeginOffset)

    def curve(self, value: Reference = None) -> Union['HybridShapeLineTangency', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_tangency.Curve = value._com
            return self
        return Reference(self.hybrid_shape_line_tangency.Curve)

    def end_offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_line_tangency.EndOffset)

    def orientation(self, value: int = None) -> Union['HybridShapeLineTangency', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_tangency.Orientation = value
            return self
        return self.hybrid_shape_line_tangency.Orientation

    def point(self, value: Reference = None) -> Union['HybridShapeLineTangency', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_tangency.Point = value._com
            return self
        return Reference(self.hybrid_shape_line_tangency.Point)

    def support(self, value: Reference = None) -> Union['HybridShapeLineTangency', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_tangency.Support = value._com
            return self
        return Reference(self.hybrid_shape_line_tangency.Support)

    def remove_support(self) -> 'HybridShapeLineTangency':
        self.hybrid_shape_line_tangency.RemoveSupport()
        return self
    
    def length_type(self, value: int = None) -> Union['HybridShapeLineTangency', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_tangency.SetLengthType(value)
            return self
        return self.hybrid_shape_line_tangency.GetLengthType()
    
    def symmetrical_extension(self, value: bool = None) -> Union['HybridShapeLineTangency', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_tangency.SetSymmetricalExtension(value)
            return self
        return self.hybrid_shape_line_tangency.GetSymmetricalExtension()

    def __repr__(self):
        return f'HybridShapeLineTangency(name="{self.name}")'