from experience.mecmod_interfaces.face import Face

class PlanarFace(Face):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfModelInterfaces.Reference
                |                         CATMmrAutomationInterfaces.Boundary
                |                             CATMmrAutomationInterfaces.Face
                |                                 PlanarFace
    """

    def __init__(self, com):
        super().__init__(com)
        self.planar_face = com

    def get_first_axis(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.planar_face, "GetFirstAxis", 2)
    
    def get_origin(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.planar_face, "GetOrigin", 2)
    
    def get_second_axis(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.planar_face, "GetSecondAxis", 2)