from experience.mecmod_interfaces.boundary import Boundary

class Edge(Boundary):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfModelInterfaces.Reference
                |                         CATMmrAutomationInterfaces.Boundary
                |                             Edge
    """

    def __init__(self, com):
        super().__init__(com)
        self.edge = com