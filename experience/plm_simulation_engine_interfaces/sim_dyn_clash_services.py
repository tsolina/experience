from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject
from experience.inf_interfaces.service import Service

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces.vpm_occurence import VPMOccurrence

class SIMDynClashServices(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         SIMDynClashServices
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_dyn_clash_services = com

    def clash_analysis_mode(self, value: bool = None) -> Union['SIMDynClashServices', bool]:
        if value is not None:
            self.sim_dyn_clash_services.ClashAnalysisMode = value
            return self
        return self.sim_dyn_clash_services.ClashAnalysisMode
    
    def clash_status(self) -> bool:
        return self.sim_dyn_clash_services.ClashStatus
    
    def clearance_analysis_mode(self, value: bool = None) -> Union['SIMDynClashServices', bool]:
        if value is not None:
            self.sim_dyn_clash_services.ClearanceAnalysisMode = value
            return self
        return self.sim_dyn_clash_services.ClearanceAnalysisMode
    
    def contact_analysis_mode(self) -> bool:
        return self.sim_dyn_clash_services.ContactAnalysisMode
    
    def penetration_reporting(self, value: bool = None) -> Union['SIMDynClashServices', bool]:
        if value is not None:
            self.sim_dyn_clash_services.PenetrationReporting = value
            return self
        return self.sim_dyn_clash_services.PenetrationReporting
    
    def add_exclusion_object(self, i_object: AnyObject) -> int:
        return self.sim_dyn_clash_services.AddExclusionObject(i_object._com)
    
    def get_exlusion_list(self) -> tuple[list[AnyObject], int]:
        rVal = self._get_multi_with_result([self.sim_dyn_clash_services],
                                           ('SIMDynClashServices', 'GetExclusionList'),
                                           ('Variant'), 'Long')
        return rVal[0], [AnyObject(obj) for obj in rVal[1]]

    def locate_exclusion_object(self, i_object: AnyObject) -> int:
        return self.sim_dyn_clash_services.LocateExclusionObject(i_object._com)
    
    def remove_exclusion_object(self, i_object: AnyObject) -> int:
        return self.sim_dyn_clash_services.RemoveExclusionObject(i_object)
    
    def retrieve_results(self) -> tuple[list[AnyObject], int]:
        rVal = self._get_multi_with_result([self.sim_dyn_clash_services],
                                           ('SIMDynClashServices', 'RetrieveResults'),
                                           ('Variant'), 'Long')
        return rVal[0], [AnyObject(obj) for obj in rVal[1]]
    
    def update_clash_agent(self) -> 'SIMDynClashServices':
        self.sim_dyn_clash_services.UpdateClashAgent()
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'