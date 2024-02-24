from experience.mecmod_interfaces.edge import Edge

class MonoDimFeatEdge(Edge):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfModelInterfaces.Reference
                |                         CATMmrAutomationInterfaces.Boundary
                |                             CATMmrAutomationInterfaces.Edge
                |                                 MonoDimFeatEdge
    """

    def __init__(self, com):
        super().__init__(com)
        self.mono_dim_feat_edge = com