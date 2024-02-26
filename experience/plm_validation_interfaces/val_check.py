from experience.plm_modeler_base_interfaces.plm_entity import PLMEntity

class VALCheck(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         VALCheck
    """

    def __init__(self, com):
        super().__init__(com)
        self.val_check = com