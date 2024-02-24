from typing import Union
from experience.inf_interfaces import Reference
from experience.knowledge_interfaces import Angle
from experience.system import AnyObject
from experience.types import cat_variant
from experience.mecmod_interfaces.mecmod_types import *

class AxisSystem(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AxisSystem
    """

    def __init__(self, com):
        super().__init__(com)
        self.axis_system = com

    def axis_rotation_angle(self) -> Angle:
        return Angle(self.axis_system.AxisRotationAngle)

    def axis_rotation_reference(self, value: Reference = None) -> Union['AxisSystem', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.AxisRotationReference = value._com
            return self        
        return Reference(self.axis_system.AxisRotationReference)

    def is_current(self, value: bool = None) -> Union['AxisSystem', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.IsCurrent = value
            return self  
        return self.axis_system.IsCurrent

    def origin_point(self, value: Reference = None) -> Union['AxisSystem', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.OriginPoint = value._com
            return self            
        return Reference(self.axis_system.OriginPoint)

    def origin_type(self, value: CATAxisSystemOriginType = None) -> Union['AxisSystem', CATAxisSystemOriginType]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.OriginType = int(value)
            return self  
        return CATAxisSystemOriginType.item(self.axis_system.OriginType)

    def type(self, value: CATAxisSystemMainType = None) -> Union['AxisSystem', CATAxisSystemMainType]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.Type = int(value)
            return self  
        return CATAxisSystemMainType.item(self.axis_system.Type)

    def x_axis_direction(self, value: Reference = None) -> Union['AxisSystem', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.XAxisDirection = value._com
            return self            
        return Reference(self.axis_system.XAxisDirection)

    def x_axis_type(self, value: CATAxisSystemAxisType = None) -> Union['AxisSystem', CATAxisSystemAxisType]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.XAxisType = int(value)
            return self  
        return CATAxisSystemAxisType.item(self.axis_system.XAxisType)

    def y_axis_direction(self, value: Reference = None) -> Union['AxisSystem', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.YAxisDirection = value._com
            return self      
        return Reference(self.axis_system.YAxisDirection)

    def y_axis_type(self, value: CATAxisSystemAxisType = None) -> Union['AxisSystem', CATAxisSystemAxisType]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.YAxisType = int(value)
            return self  
        return CATAxisSystemAxisType.item(self.axis_system.YAxisType)

    def z_axis_direction(self, value: Reference = None) -> Union['AxisSystem', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.ZAxisDirection = value._com
            return self  
        return Reference(self.axis_system.ZAxisDirection)

    def z_axis_type(self, value: CATAxisSystemAxisType = None) -> Union['AxisSystem', CATAxisSystemAxisType]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.ZAxisType = int(value)
            return self  
        return CATAxisSystemAxisType.item(self.axis_system.ZAxisType)

    def get_euler_angles(self) -> tuple[Angle, Angle, Angle]: #, o_first_angle: Angle, o_second_angle: Angle, o_third_angle: Angle
        return self.axis_system.GetEulerAngles()

    def get_origin(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.axis_system, "GetOrigin", 2)

    def get_vectors(self) -> tuple[tuple[float, float, float], tuple[float, float, float]]:
        return self._get_safe_array_multi(self.axis_system, "GetVectors", (2, 2))

    def get_x_axis(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.axis_system, "GetXAxis", 2)

    def get_y_axis(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.axis_system, "GetYAxis", 2)

    def get_z_axis(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.axis_system, "GetZAxis", 2)

    def put_origin(self, i_origin: tuple) -> 'AxisSystem':
        self.axis_system.PutOrigin(i_origin)
        return self

    def put_vectors(self, i_vector_x: tuple, i_vector_y: tuple) -> 'AxisSystem':
        self.axis_system.PutVectors(i_vector_x, i_vector_y)
        return self

    def put_x_axis(self, i_x_axis: tuple) -> 'AxisSystem':
        self.axis_system.PutXAxis(i_x_axis)
        return self

    def put_y_axis(self, i_y_axis: tuple) -> 'AxisSystem':
        self.axis_system.PutYAxis(i_y_axis)
        return self

    def put_z_axis(self, i_z_axis: tuple) -> 'AxisSystem':
        self.axis_system.PutZAxis(i_z_axis)
        return self