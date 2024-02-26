from typing import TYPE_CHECKING
from experience.plm_modeler_base_interfaces.plm_entity import PLMEntity
from experience.plm_validation_interfaces.plm_validation_types import *

if TYPE_CHECKING:
    from experience.plm_validation_interfaces import VALChecks, VALConcerns, VALContexts, VALReviews

class VALValidation(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         VALValidation
    """

    def __init__(self, com):
        super().__init__(com)
        self.val_validation = com

    def checks(self) -> 'VALChecks':
        from experience.plm_validation_interfaces import VALChecks
        return VALChecks(self.val_validation.Checks)
    
    def concerns(self) -> 'VALConcerns':
        from experience.plm_validation_interfaces import VALConcerns
        return VALConcerns(self.val_validation.Concerns)
    
    def contexts(self) -> 'VALContexts':
        from experience.plm_validation_interfaces import VALContexts
        return VALContexts(self.val_validation.Contexts)
    
    def reviews(self) -> 'VALReviews':
        from experience.plm_validation_interfaces import VALReviews
        return VALReviews(self.val_validation.Reviews)
    
    def type(self) -> PLMValidationType:
        return PLMValidationType.item(self.val_validation.Type)
