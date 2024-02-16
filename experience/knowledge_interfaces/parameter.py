from typing import TYPE_CHECKING
from experience.system.any_object import AnyObject

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Relation

class Parameter(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.parameter = com

    def comment(self, value: str = None) -> str:
        if value is not None:
            self.parameter.Comment = value
            return self
        return self.parameter.Comment

    def context(self, value: AnyObject = None) -> AnyObject:
        if value is not None:
            self.parameter.Context = value
            return self
        return AnyObject(self.parameter.Context)

    def hidden(self, value: bool = None):
        if value is not None:
            self.parameter.Hidden = value
            return self
        return self.parameter.Hidden

    def is_true_parameter(self) -> bool:
        return self.parameter.IsTrueParameter

    def optional_relation(self) -> 'Relation':
        from experience.knowledge_interfaces import Relation
        return Relation(self.parameter.OptionalRelation)

    def read_only(self) -> bool:
        return self.parameter.ReadOnly

    def renamed(self) -> bool:
        return self.parameter.Renamed

    def user_access_mode(self) -> int:
        return self.parameter.UserAccessMode

    def rename(self, i_name: str) -> 'Parameter':
        self.parameter.Rename(i_name)
        return self

    def valuate_from_string(self, i_value: str) -> 'Parameter':
        self.parameter.ValuateFromString(i_value)
        return self

    def value_as_string(self) -> str:
        return self.parameter.ValueAsString()

    def __repr__(self):
        return f'Parameter(name="{self.name()}")'
