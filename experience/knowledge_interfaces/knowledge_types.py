from experience.types.enum_item import EnumItem
from typing import Union

class KnowledgeObjectType(EnumItem):
    kweParametersSetObjectType = 0
    kweRelationsSetObjectType = 1
    kweOptimizationsSetObjectType = 2
    kweParameterObjectType = 3
    kweRelationObjectType = 4
    kweOptimizationObjectType = 5
    kweExpertRulebasesSetObjectType = 6
    kweExpertRulebaseObjectType = 7

class KnowledgeSetType(EnumItem):
    kweParametersType = 0
    kweRelationsType = 1
    kweOptimizationsType = 2
    kweRuleBasesType = 3

class KnowledgeSeverityType(EnumItem):
    Silent = 0
    Information = 1
    Warning = 2