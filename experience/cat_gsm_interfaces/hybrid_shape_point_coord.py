from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Point
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class HybridShapePointCoord(Point):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Point
                |                             HybridShapePointCoord
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_point_coord = com

    def pt_ref(self, value: Reference = None) -> Union['HybridShapePointCoord', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_coord.PtRef = value._com
            return self
        return Reference(self.hybrid_shape_point_coord.PtRef)

    def ref_axis_system(self, value: Reference = None) -> Union['HybridShapePointCoord', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_coord.RefAxisSystem = value._com
            return self
        return Reference(self.hybrid_shape_point_coord.RefAxisSystem)

    def x(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_point_coord.X)

    def y(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_point_coord.Y)

    def z(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_point_coord.Z)

    def __repr__(self):
        return f'HybridShapePointCoord(name="{self.name}")'