from experience.mecmod_interfaces.bi_dim_feat_edge import BiDimFeatEdge

class RectilinearBiDimFeatEdge(BiDimFeatEdge):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfModelInterfaces.Reference
                |                         CATMmrAutomationInterfaces.Boundary
                |                             CATMmrAutomationInterfaces.Edge
                |                                 CATMmrAutomationInterfaces.BiDimFeatEdge
                |                                     RectilinearBiDimFeatEdge
    """

    def __init__(self, com):
        super().__init__(com)
        self.rectilinear_bi_dim_feat_edge = com

    def get_direction(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.rectilinear_bi_dim_feat_edge, "GetDirection", 2)
    
    def get_origin(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.rectilinear_bi_dim_feat_edge, "GetOrigin", 2)