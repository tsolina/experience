from experience.types.enum_item import EnumItem

class CATInteractionType(EnumItem):
    CATSelection = 0       
    CATIndication = 1      
    CATMouseMove = 2       
    CATInputUndo = 3       
    CATInputRedo = 4       
    CATEscape = 5
    CATOtherEditor = 6     
    CATExclusiveCommand = 7

class CATMultiSelectionMode(EnumItem):
    CATMonoSel = 0
    CATMultiSelTriggWhenSelPerf = 1
    CATMultiSelTriggWhenUserValidatesSelection = 2

class CATPPRTreeItemType(EnumItem):
    CATProcessList = 0
    CATProductList = 1
    CATResourcesList = 2

class CATSelectionFilter(EnumItem):
    ZeroDim = 0
    MonoDim = 1
    MonoDimInfinite = 2
    RectilinearMonoDim = 3
    RectilinearMonoDimInfinite = 4
    BiDim = 5
    BiDimInfinite = 6
    PlanarBiDim = 7
    PlanarBiDimInfinite = 8
    CylindricalBiDim = 9
    TriDim = 10

class CatArrangeStyle(EnumItem):
    catArrangeCascade = 0
    catArrangeTiledHorizontal = 1
    catArrangeTiledVertical = 2
    catArrangeTiledHorizontalInAllTab = 3
    catArrangeTiledVerticalInAllTab = 4
    catArrangeTiledGridInAllTab = 5
    catArrangeTiledHorizontalInCurrentTab = 6
    catArrangeTiledVerticalInCurrentTab = 7
    catArrangeTiledGridInCurrentTab = 8
    catArrangeTiledHorizontalInNewTab = 9
    catArrangeTiledVerticalInNewTab = 10
    catArrangeTiledGridInNewTab = 11

class CatBannerPosition(EnumItem):
    catBannerPositionNone = 0
    catBannerPositionBottom = 1
    catBannerPositionTop = 2
    catBannerPositionLeft = 3
    catBannerPositionRight = 4

class CatCameraType(EnumItem):
    catCamera2D = 0
    catCamera3D = 1

class CatCaptureFormat(EnumItem):
    catCaptureFormatCGM = 0
    catCaptureFormatEMF = 1
    catCaptureFormatTIFF = 2
    catCaptureFormatTIFFGreyScale = 3
    catCaptureFormatBMP = 4
    catCaptureFormatJPEG = 5

class CatClippingMode(EnumItem):
    catClippingModeClear = 0
    catClippingModeNear = 1
    catClippingModeFar = 2
    catClippingModeNearAndFar = 3

class CatImageRotation(EnumItem):
    catImageNoRotation = 0
    catImageRotation90 = 1
    catImageRotation180 = 2
    catImageRotation270 = 3
    catImageBestRotation = 4

class CatLightingMode(EnumItem):
    catInfiniteLightSource = 0
    catNeonLightSource = 1

class CatNavigationStyle(EnumItem):
    catNavigationExamine = 0
    catNavigationWalk = 1
    catNavigationFly = 2

class CatPaperOrientation(EnumItem):
    catPaperPortrait = 0
    catPaperLandscape = 1
    catPaperBestFit = 2

class CatPaperSize(EnumItem):
    catPaperLetter = 0
    catPaperLegal = 1
    catPaperA0 = 2
    catPaperA1 = 3
    catPaperA2 = 4
    catPaperA3 = 5
    catPaperA4 = 6
    catPaperA = 7
    catPaperB = 8
    catPaperC = 9
    catPaperD = 10
    catPaperE = 11
    catPaperF = 12
    catPaperUser = 13

class CatPrintColor(EnumItem):
    catColorTrueColor = 0
    catColorGreyScale = 1
    catColorMonochrome = 2

class CatPrintLineCap(EnumItem):
    catPrintFlat = 0
    catPrintSquare = 1
    catPrintRound = 2

class CatPrintLineSpecification(EnumItem):
    catPrintAbsolute = 0
    catPrintScaled = 1
    catPrintNoThickness = 2

class CatPrintQuality(EnumItem):
    catPrintQualityDraft = 0
    catPrintQualityLow = 1
    catPrintQualityMedium = 2
    catPrintQualityHigh = 3
    catPrintQualityCustom = 4

class CatPrintRenderingMode(EnumItem):
    catPrintRenderingModeDefault = 0
    catPrintRenderingModeWireframe = 1
    catPrintRenderingModeHiddenLineRemoval = 2
    catPrintRenderingModeShadingWithTriangles = 3
    catPrintRenderingModeDynamicHiddenLineRemoval = 4
    catPrintRenderingModeOnScreen = 5

class CatPrinterDirState(EnumItem):
    CatPrinterDirFree = 0
    CatPrinterDirProtect = 1

class CatProjectionMode(EnumItem):
    catProjectionConic = 0
    catProjectionCylindric = 1
    catProjectionUndefined = 2

