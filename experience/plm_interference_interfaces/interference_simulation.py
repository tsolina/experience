from typing import Iterator, TYPE_CHECKING, Union

from .plm_interference_types import *
from experience.system import AnyObject
from experience.plm_modeler_base_interfaces.plm_entity import PLMEntity

if TYPE_CHECKING:
    from experience.plm_interference_interfaces.interference_group_objects import InterferenceGroupObjects
    from experience.plm_interference_interfaces.interference_results import InterferenceResults

class InterferenceSimulation(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         InterferenceSimulation
    """

    def __init__(self, com):
        super().__init__(com)
        self.interference_simulation = com

    def clearance_value(self, value: float = None) -> Union['InterferenceSimulation', float]:
        if value is not None:
            self.interference_simulation.ClearanceValue = value
            return self
        return self.interference_simulation.ClearanceValue
    
    def first_group_objects(self) -> 'InterferenceGroupObjects':
        '''
        deprecated: use GetGroupObjects instead
        '''
        from experience.plm_interference_interfaces.interference_group_objects import InterferenceGroupObjects
        return InterferenceGroupObjects(self.interference_simulation.FirstGroupObjects)
    
    def group_computation_type(self, value: CatInterferenceGroupComputationType = None) -> Union['InterferenceSimulation', CatInterferenceGroupComputationType]:
        '''
        deprecated: use GroupComputationType2 instead
        '''
        if value is not None:
            self.interference_simulation.GroupComputationType = int(value)
            return self
        return CatInterferenceGroupComputationType.item(self.interference_simulation.GroupComputationType)
    
    def group_computation_type2(self, value: CatInterferenceGroupComputationType2 = None) -> Union['InterferenceSimulation', CatInterferenceGroupComputationType2]:
        if value is not None:
            self.interference_simulation.GroupComputationType2 = int(value)
            return self
        return CatInterferenceGroupComputationType2.item(self.interference_simulation.GroupComputationType2)
    
    def interference_comparison(self, value: CatInterferenceComparison = None) -> Union['InterferenceSimulation', CatInterferenceComparison]:
        if value is not None:
            self.interference_simulation.InterferenceComparison = int(value)
            return self
        return CatInterferenceComparison.item(self.interference_simulation.InterferenceComparison)
    
    def interference_intermediate_representation(self, value: CatInterferenceIntermediateRepresentation = None) -> Union['InterferenceSimulation', CatInterferenceIntermediateRepresentation]:
        if value is not None:
            self.interference_simulation.InterferenceIntermediateRepresentation = int(value)
            return self
        return CatInterferenceIntermediateRepresentation.item(self.interference_simulation.InterferenceIntermediateRepresentation)  
    
    def interference_results(self) -> 'InterferenceResults':
        from experience.plm_interference_interfaces.interference_results import InterferenceResults
        return InterferenceResults(self.interference_simulation.InterferenceResults)
    
    def interference_specification_type(self, value: CatInterferenceSpecificationType = None) -> Union['InterferenceSimulation', CatInterferenceSpecificationType]:
        if value is not None:
            self.interference_simulation.InterferenceSpecificationType = int(value)
            return self
        return CatInterferenceSpecificationType.item(self.interference_simulation.InterferenceSpecificationType)
    
    def second_group_objects(self) -> 'InterferenceGroupObjects':
        '''
        deprecated: use GetGroupObjects instead
        '''
        from experience.plm_interference_interfaces.interference_group_objects import InterferenceGroupObjects
        return InterferenceGroupObjects(self.interference_simulation.SecondGroupObjects)
    
    def add_compute_quantifier(self, i_quantifier_mode: CatInterferenceComputeQuantifier) -> 'InterferenceSimulation':
        self.interference_simulation.AddComputeQuantifier(int(i_quantifier_mode))
        return self
    
    def add_group_objects(self) -> 'InterferenceGroupObjects':
        from experience.plm_interference_interfaces.interference_group_objects import InterferenceGroupObjects
        group = self._get_multi([self.interference_simulation],
                                 ('InterferenceSimulation', 'AddGroupObjects'),
                                 ('InterferenceGroupObjects'))
        return [AnyObject(obj) for obj in group]
    
    def add_itf_specification_type_eng_cnx(self, i_type_eng_cnx: CatInterferenceSpecificationTypeEngCnx) -> 'InterferenceSimulation':
        self.interference_simulation.AddItfSpecificationTypeEngCnx(int(i_type_eng_cnx))
        return self
    
    def execute(self) -> 'InterferenceSimulation':
        self.interference_simulation.Execute()
        return self
    
    def get_group_objects(self, i_index: int) -> 'InterferenceGroupObjects':
        from experience.plm_interference_interfaces.interference_group_objects import InterferenceGroupObjects
        group = self._get_multi([self.interference_simulation],
                                 ('InterferenceSimulation', 'GetGroupObjects'),
                                 ('InterferenceGroupObjects'))
        return [AnyObject(obj) for obj in group]
    
    def get_number_of_group_objects(self) -> int:
        return self.interference_simulation.GetNumberOfGroupObjects()
    
    def get_rule_set_name(self) -> str:
        return self._get_multi([self.interference_simulation],
                                 ('InterferenceSimulation', 'GetRuleSetName'),
                                 ('String'))
    
    def is_active_compute_quantifier(self, i_quantifier_mode: CatInterferenceComputeQuantifier) -> bool:
        return self._get_multi([self.interference_simulation], int(i_quantifier_mode),
                                 ('InterferenceSimulation', 'IsActiveComputeQuantifier', 'CatInterferenceComputeQuantifier'),
                                 ('Boolean'))
    
    def is_active_itf_specification_type_eng_cnx(self, i_type_eng_cnx: CatInterferenceSpecificationTypeEngCnx) -> bool:
        return self._get_multi([self.interference_simulation], int(i_type_eng_cnx),
                                 ('InterferenceSimulation', 'IsActiveItfSpecificationTypeEngCnx', 'CatInterferenceSpecificationTypeEngCnx'),
                                 ('Boolean')) 
    
    def is_compute_quantifier_available(self, i_quantifier_mode: CatInterferenceComputeQuantifier) -> bool:
        return self._get_multi([self.interference_simulation], int(i_quantifier_mode),
                                 ('InterferenceSimulation', 'IsComputeQuantifierAvailable', 'CatInterferenceComputeQuantifier'),
                                 ('Boolean'))
    
    def put_rule_set_by_name(self, i_rule_set_name: str) -> 'InterferenceSimulation':
        self.interference_simulation.PutRuleSetByName(i_rule_set_name)
        return self
    
    def remove_compute_quantifier(self, i_quantifier_mode: CatInterferenceComputeQuantifier) -> 'InterferenceSimulation':
        self.interference_simulation.RemoveComputeQuantifier(int(i_quantifier_mode))
        return self
    
    def remove_group_objects(self, i_index: int) -> 'InterferenceSimulation':
        self.interference_simulation.RemoveGroupObjects(i_index)
        return self
    
    def remove_itf_specification_tpye_eng_cnx(self, i_type_eng_cnx: CatInterferenceSpecificationTypeEngCnx) -> 'InterferenceSimulation':
        self.interference_simulation.RemoveItfSpecificationTypeEngCnx(int(i_type_eng_cnx))
        return self
    
    def remove_rule_set(self) -> 'InterferenceSimulation':
        self.interference_simulation.RemoveRuleSet()
        return self
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
