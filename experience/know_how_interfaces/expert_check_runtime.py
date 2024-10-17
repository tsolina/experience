from typing import Union, TYPE_CHECKING

from experience.know_how_interfaces.expert_rule_base_component_runtime import ExpertRuleBaseComponentRuntime

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.know_how_interfaces import ExpertCheck, ExpertReportObjects

class ExpertCheckRuntime(ExpertRuleBaseComponentRuntime):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ExpertCheckRuntime
    """

    def __init__(self, com):
        super().__init__(com)
        self.expert_check_runtime = com

    def automatic_correct(self, value: bool = None) -> Union['ExpertCheckRuntime', bool]:
        if value is not None:
            self.expert_check_runtime.AutomaticCorrect = value
            return self
        return self.expert_check_runtime.AutomaticCorrect
    
    def check_edition(self) -> 'ExpertCheck':
        from experience.know_how_interfaces.expert_check import ExpertCheck
        return ExpertCheck(self.expert_check_runtime.CheckEdition)
    
    def correct_function(self, value: str = None) -> Union['ExpertCheckRuntime', str]:
        if value is not None:
            self.expert_check_runtime.CorrectFunction = value
            return self
        return self.expert_check_runtime.CorrectFunction

    def correct_function_comment(self, value: str = None) -> Union['ExpertCheckRuntime', str]:
        if value is not None:
            self.expert_check_runtime.CorrectFunctionComment = value
            return self
        return self.expert_check_runtime.CorrectFunctionComment
    
    def correct_function_type(self, value: int = None) -> Union['ExpertCheckRuntime', int]:
        if value is not None:
            self.expert_check_runtime.CorrectFunctionComment = value
            return self
        return self.expert_check_runtime.CorrectFunctionComment
    
    def failures(self) -> 'ExpertReportObjects':
        from experience.know_how_interfaces.expert_report_objects import ExpertReportObjects
        return ExpertReportObjects(self.expert_check_runtime.Failures)
    
    def help(self, value: str = None) -> Union['ExpertCheckRuntime', str]:
        if value is not None:
            self.expert_check_runtime.Help = value
            return self
        return self.expert_check_runtime.Help
    
    def justification(self, value: str = None) -> Union['ExpertCheckRuntime', str]:
        if value is not None:
            self.expert_check_runtime.Justification = value
            return self
        return self.expert_check_runtime.Justification
    
    def priority(self, value: float = None) -> Union['ExpertCheckRuntime', float]:
        if value is not None:
            self.expert_check_runtime.Priority = value
            return self
        return self.expert_check_runtime.Priority
    
    def succeeds(self) -> 'ExpertReportObjects':
        from experience.know_how_interfaces.expert_report_objects import ExpertReportObjects
        return ExpertReportObjects(self.expert_check_runtime.Succeeds)
    
    def correct(self) -> 'ExpertReportObjects':
        self.expert_check_runtime.Correct()
        return self
    
    def highlight(self) -> 'ExpertReportObjects':
        self.expert_check_runtime.Highlight()
        return self
    
    def status(self) -> int:
        return self.expert_check_runtime.Status()

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'