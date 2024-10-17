from experience.types.enum_item import EnumItem

class CatDescriptionLengthType(EnumItem):
    ShortText = 0
    LongText = 1

class CatOutPutFormatType(EnumItem):
    KWEHtml = 0
    KWEText = 1
    KWEPrint = 2
    KWEEmail = 3

class CatShowResultType(EnumItem):
    ByRule = 0
    ByObject = 1
    ByState = 2

class CatSolveType(EnumItem):
    ManualSolveType = 0
    AutomaticOptimizedSolveType = 1
    AutomaticCompleteSolveType = 2

class CatVisualizationType(EnumItem):
    Passed = 0
    Failed = 1
    Both = 2

class CatWorkingMode(EnumItem):
    WholeObjects = 0
    OccurenceObjects = 1
    PLMObjects = 2
    AllOccurenceObjects = 3