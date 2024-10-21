from experience.system import AnyObject

class SimParameterSet(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimParameterSet
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_parameter_set = com

    def get_double_array_parameter(self, i_parameter_name: str) -> list[float]:
        return self.sim_parameter_set.GetDoubleArrayParameter(i_parameter_name)
    
    def get_double_parameter(self, i_parameter_name: str) -> float:
        return self.sim_parameter_set.GetDoubleParameter(i_parameter_name)
    
    def get_integer_array_parameter(self, i_parameter_name: str) -> list[int]:
        return self.sim_parameter_set.GetIntegerArrayParameter(i_parameter_name)
    
    def get_integer_parameter(self, i_parameter_name: str) -> float:
        return self.sim_parameter_set.GetIntegerParameter(i_parameter_name)
    
    def get_object_array_parameter(self, i_parameter_name: str) -> list[AnyObject]:
        objs = self.sim_parameter_set.GetObjectArrayParameter(i_parameter_name)
        return [AnyObject(obj) for obj in objs]
    
    def get_object_parameter(self, i_parameter_name: str) -> AnyObject:
        return AnyObject(self.sim_parameter_set.GetObjectParameter(i_parameter_name))
    
    def get_string_array_parameter(self, i_parameter_name: str) -> list[str]:
        return self.sim_parameter_set.GetStringArrayParameter(i_parameter_name)
    
    def get_string_parameter(self, i_parameter_name: str) -> float:
        return self.sim_parameter_set.GetStringParameter(i_parameter_name)
    
    def set_double_array_parameter(self, i_parameter_name: str, i_double_values: list[float]) -> 'SimParameterSet':
        self.sim_parameter_set.SetDoubleArrayParameter(i_parameter_name, i_double_values)
        return self
    
    def set_double_parameter(self, i_parameter_name: str, i_double_value: float) -> 'SimParameterSet':
        self.sim_parameter_set.SetDoubleParameter(i_parameter_name, i_double_value)

    def set_integer_array_parameter(self, i_parameter_name: str, i_integer_values: list[int]) -> 'SimParameterSet':
        self.sim_parameter_set.SetIntegerArrayParameter(i_parameter_name, i_integer_values)
        return self
    
    def set_integer_parameter(self, i_parameter_name: str, i_integer_value: int) -> 'SimParameterSet':
        self.sim_parameter_set.SetIntegerParameter(i_parameter_name, i_integer_value)

    def set_object_array_parameter(self, i_parameter_name: str, i_object_values: list[AnyObject]) -> 'SimParameterSet':
        i_objects = [getattr(obj, "_com", obj) for obj in i_object_values]
        self.sim_parameter_set.SetObjectArrayParameter(i_parameter_name, i_objects)
        return self
        
    def set_object_parameter(self, i_parameter_name: str, i_object_value: AnyObject) -> 'SimParameterSet':
        self.sim_parameter_set.SetObjectParameter(i_parameter_name, i_object_value._com)

    def set_string_array_parameter(self, i_parameter_name: str, i_string_values: list[str]) -> 'SimParameterSet':
        self.sim_parameter_set.SetStringArrayParameter(i_parameter_name, i_string_values)
        return self
    
    def set_string_parameter(self, i_parameter_name: str, i_string_value: str) -> 'SimParameterSet':
        self.sim_parameter_set.SetStringParameter(i_parameter_name, i_string_value)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'