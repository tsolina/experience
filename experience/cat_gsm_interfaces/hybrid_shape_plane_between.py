from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Plane
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import RealParam

class HybridShapePlaneBetween(Plane):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneBetween
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_plane_between = com

    def first_element(self, value: Reference = None) -> Union['HybridShapePlaneBetween', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_between.FirstElement = value._com
            return self
        return Reference(self.hybrid_shape_plane_between.FirstElement)
    
    def orientation(self, value: int = None) -> Union['HybridShapePlaneBetween', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_between.Orientation = value
            return self
        return self.hybrid_shape_plane_between.Orientation

    def ratio(self) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.hybrid_shape_plane_between.Ratio)
    
    def second_element(self, value: Reference = None) -> Union['HybridShapePlaneBetween', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_between.SecondElement = value._com
            return self
        return Reference(self.hybrid_shape_plane_between.SecondElement)