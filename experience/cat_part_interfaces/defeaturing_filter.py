from experience.system import AnyObject


class DefeaturingFilter(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DefeaturingFilter
    """

    def __init__(self, com):
        super().__init__(com)
        self.defeaturing_filter = com

    def __repr__(self):
        return f'DefeaturingFilter(name="{self.name()}")'