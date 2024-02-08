from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Plane
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length, RealParam

class HybridShapePlaneEquation(Plane):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneEquation
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_plane_equation = com

    def a(self) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.hybrid_shape_plane_equation.A)

    def b(self) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.hybrid_shape_plane_equation.B)

    def c(self) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.hybrid_shape_plane_equation.C)

    def d(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_plane_equation.D)

    def ref_axis_system(self, value: Reference = None) -> Union['HybridShapePlaneEquation', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_equation.RefAxisSystem = value._com
            return self
        return Reference(self.hybrid_shape_plane_equation.RefAxisSystem)
    
    def reference_point(self, value: Reference = None) -> Union['HybridShapePlaneEquation', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_equation.SetReferencePoint(value._com)
            return self
        return Reference(self.hybrid_shape_plane_equation.GetReferencePoint())

    def __repr__(self):
        return f'HybridShapePlaneEquation(name="{self.name}")'