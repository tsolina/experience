from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Plane
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle

class HybridShapePlaneAngle(Plane):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneAngle
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_plane_angle = com

    def angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_plane_angle.Angle)

    def orientation(self, value: int = None) -> Union['HybridShapePlaneAngle', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_angle.Orientation = value
            return self
        return self.hybrid_shape_plane_angle.Orientation

    def ref_plane(self, value: Reference = None) -> Union['HybridShapePlaneAngle', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_angle.Plane = value._com
            return self
        return Reference(self.hybrid_shape_plane_angle.Plane)

    def projection_mode(self, value: bool = None) -> Union['HybridShapePlaneAngle', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_angle.ProjectionMode = value
            return self
        return self.hybrid_shape_plane_angle.ProjectionMode

    def revol_axis(self, value: Reference = None) -> Union['HybridShapePlaneAngle', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_angle.RevolAxis = value._com
            return self
        return Reference(self.hybrid_shape_plane_angle.RevolAxis)

    def __repr__(self):
        return f'HybridShapePlaneAngle(name="{self.name}")'