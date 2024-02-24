from experience.mecmod_interfaces.boundary import Boundary

class Vertex(Boundary):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfModelInterfaces.Reference
                |                         CATMmrAutomationInterfaces.Boundary
                |                             Vertex
    """

    def __init__(self, com):
        super().__init__(com)
        self.vertex = com