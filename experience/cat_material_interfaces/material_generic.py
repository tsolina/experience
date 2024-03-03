from experience.plm_modeler_base_interfaces.plm_entity import PLMEntity

class MaterialGeneric(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         MaterialGeneric
    """

    def __init__(self, com):
        super().__init__(com)
        self.material_generic = com