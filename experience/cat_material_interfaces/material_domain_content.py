from experience.system import AnyObject

class MaterialDomainContent(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MaterialDomainContent
    """

    def __init__(self, com):
        super().__init__(com)
        self.material_domain_content = com