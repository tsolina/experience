from experience.system import AnyObject

class ToleranceZone(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ToleranceZone
    """

    def __init__(self, com):
        super().__init__(com)
        self.tolerance_zone = com

    def form(self) -> str:
        return self.tolerance_zone.Form

    def validated_tolerance_value(self, value: bool = None):
        if value is not None:
            self.tolerance_zone.ValidatedToleranceValue = value
            return self
        return self.tolerance_zone.ValidatedToleranceValue

    def value(self) -> float:
        return self.tolerance_zone.Value

    def __repr__(self):
        return f'ToleranceZone(name="{ self.name }")'
