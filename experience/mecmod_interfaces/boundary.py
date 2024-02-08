from experience.inf_interfaces import Reference

class Boundary(Reference):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Reference
                |                         Boundary
    """

    def __init__(self, com):
        super().__init__(com)
        self.boundary = com

    def __repr__(self):
        return f'Boundary(name="{self.name}")'