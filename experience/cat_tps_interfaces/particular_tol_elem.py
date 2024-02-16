from experience.system import AnyObject

class ParticularTolElem(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ParticularTolElem
    """

    def __init__(self, com):
        super().__init__(com)
        self.particular_tol_elem = com


    def particular_geometry(self) -> str:
        return self.particular_tol_elem.ParticularGeometry

    def __repr__(self):
        return f'ParticularTolElem(name="{ self.name() }")'
