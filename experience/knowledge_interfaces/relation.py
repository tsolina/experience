from typing import TYPE_CHECKING, Union

from experience.knowledge_interfaces.knowledge_activate_object import KnowledgeActivateObject
from experience.system.any_object import AnyObject

if TYPE_CHECKING:
    from experience.knowledge_interfaces.parameter import Parameter

class Relation(KnowledgeActivateObject):
    def __init__(self, com):
        super().__init__(com)
        self.relation = com

    def comment(self, value: str = None) -> Union['Relation', str]:
        if value is not None:
            self.relation.Comment = value
            return self
        return self.relation.Comment

    def context(self) -> AnyObject:
        return AnyObject(self.relation.Context)

    def nb_in_parameters(self) -> int:
        return self.relation.NbInParameters

    def nb_out_parameters(self) -> int:
        return self.relation.NbOutParameters

    def value(self) -> str:
        return self.relation.Value

    def get_in_parameter(self, i_index: int) -> AnyObject:
        return AnyObject(self.relation.GetInParameter(i_index))

    def get_out_parameter(self, i_index: int) -> 'Parameter':
        from experience.knowledge_interfaces import Parameter
        return Parameter(self.relation.GetOutParameter(i_index))

    def modify(self, i_value: str) -> 'Relation':
        self.relation.Modify(i_value)
        return self

    def rename(self, i_name: str) -> 'Relation':
        self.relation.Rename(i_name)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'