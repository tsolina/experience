from typing import TYPE_CHECKING

# from experience.knowledge_interfaces import Parameters
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.knowledge_interfaces import ParameterSets

class ParameterSet(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ParameterSet
    """

    def __init__(self, com):
        super().__init__(com)
        self.parameter_set = com

    def all_parameters(self) -> list:
        from .parameter import Parameter
        items = []
        for i in range(0, self.parameter_set.AllParameters.Count):
            items.append(Parameter(self.parameter_set.AllParameters.Item(i + 1)))
        return items

    def direct_parameters(self) -> 'Parameters':
        from experience.knowledge_interfaces import Parameters
        return Parameters(self.parameter_set.DirectParameters)

    def parameter_sets(self) -> 'ParameterSets':
        from experience.knowledge_interfaces import ParameterSets
        return ParameterSets(self.parameter_set.ParameterSets)

    def __repr__(self):
        return f'ParameterSet(name="{self.name}")'