class CatRenderingMode(EnumItem):
    catRenderShading = 0
    catRenderShadingWithEdges = 1
    catRenderWireFrame = 2
    catRenderHiddenLinesRemoval = 3
    catRenderQuickHiddenLinesRemoval = 4
    catRenderMaterial = 5
    catRenderMaterialWithEdges = 6
    catRenderShadingWithEdgesAndHiddenEdges = 7
    catRenderShadingWithEdgesWithoutSmoothEdges = 8
    catRenderWireFrameWithoutSmoothEdgesWithoutVertices = 9
    catRenderWireFrameWithHalfSmoothEdgesWithoutVertices = 10
    catRenderShadingWithEdgesWithOutlines = 11
    catRenderQuickHiddenLinesRemovalWithoutVertices = 12
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithOutlines = 13
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithOutlinesWithoutVertices = 14
    catRenderWireFrameWithHalfSmoothEdgeWithOutlinesWithoutVertices = 15
    catRenderWireFrameWithOutlinesWithoutSmoothEdgesWithoutVertices = 16
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithoutSmoothEdgesWithoutVertices = 17
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithHalfSmoothEdgeWithoutVertices = 18
    catRenderQuickHiddenLinesRemovalWithoutSmoothEdgesWithoutVertices = 19
    catRenderQuickHiddenLinesRemovalWithHalfSmoothEdgeWithoutVertices = 20
    catRenderShadingWithEdgesWithHalfSmoothEdgeWithoutVertices = 21
    catRenderShadingWithEdgesWithHalfSmoothEdge = 22
    catRenderRayTracingWithMaterial = 23
    catRenderRayTracingWithMaterialAndEdges = 24
    catRenderShadingWithEdgesWithOutlinesWithTransparency = 25
    catRenderShadingWithEdgesWithOutlinesWithTriangles = 26
    catRenderShadingWithEdgesWithoutOutlinesWithTransparency = 27
    catRenderShadingWithEdgesWithoutOutlinesWithTriangles = 28
    catRenderShadingWithEdgesWithHalfSmoothEdgeWithTransparency = 29
    catRenderShadingWithEdgesWithHalfSmoothEdgeWithTriangles = 30
    catRenderShadingWithTransparency = 31
    catRenderShadingWithTriangles = 32
    catRenderShadingWithEdgesWithoutOutlinesWithoutVerticesWithTransparency = 33
    catRenderShadingWithEdgesWithoutOutlinesWithoutVerticesWithTrangles = 34
    catRenderMaterialWithoutSmoothEdges = 35
    catRenderMaterialWithHalfSmoothEdge = 36
    catRenderMaterialWithHalfSmoothEdgeWithoutVertices = 37
    catRenderMaterialWithHalfSmoothEdgeWithoutVerticesWithOutlines = 38
    catRenderCustomRenderingMode = 39

class CatScriptCommand(EnumItem):
    CatScriptCommandDefault = 0
    CatScriptCommandStop = 1
    CatScriptCommandStart = 2

class CatSpecsAndGeomWindowLayout(EnumItem):
    catWindowSpecsOnly = 0
    catWindowGeomOnly = 1
    catWindowSpecsAndGeom = 2

class CatSpecsLayout(EnumItem):
    catSpecsViewerHorizontalIndented = 0
    catSpecsViewerHorizontalUp = 1
    catSpecsViewerHorizontalCentered = 2
    catSpecsViewerVerticalCentered = 3
    catSpecsViewerHorizontalRelational = 4
    catSpecsViewerVerticalRelational = 5

class CatVisLayerType(EnumItem):
    catVisLayerBasic = 0
    catVisLayerNone = 1

class CatVisPropertyPick(EnumItem):
    catVisPropertyPickAttr = 0
    catVisPropertyNoPickAttr = 1

class CatVisPropertyShow(EnumItem):
    catVisPropertyShowAttr = 0
    catVisPropertyNoShowAttr = 1

class CatVisPropertyStatus(EnumItem):
    catVisPropertyDefined = 0
    catVisPropertyUnDefined = 1

class CatVisPropertyType(EnumItem):
    catVisPropertyLineType = 0
    catVisPropertyWidth = 1
    catVisPropertyColor = 2
    catVisPropertyOpacity = 3

class CatWindowState(EnumItem):
    catWindowStateMaximized = 0
    catWindowStateMinimized = 1
    catWindowStateNormal = 2

class InfSymbolType(EnumItem):
    x_cross = 1
    plus_cross = 2
    unfilled_circle = 3
    two_unfilled_concentric_circles = 4
    filled_circle = 5
    filled_square = 6
    star = 7
    dot = 8
    small_dot = 9
    arrow_down = 10
    arrow_up = 11
    full_circle = 12
    full_square = 13


if __name__ == "__main__":
    val = CatPaperSize.catPaperA0
    print(val, val == CatPaperSize.catPaperA1, val != CatPaperSize.catPaperA1)