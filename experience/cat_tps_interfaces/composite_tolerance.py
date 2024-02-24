from experience.system import AnyObject

class CompositeTolerance(AnyObject):

    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CompositeTolerance
    """

    def __init__(self, com):
        super().__init__(com)
        self.composite_tolerance = com

    def box_count(self) -> float:
        return self.composite_tolerance.BoxCount

    def value(self) -> float:
        return self.composite_tolerance.Value