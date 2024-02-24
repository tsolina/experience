from experience.mecmod_interfaces.boundary import Boundary

class Face(Boundary):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfModelInterfaces.Reference
                |                         CATMmrAutomationInterfaces.Boundary
                |                             Face
    """

    def __init__(self, com):
        super().__init__(com)
        self.face = com