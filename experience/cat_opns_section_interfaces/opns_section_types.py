from experience.types.enum_item import EnumItem

class CATSectioningMode(EnumItem):
    CatSectionCrossView = 0
    CatSectionCutView = 1

class CATSectioningPlaneVisuMode(EnumItem):
    CatSectionContourAndPlane = 0
    CatSectionOnlyContour = 1
    CatSectionContourAndGridPlane = 2

class CatSectionBehavior(EnumItem):
    catSectionBehaviorAutomatic = 0
    catSectionBehaviorFreeze = 1
    catSectionBehaviorManual = 2

class CatSectionType(EnumItem):
    catSectionTypePlane = 0
    catSectionTypeSlice = 1
    catSectionTypeBox = 2
