from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import HybridShapeCircle
from experience.inf_interfaces import Reference

class HybridShapeCircleCtrPt(HybridShapeCircle):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircleCtrPt
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_circle_ctr_pt = com

    def center(self, value: Reference = None) -> Union['HybridShapeCircleCtrPt', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_ctr_pt.Center = value._com
            return self
        return Reference(self.hybrid_shape_circle_ctr_pt.Center)

    def crossing_point(self, value: Reference = None) -> Union['HybridShapeCircleCtrPt', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_ctr_pt.CrossingPoint = value._com
            return self
        return Reference(self.hybrid_shape_circle_ctr_pt.CrossingPoint)

    def support(self, value: Reference = None) -> Union['HybridShapeCircleCtrPt', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_ctr_pt.Support = value._com
            return self
        return Reference(self.hybrid_shape_circle_ctr_pt.Support)

    def is_geodesic(self) -> bool:
        return self.hybrid_shape_circle_ctr_pt.IsGeodesic()

    def set_geometry_on_support(self) -> 'HybridShapeCircleCtrPt':
        """ perform the action and return self"""
        self.hybrid_shape_circle_ctr_pt.SetGeometryOnSupport()
        return self

    def unset_geometry_on_support(self) -> 'HybridShapeCircleCtrPt':
        """ perform the action and return self"""
        self.hybrid_shape_circle_ctr_pt.UnsetGeometryOnSupport()
        return self

    def __repr__(self):
        return f'HybridShapeCircleCtrPt(name="{ self.name }")'