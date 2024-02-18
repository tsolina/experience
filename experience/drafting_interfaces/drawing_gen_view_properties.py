from typing import Union, Optional, TYPE_CHECKING

from experience.system import AnyObject
from experience.drafting_interfaces.drafting_types import *

if TYPE_CHECKING:
    from experience.types import cat_variant

class DrawingGenViewProperties(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingGenViewProperties
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_gen_view_properties = com

    def ann_callout_generation_mode(self, value: bool = None) -> Union['DrawingGenViewProperties', bool]:
        if value is not None:
            self.drawing_gen_view_properties.AnnCalloutGenerationMode = value
            return self
        return self.drawing_gen_view_properties.AnnCalloutGenerationMode
    
    def aproximate_parameter(self, value: int = None) -> Union['DrawingGenViewProperties', int]:
        if value is not None:
            self.drawing_gen_view_properties.ApproximateParameter = value
            return self
        return self.drawing_gen_view_properties.ApproximateParameter
    
    def auto_hidden_line_mode(self, value: bool = None) -> Union['DrawingGenViewProperties', bool]:
        if value is not None:
            self.drawing_gen_view_properties.AutoHiddenLineMode = value
            return self
        return self.drawing_gen_view_properties.AutoHiddenLineMode
    
    def axis_line_mode(self, value: bool = None) -> Union['DrawingGenViewProperties', bool]:
        if value is not None:
            self.drawing_gen_view_properties.AxisLineMode = value
            return self
        return self.drawing_gen_view_properties.AxisLineMode    
    
    def centerline_mode(self, value: bool = None) -> Union['DrawingGenViewProperties', bool]:
        if value is not None:
            self.drawing_gen_view_properties.CenterlineMode = value
            return self
        return self.drawing_gen_view_properties.CenterlineMode

    def clash_detection_mode(self, value: bool = None) -> Union['DrawingGenViewProperties', bool]:
        if value is not None:
            self.drawing_gen_view_properties.ClashDetectionMode = value
            return self
        return self.drawing_gen_view_properties.ClashDetectionMode

    def color_inheritance_mode(self, value: 'Cat3DColorInheritanceMode' = None) -> Union['DrawingGenViewProperties', 'Cat3DColorInheritanceMode']:
        if value is not None:
            self.drawing_gen_view_properties.ColorInheritanceMode = int(value)
            return self
        return Cat3DColorInheritanceMode.item(self.drawing_gen_view_properties.ColorInheritanceMode) 

    def fillet_representation(self, value: 'CatFilletRepresentation' = None) -> Union['DrawingGenViewProperties', 'CatFilletRepresentation']:
        if value is not None:
            self.drawing_gen_view_properties.FilletRepresentation = int(value)
            return self
        return CatFilletRepresentation.item(self.drawing_gen_view_properties.FilletRepresentation) 
    
    def hidden_line_mode(self, value: 'CatHiddenLineMode' = None) -> Union['DrawingGenViewProperties', 'CatHiddenLineMode']:
        if value is not None:
            self.drawing_gen_view_properties.HiddenLineMode = int(value)
            return self
        return CatHiddenLineMode.item(self.drawing_gen_view_properties.HiddenLineMode) 

    def image_print_precision_mode(self, value: 'RasterLevelOfDetail' = None) -> Union['DrawingGenViewProperties', 'RasterLevelOfDetail']:
        if value is not None:
            self.drawing_gen_view_properties.ImagePrintPrecisionMode = int(value)
            return self
        return RasterLevelOfDetail.item(self.drawing_gen_view_properties.ImagePrintPrecisionMode)
    
    def image_view_mode(self, value: 'CatGenViewRasterMode' = None) -> Union['DrawingGenViewProperties', 'CatGenViewRasterMode']:
        if value is not None:
            self.drawing_gen_view_properties.ImageViewMode = int(value)
            return self
        return CatGenViewRasterMode.item(self.drawing_gen_view_properties.ImageViewMode)  
    
    def image_visu_precision_mode(self, value: 'RasterLevelOfDetail' = None) -> Union['DrawingGenViewProperties', 'RasterLevelOfDetail']:
        if value is not None:
            self.drawing_gen_view_properties.ImageVisuPrecisionMode = int(value)
            return self
        return RasterLevelOfDetail.item(self.drawing_gen_view_properties.ImageVisuPrecisionMode)  
    
    def limit_bounding_box(self, value: float = None) -> Union['DrawingGenViewProperties', float]:
        if value is not None:
            self.drawing_gen_view_properties.LimitBoundingBox = value
            return self
        return self.drawing_gen_view_properties.LimitBoundingBox
    
    def occlusion_culling_mode(self, value: bool = None) -> Union['DrawingGenViewProperties', bool]:
        if value is not None:
            self.drawing_gen_view_properties.OcclusionCullingMode = value
            return self
        return self.drawing_gen_view_properties.OcclusionCullingMode
    
    def pattern_generation_mode(self, value: bool = None) -> Union['DrawingGenViewProperties', bool]:
        if value is not None:
            self.drawing_gen_view_properties.PatternGenerationMode = value
            return self
        return self.drawing_gen_view_properties.PatternGenerationMode
    
    def points_projection_mode(self, value: 'CatPointsProjectionMode' = None) -> Union['DrawingGenViewProperties', 'CatPointsProjectionMode']:
        if value is not None:
            self.drawing_gen_view_properties.PointsProjectionMode = int(value)
            return self
        return CatPointsProjectionMode.item(self.drawing_gen_view_properties.PointsProjectionMode)
        
    def points_symbol(self, value: int = None) -> Union['DrawingGenViewProperties', int]:
        if value is not None:
            self.drawing_gen_view_properties.PointsSymbol = value
            return self
        return self.drawing_gen_view_properties.PointsSymbol 

    def polyhedral_data_integration(self, value: bool = None) -> Union['DrawingGenViewProperties', bool]:
        if value is not None:
            self.drawing_gen_view_properties.PolyhedralDataIntegration = value
            return self
        return self.drawing_gen_view_properties.PolyhedralDataIntegration

    def print_precision(self, value: float = None) -> Union['DrawingGenViewProperties', float]:
        if value is not None:
            self.drawing_gen_view_properties.PrintPrecision = value
            return self
        return self.drawing_gen_view_properties.PrintPrecision
    
    def representation_mode(self, value: 'CatGenRepresentationMode' = None) -> Union['DrawingGenViewProperties', 'CatGenRepresentationMode']:
        if value is not None:
            self.drawing_gen_view_properties.RepresentationMode = int(value)
            return self
        return CatGenRepresentationMode.item(self.drawing_gen_view_properties.RepresentationMode)
    
    def scan_3d_reps_mode(self, value: 'CatDftGenRepresentationPolicy' = None) -> Union['DrawingGenViewProperties', 'CatDftGenRepresentationPolicy']:
        if value is not None:
            self.drawing_gen_view_properties.Scan3DRepsMode = int(value)
            return self
        return CatDftGenRepresentationPolicy.item(self.drawing_gen_view_properties.Scan3DRepsMode)   
    
    def shaded_background_mode(self, value: bool = None) -> Union['DrawingGenViewProperties', bool]:
        if value is not None:
            self.drawing_gen_view_properties.ShadedBackgroundMode = value
            return self
        return self.drawing_gen_view_properties.ShadedBackgroundMode

    def smooth_edges_generation_mode(self, value: bool = None) -> Union['DrawingGenViewProperties', bool]:
        if value is not None:
            self.drawing_gen_view_properties.SmoothEdgesGenerationMode = value
            return self
        return self.drawing_gen_view_properties.SmoothEdgesGenerationMode

    def thread_mode(self, value: bool = None) -> Union['DrawingGenViewProperties', bool]:
        if value is not None:
            self.drawing_gen_view_properties.ThreadMode = value
            return self
        return self.drawing_gen_view_properties.ThreadMode

    def visu_precision(self, value: float = None) -> Union['DrawingGenViewProperties', float]:
        if value is not None:
            self.drawing_gen_view_properties.VisuPrecision = value
            return self
        return self.drawing_gen_view_properties.VisuPrecision

    def wireframe_extraction_mode(self, value: 'CatWireframeMode' = None) -> Union['DrawingGenViewProperties', 'CatWireframeMode']:
        if value is not None:
            self.drawing_gen_view_properties.WireframeExtractionMode = int(value)
            return self
        return CatWireframeMode.item(self.drawing_gen_view_properties.WireframeExtractionMode)
    
    def retrieve_bck_color_property_for_op(self, ib_is_color_from_3d: bool) -> float:
        return self._get_safe_array(self.drawing_gen_view_properties, "RetrieveBckColorPropertyForOp", 2, ib_is_color_from_3d)
    
    def set_bck_color_property_for_op(self, ib_is_color_from_3d: bool, ip_rgb_values: 'cat_variant') -> 'DrawingGenViewProperties':
        self.drawing_gen_view_properties.SetBckColorPropertyForOp(ib_is_color_from_3d, ip_rgb_values)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'