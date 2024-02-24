from experience.types.enum_item import EnumItem

class CATAxisSystemAxisType(EnumItem):
    catAxisSystemAxisSameDirection = 0
    catAxisSystemAxisByCoordinates = 1
    catAxisSystemAxisOppositeDirection = 2

class CATAxisSystemMainType(EnumItem):
    catAxisSystemStandard = 0
    catAxisSystemAxisRotation = 1
    catAxisSystemEulerAngles = 2
    catAxisSystemExplicit = 3

class CATAxisSystemOriginType(EnumItem):
    catAxisSystemOriginByPoint = 0        
    catAxisSystemOriginByCoordinates = 1  

class CatConstraintAngleSector(EnumItem):
    catCstAngleSector0 = 0
    catCstAngleSector1 = 1
    catCstAngleSector2 = 2
    catCstAngleSector3 = 3

class CatConstraintDistConfig(EnumItem):
    catCstDCUnspec = 0
    catCstDCParallel = 1
    catCstDCParallelSameOrient = 2
    catCstDCParallelOppOrient = 3

class CatConstraintDistDirection(EnumItem):
    catCstDistDirectionNone = 0
    catCstDistDirection1 = 1
    catCstDistDirection2 = 2
    catCstDistDirection3 = 3

class CatConstraintMode(EnumItem):
    catCstModeDrivingDimension = 0
    catCstModeDrivenDimension = 1

class CatConstraintOrientation(EnumItem):
    catCstOrientSame = 0
    catCstOrientOpposite = 1
    catCstOrientUndefined = 2

class CatConstraintRefAxis(EnumItem):
    catCstRefAxisX = 0
    catCstRefAxisY = 1
    catCstRefAxisZ = 2

class CatConstraintRefType(EnumItem):
    catCstRefTypeRelative = 0
    catCstRefTypeFixInSpace = 1

class CatConstraintSide(EnumItem):
    catCstSidePositive = 0
    catCstSideNegative = 1
    catCstSideSameAsValue = 2
    catCstSideOppositeToValue = 3
    catCstSideUndefined = 4

class CatConstraintStatus(EnumItem):
    catCstStatusOK = 0
    catCstStatusKOStronglyNotSatisfied = 1
    catCstStatusKOWrongOrientOrSide = 2
    catCstStatusKOWrongValue = 3
    catCstStatusKOWrongGeomEltType = 4
    catCstStatusKOBroken = 5

class CatConstraintType(EnumItem):
    catCstTypeReference = 0
    catCstTypeDistance = 1
    catCstTypeOn = 2
    catCstTypeConcentricity = 3
    catCstTypeTangency = 4
    catCstTypeLength = 5
    catCstTypeAngle = 6
    catCstTypePlanarAngle = 7
    catCstTypeParallelism = 8
    catCstTypeAxisParallelism = 9
    catCstTypeHorizontality = 10
    catCstTypePerpendicularity = 11
    catCstTypeAxisPerpendicularity = 12
    catCstTypeVerticality = 13
    catCstTypeRadius = 14
    catCstTypeSymmetry = 15
    catCstTypeMidPoint = 16
    catCstTypeEquidistance = 17
    catCstTypeMajorRadius = 18
    catCstTypeMinorRadius = 19
    catCstTypeSurfContact = 20
    catCstTypeLinContact = 21
    catCstTypePoncContact = 22
    catCstTypeChamfer = 23
    catCstTypeChamferPerpend = 24
    catCstTypeAnnulContact = 25
    catCstTypeCylinderRadius = 26
    catCstTypeStContinuity = 27
    catCstTypeStDistance = 28
    catCstTypeSdContinuity = 29
    catCstTypeSdShape = 30
    catCstTypeCurvilinearDistance = 31