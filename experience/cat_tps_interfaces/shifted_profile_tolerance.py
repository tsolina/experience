from experience.system import AnyObject


class ShiftedProfileTolerance(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ShiftedProfileTolerance
    """

    def __init__(self, com):
        super().__init__(com)
        self.shifted_profile_tolerance = com

    def shift_value(self, value: float = None) -> float:
        if value is not None:
            self.shifted_profile_tolerance.ShiftValue = value
            return self
        return self.shifted_profile_tolerance.ShiftValue

    def get_shift_direction(self) -> tuple: #, op_direction: tuple
        return self.shifted_profile_tolerance.GetShiftDirection()

    def get_shift_side(self) -> tuple: #, op_point: tuple
        return self.shifted_profile_tolerance.GetShiftSide(op_point)

    def __repr__(self):
        return f'ShiftedProfileTolerance(name="{ self.name }")'
