from typing import Iterator, TYPE_CHECKING

from experience.system import Collection, AnyObject

if TYPE_CHECKING:
    from experience.types import cat_variant
    from experience.plm_modeler_base_interfaces.plm_occurrence import PLMOccurrence
    from experience.product_structure_client_interfaces.vpm_occurence import VPMOccurrence

class InterferenceGroupObjects(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     InterferenceGroupObjects
    """

    def __init__(self, com):
        super().__init__(com, child=AnyObject)
        self.interference_group_objects = com

    def add(self, i_plm_occurrence: 'PLMOccurrence') -> 'InterferenceGroupObjects':
        '''
        deprecated : use add2 instead
        '''
        self.interference_group_objects.Add(i_plm_occurrence._com)
        return self

    def add2(self, i_vpm_occurrence: 'VPMOccurrence') -> 'InterferenceGroupObjects':
        self.interference_group_objects.Add2(i_vpm_occurrence._com)
        return self

    def item(self, i_index: 'cat_variant') -> AnyObject:
        return AnyObject(self.interference_group_objects.Item(i_index))

    def remove(self, i_plm_occurrence: 'PLMOccurrence') -> 'InterferenceGroupObjects':
        '''
        deprecated: use remove2 instead
        '''
        self.interference_group_objects.Remove(i_plm_occurrence._com)
        return self
    
    def remove2(self, i_vpm_occurrence: 'VPMOccurrence') -> 'InterferenceGroupObjects':
        self.interference_group_objects.Remove2(i_vpm_occurrence._com)
        return self

    def __getitem__(self, n: int) -> AnyObject:
        if (n + 1) > self.count():
            raise StopIteration

        return AnyObject(self.interference_group_objects.item(n + 1))

    def __iter__(self) -> Iterator[AnyObject]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
