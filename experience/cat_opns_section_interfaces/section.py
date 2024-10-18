from typing import Union, TYPE_CHECKING

from experience.system import AnyObject
from experience.cat_opns_section_interfaces.opns_section_types import *

if TYPE_CHECKING:
    from experience.plm_validation_interfaces.markers import Markers
    from experience.cat_opns_measure_interfaces.measures import Measures
    from experience.mecmod_interfaces.part import Part
    from experience.inf_interfaces.editor import Editor

class Section(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Section
    """

    def __init__(self, com):
        super().__init__(com)
        self.section = com

    def behavior(self, value: CatSectionBehavior = None) -> Union['Section', CatSectionBehavior]:
        if value is not None:
            self.section.Behavior = int(value)
            return self
        return CatSectionBehavior.item(self.section.Behavior)
    
    def height(self, value: float = None) -> Union['Section', float]:
        if value is not None:
            self.section.Height = value
            return self
        return self.section.Height
    
    def markers(self) -> 'Markers':
        from experience.plm_validation_interfaces.markers import Markers
        return Markers(self.section.Markers)
    
    def measures(self) -> 'Measures':
        from experience.cat_opns_measure_interfaces.measures import Measures
        return Measures(self.section.Measures)
    
    def scene_render(self, value: int = None) -> Union['Section', int]:
        if value is not None:
            self.section.SceneRender = value
            return self
        return self.section.SceneRender
    
    def thickness(self, value: float = None) -> Union['Section', float]:
        if value is not None:
            self.section.Thickness = value
            return self
        return self.section.Thickness
    
    def type(self, value: CatSectionType = None) -> Union['Section', CatSectionType]:
        if value is not None:
            self.section.Type = int(value)
            return self
        return CatSectionType.item(self.section.Type)
    
    def width(self, value: float = None) -> Union['Section', float]:
        if value is not None:
            self.section.Width = value
            return self
        return self.section.Width
    
    def export(self) -> 'Part':
        from experience.mecmod_interfaces.part import Part
        return Part(self._get_multi([self.section], ("Section", "Export"), ("Part")))
    
    def export_as_drawing(self) -> 'Editor':
        from experience.inf_interfaces.editor import Editor
        return Editor(self._get_multi([self.section], ("Section", "ExportAsDrawing"), ("Editor")))
    
    def export_to(self, i_format: str, i_save_path: str) -> 'Section':
        self.section.ExportTo(i_format, i_save_path)
        return self
    
    def export_to_existing(self) -> 'Part':
        from experience.mecmod_interfaces.part import Part
        return Part(self._get_multi([self.section], ("Section", "ExportToExisting"), ("Part")))
    
    def get_position(self) -> tuple[float, float, float,  float, float, float,  float, float, float,  float, float, float]:
        '''
        x012, y345, z678, o91011
        '''
        return self._get_safe_array(self.section, "GetPosition", 11)
    
    def is_empty(self) -> int:
        return self.section.IsEmpty()
    
    def set_position(self, i_components: list) -> 'Section':
        self.section.SetPosition(i_components)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'