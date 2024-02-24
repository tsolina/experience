from experience.mecmod_interfaces.vertex import Vertex

class TriDimFeatVertexOrBiDimFeatVertex(Vertex):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfModelInterfaces.Reference
                |                         CATMmrAutomationInterfaces.Boundary
                |                             CATMmrAutomationInterfaces.Vertex
                |                                 TriDimFeatVertexOrBiDimFeatVertex
    """

    def __init__(self, com):
        super().__init__(com)
        self.tri_dim_feat_vertex_or_bi_dim_feat_vertex = com