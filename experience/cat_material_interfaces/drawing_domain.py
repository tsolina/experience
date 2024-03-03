from typing import TYPE_CHECKING

from experience.cat_material_interfaces import MaterialDomainContent
from experience.cat_material_interfaces.cat_material_types import *

if TYPE_CHECKING:
    from experience.types import cat_variant

class DrawingDomain(MaterialDomainContent):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMaterialIDLItf.MaterialDomainContent
                |                         DrawingDomain
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_domain = com

    def create_coloring_pattern(self, i_name: str, i_color: int) -> 'DrawingDomain':
        self.drawing_domain.CreateColoringPattern(i_name, i_color)
        return self
    
    def create_dotting_pattern(self, i_name: str, i_pitch: float, i_bright: int, i_color: int, i_zigzag: int) -> 'DrawingDomain':
        self.drawing_domain.CreateDottingPattern(i_name, i_pitch, i_bright, i_color, i_zigzag)
        return self
    
    def create_hatching_pattern(self, i_name: str, i_hatching_nb: int, i_offset: float, i_angle:float, i_pitch: tuple,
                                i_texture: tuple, i_thickness: tuple, i_color: tuple) -> 'DrawingDomain':
        self.drawing_domain.CreateHatchingPattern(i_name, i_hatching_nb, i_offset, i_angle, i_pitch, i_texture, i_thickness, i_color)
        return self
    
    def create_none_pattern(self, i_name: str) -> 'DrawingDomain':
        self.drawing_domain.CreateNonePattern(i_name)
        return self