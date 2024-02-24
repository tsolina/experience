from typing import Union, Optional, TYPE_CHECKING

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.plm_modeler_base_interfaces import PLMEntity, PLMOccurrences

class PLMOccurrence(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMOccurrence
    """

    def __init__(self, com):
        super().__init__(com)
        self.plm_occurrence = com

    def plm_entity(self) -> 'PLMEntity':
        from experience.plm_modeler_base_interfaces import PLMEntity
        return PLMEntity(self.plm_occurrence.PLMEntity)
    
    def plm_occurrences(self) -> 'PLMOccurrences':
        from experience.plm_modeler_base_interfaces import PLMOccurrences
        return PLMOccurrences(self.plm_occurrence.PLMOccurrences) 