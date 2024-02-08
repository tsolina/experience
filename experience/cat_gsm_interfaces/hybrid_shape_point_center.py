from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Point
from experience.inf_interfaces import Reference

class HybridShapePointCenter(Point):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Point
                |                             HybridShapePointCenter
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_point_center = com

    def element(self, value: Reference = None) -> Union['HybridShapePointCenter', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_center.Element = value._com
            return self
        return Reference(self.hybrid_shape_point_center.Element)

    def __repr__(self):
        return f'HybridShapePointCenter(name="{self.name}")'