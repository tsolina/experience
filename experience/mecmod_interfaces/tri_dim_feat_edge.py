from experience.mecmod_interfaces.edge import Edge

class TriDimFeatEdge(Edge):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfModelInterfaces.Reference
                |                         CATMmrAutomationInterfaces.Boundary
                |                             CATMmrAutomationInterfaces.Edge
                |                                 TriDimFeatEdge
    """

    def __init__(self, com):
        super().__init__(com)
        self.tri_dim_feat_edge = com