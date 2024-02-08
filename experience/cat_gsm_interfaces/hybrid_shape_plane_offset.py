from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Plane
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class HybridShapePlaneOffset(Plane):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneOffset
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_plane_offset = com

    def offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_plane_offset.Offset)

    def orientation(self, value: int = None) -> Union['HybridShapePlaneOffset', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_offset.Orientation = value
            return self
        return self.hybrid_shape_plane_offset.Orientation

    def ref_plane(self, value: Reference = None) -> Union['HybridShapePlaneOffset', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_offset.Plane = value._com
            return self
        return Reference(self.hybrid_shape_plane_offset.Plane)

    def __repr__(self):
        return f'HybridShapePlaneOffset(name="{self.name}")'