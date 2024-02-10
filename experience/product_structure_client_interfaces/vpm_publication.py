from experience.plm_modeler_base_interfaces import PLMEntity

class VPMPublication(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMEntity
                |                       VPMPublication 
    """

    def __init__(self, com):
        super().__init__(com)
        self.vpm_publication = com

    def __repr__(self):
        return f'VPMPublication(name="{self.name}")'