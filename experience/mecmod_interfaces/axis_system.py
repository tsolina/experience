from typing import Union
from experience.inf_interfaces import Reference
from experience.knowledge_interfaces import Angle
from experience.system import AnyObject
from experience.types import cat_variant

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

    def origin_type(self, value: int = None) -> Union['AxisSystem', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.OriginType = value
            return self  
        return self.axis_system.OriginType

    def type(self, value: int = None) -> Union['AxisSystem', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.Type = value
            return self  
        return self.axis_system.Type

    def x_axis_direction(self, value: Reference = None) -> Union['AxisSystem', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.XAxisDirection = value._com
            return self            
        return Reference(self.axis_system.XAxisDirection)

    def x_axis_type(self, value: int = None) -> Union['AxisSystem', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.XAxisType = value
            return self  
        return self.axis_system.XAxisType

    def y_axis_direction(self, value: Reference = None) -> Union['AxisSystem', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.YAxisDirection = value._com
            return self      
        return Reference(self.axis_system.YAxisDirection)

    def y_axis_type(self, value: int = None) -> Union['AxisSystem', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.YAxisType = value
            return self  
        return self.axis_system.YAxisType

    def z_axis_direction(self, value: Reference = None) -> Union['AxisSystem', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.ZAxisDirection = value._com
            return self  
        return Reference(self.axis_system.ZAxisDirection)

    @property
    def z_axis_type(self, value: int = None) -> Union['AxisSystem', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.axis_system.ZAxisType = value
            return self  
        return self.axis_system.ZAxisType

    def get_euler_angles(self, o_first_angle: Angle, o_second_angle: Angle, o_third_angle: Angle) -> tuple[Angle, Angle, Angle]:
        # vba_function_name = 'get_euler_angles'
        # vba_code = """
        # Public Function get_euler_angles(axis_system)
        #     Dim oFirstAngle (2)
        #     axis_system.GetEulerAngles oFirstAngle
        #     get_euler_angles = oFirstAngle
        # End Function
        # """

        # system_service = self.application.system_service
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])
        return self.axis_system.GetEulerAngles(o_first_angle, o_second_angle, o_third_angle)

    def get_origin(self, o_origin: tuple = None) -> tuple:
        # vba_function_name = 'get_origin'
        # vba_code = """
        # Public Function get_origin(axis_system)
        #     Dim oOrigin (2)
        #     axis_system.GetOrigin oOrigin
        #     get_origin = oOrigin
        # End Function
        # """

        # system_service = self.application.system_service
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])
        return self.axis_system.GetOrigin(o_origin)

    def get_vectors(self, o_vector_x: tuple = None, o_vector_y: tuple = None) -> tuple:
        # vba_function_name = "get_vectors"
        # vba_code = """
        # Public Function get_vectors(axis_system)
        #     Dim oVectorX (2)
        #     Dim oVectorY (2)
        #     axis_system.GetVectors oVectorX, oVectorY
        #     Dim oVectors (1)
        #     oVectors(0) = oVectorX
        #     oVectors(1) = oVectorY
        #     get_vectors = oVectors
        # End Function
        # """

        # system_service = self.application.system_service
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])
        return self.axis_system.GetVectors(o_vector_x, o_vector_y)

    def get_x_axis(self, o_x_axis: tuple = None) -> tuple:
        # vba_function_name = 'get_x_axis'
        # vba_code = """
        # Public Function get_x_axis(axis_system)
        #     Dim oXAxis (2)
        #     axis_system.GetXAxis oXAxis
        #     get_x_axis = oXAxis
        # End Function
        # """

        # system_service = self.application.system_service
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])
        return self.axis_system.GetXAxis(o_x_axis)

    def get_y_axis(self, o_y_axis: tuple = None) -> tuple:
        # vba_function_name = 'get_y_axis'
        # vba_code = """
        # Public Function get_y_axis(axis_system)
        #     Dim oYAxis (2)
        #     axis_system.GetYAxis oYAxis
        #     get_y_axis = oYAxis
        # End Function
        # """

        # system_service = self.application.system_service
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])
        return self.axis_system.GetYAxis(o_y_axis)

    def get_z_axis(self, o_z_axis: tuple = None) -> tuple:
        # vba_function_name = 'get_z_axis'
        # vba_code = """
        # Public Function get_z_axis(axis_system)
        #     Dim oZAxis (2)
        #     axis_system.GetZAxis oZAxis
        #     get_z_axis = oZAxis
        # End Function
        # """

        # system_service = self.application.system_service
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])
        return self.axis_system.GetZAxis(o_z_axis)

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

    def __repr__(self):
        return f'AxisSystem(name="{self.name}")'