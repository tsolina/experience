from experience.system import AnyObject

class Slide(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Slide
    """

    def __init__(self, com):
        super().__init__(com)
        self.slide = com