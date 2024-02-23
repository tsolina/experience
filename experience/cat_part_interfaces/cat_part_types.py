from experience.types.enum_item import EnumItem

class CatCDHoleMode(EnumItem):
    catCDModeNoCountersunkDiameter = 0
    catCDModeCountersunkDiameter = 1

class CatCSHoleMode(EnumItem):
    catCSModeDepthAngle = 0
    catCSModeDepthDiameter = 1
    catCSModeAngleDiameter = 2

class CatChamferMode(EnumItem):
    catTwoLengthChamfer = 0
    catLengthAngleChamfer = 1

class CatChamferOrientation(EnumItem):
    catNoReverseChamfer = 0
    catReverseChamfer = 1

class CatChamferPropagation(EnumItem):
    catTangencyChamfer = 0
    catMinimalChamfer = 1

class CatCircularPatternParameters(EnumItem):
    catInstancesandAngularSpacing = 0
    catCompleteCrown = 1
    catUnequalAngularSpacing = 2

class CatDraftMode(EnumItem):
    catStandardDraftMode = 0
    catReflectKeepFaceDraftMode = 1
    catReflectKeepEdgeDraftMode = 2

class CatDraftMultiselectionMode(EnumItem):
    catNoneDraftMultiselectionMode = 0
    catDraftMultiselectionByNeutralMode = 1

class CatDraftNeutralPropagationMode(EnumItem):
    catNoneDraftNeutralPropagationMode = 0
    catSmoothDraftNeutralPropagationMode = 1

class CatFilletBitangencyType(EnumItem):
    catSphereBitangencyType = 0
    catCircleBitangencyType = 1

class CatFilletBoundaryRelimitation(EnumItem):
    catAutomaticFilletBoundaryRelimitation = 0
    catUVFilletBoundaryRelimitation = 1
    catConnectFilletBoundaryRelimitation = 2
    catMinimumFilletBoundaryRelimitation = 3
    catMaximumFilletBoundaryRelimitation = 4

class CatFilletEdgePropagation(EnumItem):
    catMinimalFilletEdgePropagation = 0
    catTangencyFilletEdgePropagation = 1

class CatFilletTrimSupport(EnumItem):
    catTrimFilletSupport = 0
    catNoTrimFilletSupport = 1

class CatFilletVariation(EnumItem):
    catLinearFilletVariation = 0
    catCubicFilletVariation = 1

class CatHoleAnchorMode(EnumItem):
    catExtremPointHoleAnchor = 0
    catMiddlePointHoleAnchor = 1

class CatHoleBottomType(EnumItem):
    catFlatHoleBottom = 0
    catVHoleBottom = 1
    catTrimmedHoleBottom = 2

class CatHoleThreadSide(EnumItem):
    catRightThreadSide = 0
    catLeftThreadSide = 1

class CatHoleThreadStandard(EnumItem):
    catHoleMetricThinPitch = 0
    catHoleMetricThickPitch = 1

class CatHoleThreadingMode(EnumItem):
    catThreadedHoleThreading = 0
    catSmoothHoleThreading = 1

class CatHoleType(EnumItem):
    catSimpleHole = 0
    catTaperedHole = 1
    catCounterboredHole = 2
    catCountersunkHole = 3
    catCounterdrilledHole = 4

class CatLimitMode(EnumItem):
    catOffsetLimit = 0
    catUpToNextLimit = 1
    catUpToLastLimit = 2
    catUpToPlaneLimit = 3
    catUpToSurfaceLimit = 4
    catUpThruNextLimit = 5
    catUntilLimit = 6

class CatMergeMode(EnumItem):
    catMergeOff = 0
    catMergeOn = 1

class CatPartitionLimitType(EnumItem):
    CatPartitionLimit_None = 0
    CatPartitionLimit_Infinite = 1
    CatPartitionLimit_UpToNext = 2

class CatPrismExtrusionDirection(EnumItem):
    catNormalToSketchDirection = 0
    catNotNormalToSketchDirection = 1

class CatPrismOrientation(EnumItem):
    catRegularOrientation = 0
    catInverseOrientation = 1

class CatRectangularPatternParameters(EnumItem):
    catInstancesandSpacing = 0
    catUnequalSpacing = 1

class CatSewingIntersectionMode(EnumItem):
    catSewingNoIntersect = 0
    catSewingIntersect = 1

class CatSplitSide(EnumItem):
    catPositiveSide = 0
    catNegativeSide = 1

class CatThreadPolarity(EnumItem):
    catThread = 0
    catTap = 1

class CatThreadSide(EnumItem):
    catRightSide = 0
    catLeftSide = 1

class CatThreadStandard(EnumItem):
    catMetricThinPitch = 0
    catMetricThickPitch = 1