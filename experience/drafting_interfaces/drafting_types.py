from experience.types.enum_item import EnumItem

class Cat3DColorInheritanceMode(EnumItem):
    cat3DColorInheritanceModeOff = 0
    cat3DColorInheritanceModeOn = 1

class CatAreaFillType(EnumItem):
    catAreaFillOnCurves = 0
    catAreaFillOnMathematicPoints = 1

class CatDftGenRepresentationPolicy(EnumItem):
    catDftAllDesignRepsPolicy = 0
    catDftFirstDesignRepsPolicy = 1
    catDftAllSessionRepsPolicy = 2
    catDftCustomParam = 3

class CatDrawingViewType(EnumItem):
    catViewBackground = 0
    catViewFront = 1
    catViewLeft = 2
    catViewRight = 3
    catViewTop = 4
    catViewBottom = 5
    catViewRear = 6
    catViewAuxiliary = 7
    catViewIsom = 8
    catViewSection = 9
    catViewSectionCut = 10
    catViewDetail = 11
    catViewUntyped = 12
    catViewMain = 13
    catViewPure_Sketch = 14
    catViewUnfolded = 15
    catViewAxonometric = 16

class CatFilletRepresentation(EnumItem):
    catFilletRepNone = 0
    catFilletRepBoundary = 1
    catFilletRepSymbolic = 2
    catFilletRepOriginalEdge = 3
    catFilletRepProjectedOriginalEdge = 4

class CatGenRepresentationMode(EnumItem):
    catModeExact = 0
    catModeCGR = 1
    catModeApproximate = 2
    catModeRaster = 3

class CatGenViewRasterMode(EnumItem):
    catImageHRD = 0
    catImageShading = 1
    catImageShadingEdges = 2
    catImageShadingNoLight = 3
    catImageShadingEdgesNoLight = 4

class CatHiddenLineMode(EnumItem):
    catHlrModeOff = 0
    catHlrModeOn = 1

class CatImageViewMode(EnumItem):
    catImageModeOff = 0
    catImageModeHRD = 1
    catImageModeShading = 2
    catImageModeShadingWithEdges = 3
    catImageModeShadingNoLightSource = 4
    catImageModeShadingWithEdgesAndNoLightSource = 5

class CatPictureFormat(EnumItem):
    catPictureNONE = 0
    catPicturePNG = 1
    catPictureJPEG = 2
    catPictureCCITTG3 = 3

class CatPictureType(EnumItem):
    catPictureRaster = 0
    catPictureVector = 1

class CatPointsProjectionMode(EnumItem):
    catPointsProjectionModeOff = 0
    catPointsProjectionModeOn = 1

class CatProjViewType(EnumItem):
    catRightView = 0
    catLeftView = 1
    catTopView = 2
    catBottomView = 3
    catRearView = 4

class CatRepresentationMode(EnumItem):
    catExactMode = 0
    catPolyhedricMode = 1
    catVisualMode = 2

class CatSheetGenViewsPosMode(EnumItem):
    catFixedCG = 0
    catFixedAxis = 1

class CatSheetProjectionMethod(EnumItem):
    catFirstAngle = 0
    catThirdAngle = 1

class CatThreadLinkedTo(EnumItem):
    catNotDefined = 0
    catNoLink = 1
    cat2DPoint = 2
    cat2DCircle = 3
    cat3DGeom = 4
    cat3DHole = 5
    cat3DThread = 6

class CatThreadType(EnumItem):
    catThreaded = 0
    catTaped = 1

class CatWireframeMode(EnumItem):
    catGenWFOff = 0
    catGenWFCanBeHidden = 1
    catGenWFAlwaysVisible = 2

class RasterLevelOfDetail(EnumItem):
    LowQuality = 0
    NormalQuality = 1
    HighQuality = 2
    Customize = 3