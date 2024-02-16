from experience.system import AnyObject


class DimensionLimit(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DimensionLimit
    """

    def __init__(self, com):
        super().__init__(com)
        self.dimension_limit = com

    def dimension_limit_type(self, value: str = None) -> str:
        if value is not None:
            self.dimension_limit.DimensionLimitType = value
            return self
        return self.dimension_limit.DimensionLimitType

    def modifier(self, value: str = None) -> str:
        if value is not None:
            self.dimension_limit.Modifier = value
            return self
        return self.dimension_limit.Modifier

    def nominal_value(self) -> float:
        return self.dimension_limit.Nominalvalue

    def symetric_value(self, value: bool = None) -> bool:
        if value is not None:
            self.dimension_limit.SymetricValue = value
            return self
        return self.dimension_limit.SymetricValue

    def tabulated_limit(self, value: str = None) -> str:
        if value is not None:
            self.dimension_limit.TabulatedLimit = value
            return self
        return self.dimension_limit.TabulatedLimit

    def limits(self) -> tuple: #, o_bottom: float, o_up: float
        return self.dimension_limit.Limits()

    def put_limits(self, i_bottom: float, i_up: float) -> 'DimensionLimit':
        self.dimension_limit.PutLimits(i_bottom, i_up)
        return self

    def __repr__(self):
        return f'DimensionLimit(name="{self.name()}")'
