from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length, RealParam

class HybridShapeBump(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeBump
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_bump = com

    def body_to_bump(self, value: Reference = None) -> Union['HybridShapeBump', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_bump.BodyToBump = value._com
            return self
        return Reference(self.hybrid_shape_bump.BodyToBump)

    def center_tension(self, value: 'RealParam' = None) -> Union['HybridShapeBump', 'RealParam']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_bump.BodyToBump = value._com
            return self
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.hybrid_shape_bump.CenterTension)

    def continuity_type(self, value: int = None) -> Union['HybridShapeBump', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_bump.ContinuityType = value
            return self
        return self.hybrid_shape_bump.ContinuityType

    def deformation_center(self, value: Reference = None) -> Union['HybridShapeBump', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_bump.DeformationCenter = value._com
            return self
        return Reference(self.hybrid_shape_bump.DeformationCenter)

    def deformation_dir(self, value: Reference = None) -> Union['HybridShapeBump', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_bump.DeformationDir = value._com
            return self
        return Reference(self.hybrid_shape_bump.DeformationDir)

    def deformation_dist(self, value: 'Length' = None) -> Union['HybridShapeBump', 'Length']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_bump.DeformationDist = value._com
            return self
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_bump.DeformationDist)

    def deformation_dist_value(self, value: float = None) -> Union['HybridShapeBump', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_bump.DeformationDistValue = value
            return self
        return self.hybrid_shape_bump.DeformationDistValue

    def limit_curve(self, value: Reference = None) -> Union['HybridShapeBump', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_bump.LimitCurve = value._com
            return self
        return self.hybrid_shape_bump.LimitCurve

    def projection_dir(self, value: Reference = None) -> Union['HybridShapeBump', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_bump.ProjectionDir = value._com
            return self
        return Reference(self.hybrid_shape_bump.ProjectionDir)

    def __repr__(self):
        return f'HybridShapeBump(name="{self.name}")'