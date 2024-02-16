from experience.system import AnyObject

class OriginElements(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OriginElements
    """

    def __init__(self, com):
        super().__init__(com)
        self.origin_elements = com

    def plane_xy(self) -> AnyObject:
        return AnyObject(self.origin_elements.PlaneXY)

    def plane_yz(self) -> AnyObject:
        return AnyObject(self.origin_elements.PlaneYZ)

    def plane_zx(self) -> AnyObject:
        return AnyObject(self.origin_elements.PlaneZX)

    def __repr__(self):
        return f'OriginElements(name="{ self.name() }")'