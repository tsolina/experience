from typing import Union, TYPE_CHECKING

from experience.know_how_interfaces.know_how_types import *

from experience.knowledge_interfaces.relation import Relation
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.know_how_interfaces import ExpertRuleBase, ExpertRuleSet

class ExpertRuleBaseRuntime(Relation):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                         KnowledgeIDLItf.KnowledgeActivateObject
                |                             KnowledgeIDLItf.Relation
                |                                 ExpertRuleBaseRuntime
    """

    def __init__(self, com):
        super().__init__(com)
        self.expert_rule_base_runtime = com

    def report_description_length(self, value: CatDescriptionLengthType = None) -> Union['ExpertRuleBaseRuntime', CatDescriptionLengthType]:
        if value is not None:
            self.expert_rule_base_runtime.ReportDescriptionLength = int(value)
            return self
        return CatDescriptionLengthType.item(self.expert_rule_base_runtime.ReportDescriptionLength)
    
    def report_out_put_format(self, value: CatOutPutFormatType = None) -> Union['ExpertRuleBaseRuntime', CatOutPutFormatType]:
        if value is not None:
            self.expert_rule_base_runtime.ReportOutPutFormat = int(value)
            return self
        return CatOutPutFormatType.item(self.expert_rule_base_runtime.ReportOutPutFormat)
    
    def report_path(self, value: str = None) -> Union['ExpertRuleBaseRuntime', str]:
        if value is not None:
            self.expert_rule_base_runtime.ReportPath = value
            return self
        return self.expert_rule_base_runtime.ReportPath
    
    def report_show_result(self, value: CatShowResultType = None) -> Union['ExpertRuleBaseRuntime', CatShowResultType]:
        if value is not None:
            self.expert_rule_base_runtime.ReportShowResult = int(value)
            return self
        return CatShowResultType.item(self.expert_rule_base_runtime.ReportShowResult)
    
    def rule_base_edition(self) -> 'ExpertRuleBase':
        from experience.know_how_interfaces.expert_rule_base import ExpertRuleBase
        return ExpertRuleBase(self.expert_rule_base_runtime.RuleBaseEdition)
    
    def rule_set(self) -> 'ExpertRuleSet':
        from experience.know_how_interfaces import ExpertRuleSet
        return ExpertRuleSet(self.expert_rule_base_runtime.RuleSet)
    
    def solve_type(self, value: CatSolveType = None) -> Union['ExpertRuleBaseRuntime', CatSolveType]:
        if value is not None:
            self.expert_rule_base_runtime.SolveType = int(value)
            return self
        return CatSolveType.item(self.expert_rule_base_runtime.SolveType)
    
    def text_visualization(self, value: CatVisualizationType = None) -> Union['ExpertRuleBaseRuntime', CatVisualizationType]:
        if value is not None:
            self.expert_rule_base_runtime.TextVisualization = int(value)
            return self
        return CatVisualizationType.item(self.expert_rule_base_runtime.TextVisualization)
    
    def working_mode(self, value: CatWorkingMode = None) -> Union['ExpertRuleBaseRuntime', CatWorkingMode]:
        if value is not None:
            self.expert_rule_base_runtime.WorkingMode = int(value)
            return self
        return CatWorkingMode.item(self.expert_rule_base_runtime.WorkingMode)
    
    def accurate_type(self) -> str:
        return self.expert_rule_base_runtime.AccurateType()
    
    def add_fact(self, i_fact: AnyObject) -> 'ExpertRuleBaseRuntime':
        self.expert_rule_base_runtime.AddFact(i_fact._com)
        return self
    
    def add_root_of_facts(self, i_root_facts: AnyObject) -> 'ExpertRuleBaseRuntime':
        self.expert_rule_base_runtime.AddRootOfFacts(i_root_facts._com)
        return self

    def deduce(self) -> 'ExpertRuleBaseRuntime':
        self.expert_rule_base_runtime.Deduce()
        return self
    
    def fingerprint(self) -> bool:
        return self.expert_rule_base_runtime.Fingerprint()
    
    def get_number_of_roots_of_facts(self) -> int:
        return self.expert_rule_base_runtime.GetNumberOfRootsOfFacts()
    
    def get_root_of_facts(self) -> tuple:
        # to test
        return self._get_multi([self.expert_rule_base_runtime], ('ExpertRuleBaseRuntime', 'GetRootsOfFacts'), ('Variant'))
    
    def import_(self, i_rule_set: 'ExpertRuleSet', i_force: bool) -> 'ExpertRuleBaseRuntime':
        self.expert_rule_base_runtime.Import(i_rule_set._com, i_force)
        return self
    
    def reload_fact(self, i_fact: AnyObject) -> 'ExpertRuleBaseRuntime':
        self.expert_rule_base_runtime.ReloadFact(i_fact._com)
        return self
    
    def remove_fact(self, i_fact: AnyObject) -> 'ExpertRuleBaseRuntime':
        self.expert_rule_base_runtime.RemoveFact(i_fact._com)
        return self
    
    def remove_root_of_facts(self, i_root_facts: AnyObject) -> 'ExpertRuleBaseRuntime':
        self.expert_rule_base_runtime.RemoveRootOfFacts(i_root_facts._com)
        return self
    
    def report(self, really_start_browser: bool) -> 'ExpertRuleBaseRuntime':
        self.expert_rule_base_runtime.Report(really_start_browser)
        return self
    
    def solve(self, i_complete_solve: bool) -> 'ExpertRuleBaseRuntime':
        self.expert_rule_base_runtime.Solve(i_complete_solve)
        return self 
    
    def solve_with_load(self, i_complete_solve: bool) -> 'ExpertRuleBaseRuntime':
        self.expert_rule_base_runtime.SolveWithLoad(i_complete_solve)
        return self 

    def synchronize_status(self) -> bool:
        return self.expert_rule_base_runtime.SynchronizeStatus()

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'