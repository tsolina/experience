from experience.system import SettingController

class MeasureSettingAtt(SettingController):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         MeasureSettingAtt
    """

    def __init__(self, com):
        super().__init__(com)
        self.measure_setting_att = com

    def get_auto_attach_move_status(self) -> int:
        return self.measure_setting_att.GetAutoAttachMoveStatus()
    
    def get_border_color(self) -> tuple[int, int, int]:
        return self.measure_setting_att.GetBorderColor()
    
    def get_border_status(self) -> int:
        return self.measure_setting_att.GetBorderStatus()

    def get_fill_status(self) -> int:
        return self.measure_setting_att.GetFillStatus()
    
    def get_fill_style(self) -> int:
        return self.measure_setting_att.GetFillStyle()
    
    def get_line_color(self) -> tuple[int, int, int]:
        return self.measure_setting_att.GetLineColor()    
    
    def get_line_width(self) -> int:
        return self.measure_setting_att.GetLineWidth()
    
    def get_measure_only_shown_elements_status(self) -> int:
        return self.measure_setting_att.GetMeasureOnlyShownElementsStatus()
    
    def get_product_update_status(self) -> int:
        return self.measure_setting_att.GetProductUpdateStatus()
    
    def get_text_box_color(self) -> tuple[int, int, int]:
        return self.measure_setting_att.GetTextBoxColor()  
    
    def get_text_box_transparency(self) -> int:
        return self.measure_setting_att.GetTextBoxTransparency()
    
    def get_text_color(self) -> tuple[int, int, int]:
        return self.measure_setting_att.GetTextColor() 
    
    def get_text_font(self) -> int:
        return self.measure_setting_att.GetTextFont()
    
    def get_text_font_index(self) -> int:
        return self.measure_setting_att.GetTextFontIndex()
    
    def get_text_size(self) -> int:
        return self.measure_setting_att.GetTextSize()
    
    def get_tilde_shown_status(self) -> int:
        return self.measure_setting_att.GetTildeShownStatus()
    
    def set_auto_attach_move_status(self, i_auto_update_in_prd: int) -> 'MeasureSettingAtt':
        self.measure_setting_att.SetAutoAttachMoveStatus(i_auto_update_in_prd)
        return self
    
    def set_border_color(self, i_r: int, i_g: int, i_b: int) -> 'MeasureSettingAtt':
        self.measure_setting_att.SetBorderColor(i_r, i_g, i_b)
        return self
    
    def set_border_status(self, value: int) -> 'MeasureSettingAtt':
        self.measure_setting_att.SetBorderStatus(value)
        return self
    
    def set_fill_status(self, value: int) -> 'MeasureSettingAtt':
        self.measure_setting_att.SetFillStatus(value)
        return self
    
    def set_fill_style(self, value: int) -> 'MeasureSettingAtt':
        self.measure_setting_att.SetFillStyle(value)
        return self
    
    def set_line_color(self, i_r: int, i_g: int, i_b: int) -> 'MeasureSettingAtt':
        self.measure_setting_att.SetLineColor(i_r, i_g, i_b)
        return self
    
    def set_line_width(self, value: int) -> 'MeasureSettingAtt':
        self.measure_setting_att.SetLineWidth(value)
        return self
    
    def set_measure_only_shown_elements_status(self, value: int) -> 'MeasureSettingAtt':
        self.measure_setting_att.SetMeasureOnlyShownElementsStatus(value)
        return self
    
    def set_product_update_status(self, value: int) -> 'MeasureSettingAtt':
        self.measure_setting_att.SetProductUpdateStatus(value)
        return self
    
    def set_text_box_color(self, i_r: int, i_g: int, i_b: int) -> 'MeasureSettingAtt':
        self.measure_setting_att.SetTextBoxColor(i_r, i_g, i_b)
        return self
    
    def set_text_box_transparency(self, value: int) -> 'MeasureSettingAtt':
        self.measure_setting_att.SetTextBoxTransparency(value)
        return self
    
    def set_text_color(self, i_r: int, i_g: int, i_b: int) -> 'MeasureSettingAtt':
        self.measure_setting_att.SetTextColor(i_r, i_g, i_b)
        return self
    
    def set_text_font(self, value: int) -> 'MeasureSettingAtt':
        self.measure_setting_att.SetTextFont(value)
        return self
    
    def set_text_font_index(self, value: int) -> 'MeasureSettingAtt':
        self.measure_setting_att.SetTextFontIndex(value)
        return self
    
    def set_text_size(self, value: int) -> 'MeasureSettingAtt':
        self.measure_setting_att.SetTextSize(value)
        return self    
    
    def set_tilde_shown_status(self, value: int) -> 'MeasureSettingAtt':
        self.measure_setting_att.SetTildeShownStatus(value)
        return self  

    def __repr__(self):
        return f'MeasureSettingAtt(name="{self.name()}")'
