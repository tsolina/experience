from experience.system.any_object import AnyObject

class AppliedMaterial(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMaterialIDLItf.MaterialDomainContent
                |                         AppliedMaterial
    """

    def __init__(self, com):
        super().__init__(com)
        self.applied_material = com