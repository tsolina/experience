from experience.system import AnyObject

class Measure(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Measure
    """

    def __init__(self, com):
        super().__init__(com)
        self.measure = com

    def minimum_distance(self) -> float:
        return self.measure.MinimumDistance()

    def __repr__(self):
        return f'Measure(name="{self.name()}")'
