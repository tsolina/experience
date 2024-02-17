from experience.types.enum_item import EnumItem
from typing import Union

class KnowledgeObjectType(EnumItem):
    kweParametersSetObjectType = 1
    kweRelationsSetObjectType = 2
    kweOptimizationsSetObjectType = 3
    kweParameterObjectType = 4
    kweRelationObjectType = 5
    kweOptimizationObjectType = 6
    kweExpertRulebasesSetObjectType = 7
    kweExpertRulebaseObjectType = 8

class KnowledgeSetType(EnumItem):
    kweParametersType = 1
    kweRelationsType = 2
    kweOptimizationsType = 3
    kweRuleBasesType = 4

class KnowledgeSeverityType(EnumItem):
    Silent = 1
    Information = 2
    Warning = 3