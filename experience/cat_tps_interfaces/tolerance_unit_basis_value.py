from experience.system import AnyObject

class ToleranceUnitBasisValue(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ToleranceUnitBasisValue
    """

    def __init__(self, com):
        super().__init__(com)
        self.tolerance_unit_basis_value = com

    def set_values(self, i_value1: float, i_value2: float) -> 'ToleranceUnitBasisValue':
        self.tolerance_unit_basis_value.SetValues(i_value1, i_value2)
        return self

    def values(self) -> None: #', o_value1: float, o_value2: float'
        return self.tolerance_unit_basis_value.Values()