from experience.knowledge_interfaces.parameter import Parameter

class IntParam(Parameter):
    def __init__(self, com):
        super().__init__(com)
        self.int_param = com

    def range_max(self, value: int = None) -> int:
        if value is not None:
            self.int_param.RangeMax = value
            return self
        return self.int_param.RangeMax

    def range_max_validity(self, value: int = None) -> int:
        if value is not None:
            self.int_param.RangeMaxValidity = value
            return self
        return self.int_param.RangeMaxValidity

    def range_min(self, value: int = None) -> int:
        if value is not None:
            self.int_param.RangeMin = value
            return self
        return self.int_param.RangeMin

    def range_min_validity(self, value: int = None) -> int:
        if value is not None:
            self.int_param.RangeMinValidity = value
            return self
        return self.int_param.RangeMinValidity

    def value(self, value: int = None) -> int:
        if value is not None:
            self.int_param.Value = value
            return self
        return self.int_param.Value

    def get_enumerate_values(self, o_safe_array: tuple) -> tuple:
        return self.int_param.GetEnumerateValues(o_safe_array)

    def get_enumerate_values_size(self) -> int:
        return self.int_param.GetEnumerateValuesSize()

    def set_enumerate_values(self, i_safe_array: tuple) -> 'IntParam':
        self.int_param.SetEnumerateValues(i_safe_array)
        return self

    def suppress_enumerate_values(self) -> 'IntParam':
        self.int_param.SuppressEnumerateValues()
        return self

    def __repr__(self):
        return f'IntParam(name="{self.name()}")'
