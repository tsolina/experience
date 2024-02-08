from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces.reference import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces.real_param import RealParam

class HybridShapeConnect(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeConnect
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_connect = com

    def base_curve(self, value: Reference = None) -> Union['HybridShapeConnect', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_connect.BaseCurve = value._com
            return self
        return Reference(self.hybrid_shape_connect.BaseCurve)

    def connect_type(self, value: int = None) -> Union['HybridShapeConnect', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_connect.ConnectType = value
            return self
        return self.hybrid_shape_connect.ConnectType

    def first_continuity(self, value: int = None) -> Union['HybridShapeConnect', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_connect.FirstContinuity = value
            return self
        return self.hybrid_shape_connect.FirstContinuity

    def first_curve(self, value: Reference = None) -> Union['HybridShapeConnect', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_connect.FirstCurve = value._com
            return self
        return Reference(self.hybrid_shape_connect.FirstCurve)

    def first_orientation(self, value: int = None) -> Union['HybridShapeConnect', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_connect.FirstOrientation = value
            return self
        return self.hybrid_shape_connect.FirstOrientation

    def first_point(self, value: Reference = None) -> Union['HybridShapeConnect', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_connect.FirstPoint = value._com
            return self
        return Reference(self.hybrid_shape_connect.FirstPoint)

    def first_tension(self) -> 'RealParam':
        from experience.knowledge_interfaces.real_param import RealParam
        return RealParam(self.hybrid_shape_connect.FirstTension)

    def second_continuity(self, value: int = None) -> Union['HybridShapeConnect', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_connect.SecondContinuity = value
            return self
        return self.hybrid_shape_connect.SecondContinuity

    def second_curve(self, value: Reference = None) -> Union['HybridShapeConnect', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_connect.SecondCurve = value._com
            return self
        return Reference(self.hybrid_shape_connect.SecondCurve)

    def second_orientation(self, value: int = None) -> Union['HybridShapeConnect', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_connect.SecondOrientation = value
            return self
        return self.hybrid_shape_connect.SecondOrientation

    def second_point(self, value: Reference = None) -> Union['HybridShapeConnect', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_connect.SecondPoint = value._com
            return self
        return Reference(self.hybrid_shape_connect.SecondPoint)

    def second_tension(self) -> 'RealParam':
        from experience.knowledge_interfaces.real_param import RealParam
        return RealParam(self.hybrid_shape_connect.SecondTension)

    def trim(self, value: bool = None) -> Union['HybridShapeConnect', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_connect.Trim = value
            return self
        return self.hybrid_shape_connect.Trim

    def __repr__(self):
        return f'HybridShapeConnect(name="{self.name}")'