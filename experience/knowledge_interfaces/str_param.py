from experience.knowledge_interfaces.parameter import Parameter

class StrParam(Parameter):
    def __init__(self, com):
        super().__init__(com)
        self.str_param = com

    def value(self, value: str = None) -> str:
        if value is not None:
            self.str_param.Value = value
            return self
        return self.str_param.Value

    def get_enumerate_values(self, o_safe_array: tuple) -> tuple:
        return self.str_param.GetEnumerateValues(o_safe_array)

    def get_enumerate_values_size(self) -> int:
        return self.str_param.GetEnumerateValuesSize()

    def set_enumerate_values(self, i_safe_array: tuple) -> 'StrParam':
        self.str_param.SetEnumerateValues(i_safe_array)
        return self

    def suppress_enumerate_values(self) -> 'StrParam':
        self.str_param.SuppressEnumerateValues()
        return self

    def __repr__(self):
        return f'StrParam(name="{ self.name }")'
