from experience.mecmod_interfaces.vertex import Vertex

class NotWireBoundaryMonoDimFeatVertex(Vertex):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfModelInterfaces.Reference
                |                         CATMmrAutomationInterfaces.Boundary
                |                             CATMmrAutomationInterfaces.Vertex
                |                                 NotWireBoundaryMonoDimFeatVertex
    """

    def __init__(self, com):
        super().__init__(com)
        self.not_wire_boundary_mono_dim_feat_vertex = com