from experience.system import AnyObject

class Unit(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Unit
    """

    def __init__(self, com):
        super().__init__(com)
        self.unit = com

    def magnitude(self) -> str:
        return self.unit.Magnitude

    def symbol(self) -> str:
        return self.unit.Symbol

    def convert_from_mks(self, i_value_in_mks: float) -> float:
        return self.unit.ConvertFromMKS(i_value_in_mks)

    def convert_from_storage_unit(self, i_value_in_storage_unit: float) -> float:
        return self.unit.ConvertFromStorageUnit(i_value_in_storage_unit)

    def convert_to_mks(self, i_value_in_this_unit: float) -> float:
        return self.unit.ConvertToMKS(i_value_in_this_unit)

    def convert_to_storage_unit(self, i_value_in_this_unit: float) -> float:
        return self.unit.ConvertToStorageUnit(i_value_in_this_unit)

    def __repr__(self):
        return f'Unit(name="{ self.name }")'
