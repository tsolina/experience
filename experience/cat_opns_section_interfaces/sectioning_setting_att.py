from typing import Union, TYPE_CHECKING

# from experience.system import AnyObject
from experience.cat_opns_section_interfaces.opns_section_types import *
from experience.system.setting_controller import SettingController

# if TYPE_CHECKING:
#     from experience.plm_validation_interfaces.markers import Markers
#     from experience.cat_opns_measure_interfaces.measures import Measures
#     from experience.mecmod_interfaces.part import Part
#     from experience.inf_interfaces.editor import Editor

class SectioningSettingAtt(SettingController):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         SectioningSettingAtt
    """

    def __init__(self, com):
        super().__init__(com)
        self.section_setting_att = com

    def get_export_mode(self) -> int:
        #return self._get_multi([self.section_setting_att], ('SectioningSettingAtt', "GetExportMode"), ("Long"))
        return self.section_setting_att.GetExportMode()
    
    def get_only_plane_dyn_mode(self) -> int:
        return self.section_setting_att.GetOnlyPlaneDynMode()
    
    def get_plane_color(self) -> tuple[int, int, int]:
        return self.section_setting_att.GetPlaneColor()
    
    def get_plane_transparency(self) -> int:
        return self.section_setting_att.GetPlaneTransparency()
    
    def get_section_contour_color(self) -> tuple[int, int, int]:
        return self.section_setting_att.GetSectionContourColor()
    
    def get_section_contour_dominant_status(self) -> int:
        return self.section_setting_att.GetSectionContourDominantStatus()
    
    def get_section_info_disp_mode(self) -> int:
        return self.section_setting_att.GetSectionInfoDispMode()
    
    def get_section_mode(self) -> CATSectioningMode:
        return CATSectioningMode.item(self.section_setting_att.GetSectionMode())
    
    def get_section_visu_mode(self) -> CATSectioningPlaneVisuMode:
        return CATSectioningPlaneVisuMode.item(self.section_setting_att.GetSectionPlaneVisuMode())
    
    def get_section_update_mode(self) -> int:
        return self.section_setting_att.GetSectionUpdateMode()
    
    def get_thickness_line(self) -> int:
        return self.section_setting_att.GetThicknessLine()
    
    def set_export_mode(self, i_export_mode: int) -> 'SectioningSettingAtt':
        self.section_setting_att.SetExportMode(i_export_mode)
        return self
    
    def set_only_plane_dyn_mode(self, i_only_plane_dyn_mode: int) -> 'SectioningSettingAtt':
        self.section_setting_att.SetOnlyPlaneDynMode(i_only_plane_dyn_mode)
        return self
    
    def set_plane_color(self, i_r: int, i_g: int, i_b: int) -> 'SectioningSettingAtt':
        self.section_setting_att.SetPlaneColor(i_r, i_g, i_b)
        return self
    
    def set_plane_transparency(self, i_plane_transparency: int) -> 'SectioningSettingAtt':
        self.section_setting_att.SetPlaneTransparency(i_plane_transparency)
        return self

    def set_section_contour_color(self, i_r: int, i_g: int, i_b: int) -> 'SectioningSettingAtt':
        self.section_setting_att.SetSectionContourColor(i_r, i_g, i_b)
        return self
    
    def set_section_contour_dominant_status(self, value: int) -> 'SectioningSettingAtt':
        self.section_setting_att.SetSectionContourDominantStatus(value)
        return self
    
    def set_section_info_disp_mode(self, value: int) -> 'SectioningSettingAtt':
        self.section_setting_att.SetSectionInfoDispMode(value)
        return self
    
    def set_section_mode(self, value: CATSectioningMode) -> 'SectioningSettingAtt':
        self.section_setting_att.SetSectionMode(int(value))
        return self
    
    def set_section_plane_visu_mode(self, value: CATSectioningPlaneVisuMode) -> 'SectioningSettingAtt':
        self.section_setting_att.SetSectionPlaneVisuMode(int(value))
        return self
    
    def set_section_update_mode(self, value: int) -> 'SectioningSettingAtt':
        self.section_setting_att.SetSectionUpdateMode(value)
        return self
    
    def set_thickness_line(self, value: int) -> 'SectioningSettingAtt':
        self.section_setting_att.SetThicknessLine(value)
        return self
    
    # def section_mode(self, value: CATSectioningMode = None) -> CATSectioningMode:
    #     if value is not None:
    #         self._com.SetAttr("SectionMode", int(value)) 
    #         return self
    #     return CATSectioningMode.item(self._com.GetAttr("SectionMode")) 
    
    def section_mode(self, value: int = None) -> Union['SectioningSettingAtt', int]:
        if value is not None:
            self._com.PutAttr("SectionMode", value)
            return self
        return self._com.GetAttr("SectionMode")
    
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'