from experience.mecmod_interfaces.edge import Edge

class BiDimFeatEdge(Edge):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfModelInterfaces.Reference
                |                         CATMmrAutomationInterfaces.Boundary
                |                             CATMmrAutomationInterfaces.Edge
                |                                 BiDimFeatEdge
    """

    def __init__(self, com):
        super().__init__(com)
        self.bi_dim_feat_edge = com