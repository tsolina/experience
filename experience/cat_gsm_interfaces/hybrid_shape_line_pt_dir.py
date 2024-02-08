from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Line
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection
    from experience.knowledge_interfaces import Length


class HybridShapeLinePtDir(Line):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Line
                |                             HybridShapeLinePtDir
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_line_pt_dir = com

    def begin_offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_line_pt_dir.BeginOffset)

    def dir(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeLinePtDir', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_pt_dir.Dir = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_line_pt_dir.Dir)

    def end_offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_line_pt_dir.EndOffset)

    def orientation(self, value: int = None) -> Union['HybridShapeLinePtDir', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_pt_dir.Orientation = value
            return self
        return self.hybrid_shape_line_pt_dir.Orientation

    def point(self, value: Reference = None) -> Union['HybridShapeLinePtDir', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_pt_dir.Point = value._com
            return self
        return Reference(self.hybrid_shape_line_pt_dir.Point)

    def support(self, value: Reference = None) -> Union['HybridShapeLinePtDir', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_pt_dir.Support = value._com
            return self
        return Reference(self.hybrid_shape_line_pt_dir.Support)

    def remove_support(self) -> 'HybridShapeLinePtDir':
        self.hybrid_shape_line_pt_dir.RemoveSupport()
        return self
    
    def length_type(self, value: int = None) -> Union['HybridShapeLinePtDir', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_pt_dir.SetLengthType(value)
            return self
        return self.hybrid_shape_line_pt_dir.GetLengthType()
    
    def symmetrical_extension(self, value: bool = None) -> Union['HybridShapeLinePtDir', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_line_pt_dir.SetSymmetricalExtension(value)
            return self
        return self.hybrid_shape_line_pt_dir.GetSymmetricalExtension()

    def __repr__(self):
        return f'HybridShapeLinePtDir(name="{self.name}")'