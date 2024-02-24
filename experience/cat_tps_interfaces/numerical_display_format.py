from experience.system import AnyObject

class NumericalDisplayFormat(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Noa
    """

    def __init__(self, com):
        super().__init__(com)
        self.numerical_display_format = com

    def available_display_factor(self, value : int = None):
        if value is not None:
            self.numerical_display_format.AvailableDisplayFactor = value
            return self
        return self.numerical_display_format.AvailableDisplayFactor

    def display_factor(self, value : int = None):
        if value is not None:
            self.numerical_display_format.DisplayFactor = value
            return self
        return self.numerical_display_format.DisplayFactor

    def display_leading_zero(self, value : int = None):
        if value is not None:
            self.numerical_display_format.DisplayLeadingZero = value
            return self
        return self.numerical_display_format.DisplayLeadingZero

    def display_trailing_zero(self, value : int = None):
        if value is not None:
            self.numerical_display_format.DisplayTrailingZero = value
            return self
        return self.numerical_display_format.DisplayTrailingZero

    def format_name(self, value : str = None):
        if value is not None:
            self.numerical_display_format.FormatName = value
            return self
        return self.numerical_display_format.FormatName

    def precision(self, value : int = None):
        if value is not None:
            self.numerical_display_format.Precision = value
            return self
        return self.numerical_display_format.Precision

    def separator(self, value : int = None):
        if value is not None:
            self.numerical_display_format.Separator = value
            return self
        return self.numerical_display_format.Separator