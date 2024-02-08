from typing import Union

from experience.inf_interfaces import Reference
from experience.knowledge_interfaces import RealParam
from experience.mecmod_interfaces import HybridShape

class HybridShapeDirection(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeDirection   
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_direction = com

    def object(self, value: int = None) -> Union['HybridShapeDirection', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_direction.Object = value
            return self
        return Reference(self.hybrid_shape_direction.Object)

    def ref_axis_system(self, value: Reference = None) -> Union['HybridShapeDirection', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_direction.Object = value._com
            return self
        return Reference(self.hybrid_shape_direction.RefAxisSystem)

    def type(self) -> int:
        return self.hybrid_shape_direction.Type

    def direction_specification(self) -> int:
        return self.hybrid_shape_direction.DirectionSpecification()

    def get_x(self):
        return RealParam(self.hybrid_shape_direction.GetX())

    def get_x_val(self) -> float:
        return self.hybrid_shape_direction.GetXVal()

    def get_y(self) -> RealParam:
        return RealParam(self.hybrid_shape_direction.GetY())

    def get_y_val(self) -> float:
        return self.hybrid_shape_direction.GetYVal()

    def get_z(self) -> RealParam:
        return RealParam(self.hybrid_shape_direction.GetZ())

    def get_z_val(self) -> float:
        return self.hybrid_shape_direction.GetZVal()

    def __repr__(self):
        return f'HybridShapeDirection(name="{self.name}")'