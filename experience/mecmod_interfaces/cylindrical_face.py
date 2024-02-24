from experience.mecmod_interfaces.face import Face

class CylindricalFace(Face):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfModelInterfaces.Reference
                |                         CATMmrAutomationInterfaces.Boundary
                |                             CATMmrAutomationInterfaces.Face
                |                                 CylindricalFace
    """

    def __init__(self, com):
        super().__init__(com)
        self.cylindrical_face = com

    def get_direction(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.cylindrical_face, "GetDirection", 2)
    
    def get_origin(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.cylindrical_face, "GetOrigin", 2)