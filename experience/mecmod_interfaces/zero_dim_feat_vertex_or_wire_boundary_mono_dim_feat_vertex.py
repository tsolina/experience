from experience.mecmod_interfaces.vertex import Vertex

class ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex(Vertex):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfModelInterfaces.Reference
                |                         CATMmrAutomationInterfaces.Boundary
                |                             CATMmrAutomationInterfaces.Vertex
                |                                 ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex
    """

    def __init__(self, com):
        super().__init__(com)
        self.zero_dim_feat_vertex_or_wire_boundary_mono_dim_feat_vertex = com