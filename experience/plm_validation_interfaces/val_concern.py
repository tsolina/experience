from experience.plm_modeler_base_interfaces.plm_entity import PLMEntity
from experience.system.any_object import AnyObject

class VALConcern(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         VALConcern
    """

    def __init__(self, com):
        super().__init__(com)
        self.val_concern = com

    def published(self, value: AnyObject = None) -> AnyObject:
        if value is not None:
            self.val_concern.Published = value._com
            return self
        return AnyObject(self.val_concern.Published)