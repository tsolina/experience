from experience.system import AnyObject

class TangentPlane(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TangentPlane
    """

    def __init__(self, com):
        super().__init__(com)
        self.tangent_plane = com

    def modifier(self) -> str:
        return self.tangent_plane.Modifier