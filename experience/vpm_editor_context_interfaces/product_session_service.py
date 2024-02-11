from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Service

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces import Shape3Ds, VPMRootOccurrence

class ProductSessionService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         ProductSessionService
    """

    def __init__(self, com):
        super().__init__(com)
        self.product_session_service = com
    
    def shapes_3ds(self) -> 'Shape3Ds':
        return Shape3Ds(self.product_session_service.Shape3Ds)

    def compare_root_occurrences(self, i_first_root_occurrence: 'VPMRootOccurrence', i_second_root_occurrence: 'VPMRootOccurrence') -> int:
        """ r_val:  
        enum CatCompareOccurrenceResult {
        catDifferentObjects,
        catIdenticalOccurrence,
        catIdenticalReference
        }  
        """
        return self.product_session_service.CatCompareOccurrenceResult(i_first_root_occurrence, i_second_root_occurrence)

    def __repr__(self):
        return f'ProductSessionService(name="{self.name()}")'