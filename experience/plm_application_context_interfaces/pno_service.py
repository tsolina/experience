from typing import TYPE_CHECKING

from experience.inf_interfaces import Service

if TYPE_CHECKING:
    from experience.plm_application_context_interfaces import Person

class PnOService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         PnOService
    """

    def __init__(self, com):
        super().__init__(com)
        self.pno_service = com

    def person(self) -> 'Person':
        from experience.plm_application_context_interfaces import Person
        return Person(self.pno_service.Person)
