from typing import Iterator, TYPE_CHECKING, Union

from .plm_interference_types import *
from experience.system import AnyObject
from experience.plm_modeler_base_interfaces.plm_entity import PLMEntity

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces.vpm_occurence import VPMOccurrence
    from experience.plm_modeler_base_interfaces.plm_occurrence import PLMOccurrence

class InterferenceResult(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         InterferenceResult
    """

    def __init__(self, com):
        super().__init__(com)
        self.interference_result = com

    def analysis_status(self, value: CatInterferenceResultStatus = None) -> Union['InterferenceResult' ,CatInterferenceResultStatus]:
        if value is not None:
            self.interference_result.AnalysisStatus = int(value)
            return self
        return CatInterferenceResultStatus.item(self.interference_result.AnalysisStatus)
    
    def first_product(self) -> 'PLMOccurrence':
        from experience.plm_modeler_base_interfaces.plm_occurrence import PLMOccurrence
        return PLMOccurrence(self.interference_result.FirstProduct)
    
    def second_product(self) -> 'PLMOccurrence':
        from experience.plm_modeler_base_interfaces.plm_occurrence import PLMOccurrence
        return PLMOccurrence(self.interference_result.SecondProduct)
    
    def type(self) -> CatInterferenceResultType:
        return CatInterferenceResultType.item(self.interference_result.Type)
    
    def user_comment(self) -> str:
        return self.interference_result.UserComment
    
    def user_type(self, value: CatInterferenceResultUserType = None) -> Union['InterferenceResult' ,CatInterferenceResultUserType]:
        if value is not None:
            self.interference_result.UserType = int(value)
            return self
        return CatInterferenceResultUserType.item(self.interference_result.UserType)
    
    def compute_picture(self, i_full_path: str, i_format: str, i_width: int, i_height: int) -> 'InterferenceResult':
        self.interference_result.ComputePicture(i_full_path, i_format, i_width, i_height)
        return self
    
    def get_geometrical_values(self) -> tuple[list, list, float]:
        return self._get_multi([self.interference_result], ('InterferenceResult', 'GetGeometricalValues'), ("Variant", "Variant", "Double"))
    
    def get_intersection_volume(self) -> tuple[list, float]:
        return self._get_multi([self.interference_result], ('InterferenceResult', 'GetIntersectionVolume'), ("Variant", "Double"))
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'