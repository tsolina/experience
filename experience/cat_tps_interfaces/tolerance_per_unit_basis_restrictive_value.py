from experience.system import AnyObject

class TolerancePerUnitBasisRestrictiveValue(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TolerancePerUnitBasisRestrictiveValue
    """

    def __init__(self, com):
        super().__init__(com)
        self.tolerance_per_unit_basis_restrictive_value = com

    def value(self) -> float:
        return self.tolerance_per_unit_basis_restrictive_value.Value

    def __repr__(self):
        return f'TolerancePerUnitBasisRestrictiveValue(name="{ self.name }")'
