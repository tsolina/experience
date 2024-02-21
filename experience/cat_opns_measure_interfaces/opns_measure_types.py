from experience.types.enum_item import EnumItem

class CATMeasurableContextType(EnumItem):
    PartContext = 0
    ProductContext = 1

class CATMeasurableModeOfCalc(EnumItem):
    MeasExactCalculation = 0
    MeasApproximateCalculation = 1
    MeasExactElseApproxCalculation = 2
    MeasUnknownCalculation = 3

class CATMeasurableType(EnumItem):
    CAAMeasurableAxisSystem = 0
    CAAMeasurableBetween = 1
    CAAMeasurableCircle = 2
    CAAMeasurableCone = 3
    CAAMeasurableCurve = 4
    CAAMeasurableCylinder = 5
    CAAMeasurableLine = 6
    CAAMeasurablePlane = 7
    CAAMeasurablePoint = 8
    CAAMeasurableSphere = 9
    CAAMeasurableSurface = 10
    CAAMeasurableVolume = 11

class CATOpnsMeasureDistanceType(EnumItem):
    catOpnsMinimumDistance = 0
    catOpnsMaximumDistance = 1
    catOpnsMaximumDistance12 = 2
    catOpnsMinimumDistanceAlongDir = 3
    catOpnsBandAnalysis = 4
    catOpnsUnknownDistance = 5

class CATOpnsMeasureEdgeType(EnumItem):
    catOpnsLineEdge = 0
    catOpnsArcEdge = 1
    catOpnsCurveEdge = 2
    catOpnsEllipseEdge = 3
    catOpnsParabolaEdge = 4
    catOpnsHyperbolaEdge = 5
    catOpnsAxisEdge = 6
    catOpnsUnknownEdge = 7

class CATOpnsMeasureExtensionMode(EnumItem):
    catOpnsFiniteExtend = 0
    catOpnsInfiniteExtend = 1

class CATOpnsMeasureItemType(EnumItem):
    catOpnsPointItem = 0
    catOpnsEdgeItem = 1
    catOpnsSurfaceItem = 2
    catOpnsVolumeItem = 3
    catOpnsComplexItem = 4
    catOpnsUnknownItem = 5
    catOpnsNotValid = 6
    catOpnsThicknessItem = 7
    catOpnsSurface2DItem = 8
    catOpnsAngle3PtsItem = 9

class CATOpnsMeasureSurfaceType(EnumItem):
    catOpnsPlaneSurface = 0
    catOpnsCylinderSurface = 1
    catOpnsSphereSurface = 2
    catOpnsTorusSurface = 3
    catOpnsConeSurface = 4
    catOpnsUnknownSurface = 5

class CATResultCalcType(EnumItem):
    ResExactCalculation = 0
    ResApproximateCalculation = 1
    ResUnknownCalculation = 2
    ResMixedCalculation = 3