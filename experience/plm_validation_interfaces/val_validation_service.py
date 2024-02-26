from typing import TYPE_CHECKING

from experience.inf_interfaces import Service

if TYPE_CHECKING:
    from experience.plm_validation_interfaces import VALValidation

class VALValidationService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         VALValidationService
    """

    def __init__(self, com):
        super().__init__(com)
        self.val_validation_service = com

    def validation(self) -> 'VALValidation':
        from experience.plm_validation_interfaces import VALValidation
        return VALValidation(self.val_validation_service.Validation)