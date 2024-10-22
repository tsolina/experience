from experience.types.enum_item import EnumItem

class CatInterferenceComparison(EnumItem):
    catInterferenceComparisonNone = 0
    catInterferenceComparisonRecomputeModify = 1
    catInterferenceComparisonDeleteOutOfScope = 2

class CatInterferenceComputeQuantifier(EnumItem):
    catInterferenceComputeQuantifierMinimumDistance = 0
    catInterferenceComputeQuantifierPenetrationVector = 1

class CatInterferenceGroupComputationType(EnumItem):
    catInterferenceGroupComputationTypeAllAgainstAllInGroup1 = 0
    catInterferenceGroupComputationTypeGroup1AgainstGroup2 = 1

class CatInterferenceGroupComputationType2(EnumItem):
    catInterferenceGroupComputationTypeAllAgainstAllInGroup = 0
    catInterferenceGroupComputationTypeGroupAgainstGroup = 1
    catInterferenceGroupComputationTypeGroupAgainstContext = 2
    catInterferenceGroupComputationTypeAllAgainstAllInContext = 3

class CatInterferenceIntermediateRepresentation(EnumItem):
    catInterferenceInterRepNone = 0
    catInterferenceInterRepAppend = 1
    catInterferenceInterRepComputeBetween = 2

class CatInterferenceResultStatus(EnumItem):
    catInterferenceResultStatusOK = 0
    catInterferenceResultStatusKO = 1
    catInterferenceResultStatusNotAnalyzed = 2

class CatInterferenceResultType(EnumItem):
    catInterferenceResultTypeClash = 0
    catInterferenceResultTypeContact = 1
    catInterferenceResultTypeClearance = 2
    catInterferenceResultTypeNoInterference = 3
    catInterferenceResultTypeUndefined = 4

class CatInterferenceResultUserType(EnumItem):
    catInterferenceResultUserTypeClash = 0
    catInterferenceResultUserTypeContact = 1
    catInterferenceResultUserTypeClearance = 2
    catInterferenceResultUserTypeNoInterference = 3
    catInterferenceResultUserTypeUndefined = 4

class CatInterferenceSpecificationType(EnumItem):
    catInterferenceSpecificationTypeNone = 0
    catInterferenceSpecificationTypeClash = 1
    catInterferenceSpecificationTypeClearance = 2
    catInterferenceSpecificationTypeClashWithoutContact = 3

class CatInterferenceSpecificationTypeEngCnx(EnumItem):
    catInterferenceSpecificationTypeEngCnxCheckNone = 0
    catInterferenceSpecificationTypeEngCnxCheckNoClash = 1
    catInterferenceSpecificationTypeEngCnxCheckContact = 2
    catInterferenceSpecificationTypeEngCnxCheckClearance = 3
    catInterferenceSpecificationTypeEngCnxNoCheck = 4