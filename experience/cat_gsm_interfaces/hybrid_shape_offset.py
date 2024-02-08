from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class HybridShapeOffset(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeOffset
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_offset = com

    def offset_direction(self, value: bool = None) -> Union['HybridShapeOffset', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_offset.OffsetDirection = value
            return self
        return self.hybrid_shape_offset.OffsetDirection

    def offset_value(self, value: 'Length' = None) -> Union['HybridShapeOffset', 'Length']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_offset.OffsetValue = value._com
            return self
        return Length(self.hybrid_shape_offset.OffsetValue)

    def offseted_object(self, value: Reference = None) -> Union['HybridShapeOffset', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_offset.OffsetedObject = value._com
            return self
        return Reference(self.hybrid_shape_offset.OffsetedObject)

    def suppress_mode(self, value: bool = None) -> Union['HybridShapeOffset', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_offset.SuppressMode = value
            return self
        return self.hybrid_shape_offset.SuppressMode

    def add_tricky_face(self, i_tricky_face: Reference) -> 'HybridShapeOffset':
        self.hybrid_shape_offset.AddTrickyFace(i_tricky_face._com)
        return self

    def get_tricky_face(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_offset.GetTrickyFace(i_rank))

    def remove_tricky_face(self, i_rank: int) -> 'HybridShapeOffset':
        self.hybrid_shape_offset.RemoveTrickyFace(i_rank)
        return self

    def set_offset_value(self, i_offset: float) -> 'HybridShapeOffset':
        self.hybrid_shape_offset.SetOffsetValue(i_offset)
        return self

    def __repr__(self):
        return f'HybridShapeOffset(name="{self.name}")'