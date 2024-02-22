from experience.knowledge_interfaces import Parameter

class RealParam(Parameter):
    def __init__(self, com):
        super().__init__(com)
        self.real_param = com

    def maximum_tolerance(self, value: float = None) -> float:
        if value is not None:
            self.real_param.MaximumTolerance = value
            return self
        return self.real_param.MaximumTolerance

    def minimum_tolerance(self, value: float = None) -> float:
        if value is not None:
            self.real_param.MinimumTolerance = value
            return self
        return self.real_param.MinimumTolerance

    def range_max(self, value: float = None) -> float:
        if value is not None:
            self.real_param.RangeMax = value
            return self
        return self.real_param.RangeMax

    def range_max_validity(self, value: int = None) -> int:
        if value is not None:
            self.real_param.RangeMaxValidity = value
            return self
        return self.real_param.RangeMaxValidity

    def range_min(self, value: float = None) -> float:
        if value is not None:
            self.real_param.RangeMin = value
            return self
        return self.real_param.RangeMin

    def range_min_validity(self, value: int = None) -> int:
        if value is not None:
            self.real_param.RangeMinValidity = value
            return self
        return self.real_param.RangeMinValidity

    def value(self, value: float = None) -> float:
        if value is not None:
            self.real_param.Value = value
            return self
        return self.real_param.Value

    def get_enumerate_values(self, o_safe_array: tuple) -> tuple:
        return self.real_param.GetEnumerateValues(o_safe_array)

    def get_enumerate_values_size(self) -> int:
        return self.real_param.GetEnumerateValuesSize()

    def is_equal_to(self, i_value_to_compare: float) -> bool:
        return self.real_param.IsEqualTo(i_value_to_compare)

    def set_enumerate_values(self, i_safe_array: tuple) -> 'RealParam':
        self.real_param.SetEnumerateValues(i_safe_array)
        return self

    def suppress_enumerate_values(self) -> 'RealParam':
        self.real_param.SuppressEnumerateValues()
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'