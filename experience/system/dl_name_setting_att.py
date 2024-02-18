from typing import TYPE_CHECKING, Union
from experience.system import SettingController


class DLNameSettingAtt(SettingController):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         DLNameSettingAtt
    """

    def __init__(self, com):
        super().__init__(com)
        self.setting_controller = com

    def dl_name_creation_right(self, value: bool = None) -> Union['DLNameSettingAtt', bool]:
        if value is not None:
            self.setting_controller.DLNameCreationRight = value
            return self
        return self.setting_controller.DLNameCreationRight
    
    def root_dl_name_creation_right(self, value: bool = None) -> Union['DLNameSettingAtt', bool]:
        if value is not None:
            self.setting_controller.RootDLNameCreationRight = value
            return self
        return self.setting_controller.RootDLNameCreationRight
    
    def get_dl_name(self, i_dl_name: str) -> tuple:
        return self._get_multi([self.setting_controller, i_dl_name], 
                               ('DLNameSettingAtt', 'GetDLName', 'String'), 
                               ('String', 'String', 'String'))

    def get_dl_name_creation_right_info(self, admin_level: str) -> tuple:
        return self.setting_controller.GetDLNameCreationRightInfo(admin_level)
    
    def get_dl_name_exp(self, i_dl_name: str) -> tuple[str, str, str]:
        return self._get_multi([self.setting_controller, i_dl_name], 
                               ('DLNameSettingAtt', 'GetDLNameExp', 'String'), 
                               ('String', 'String', 'String'))  
    
    def get_dl_name_exp(self, i_dl_name: str) -> tuple[bool, str, str]:
        return self.setting_controller.GetDLNameInfo(i_dl_name)
    
    def get_dl_name_list(self) -> tuple:
        return self._get_safe_array(self.setting_controller, "GetDLNameList", 100)
    
    def get_dl_name_sub_list(self, i_dl_name: str) -> tuple:
        return self._get_safe_array(self.setting_controller, "GetDLNameSubList", 100, i_dl_name)
    
    def get_root_dl_name_creation_right_info(self) -> tuple:
        return self.setting_controller.GetRootDLNameCreationRightInfo()
    
    def remove_dl_name(self, i_dl_name: str) -> 'SettingController':
        self.setting_controller.RemoveDLName(i_dl_name)
        return self
    
    def rename_dl_name(self, i_dl_name: str, i_new_name: str) -> 'SettingController':
        self.setting_controller.RenameDLName(i_dl_name, i_new_name)
        return self
        
    def set_dl_name(self, i_dl_name: str, i_real_name_unix: str, i_real_name_nt: str, i_father: str, i_verif_directory: bool) -> 'SettingController':
        self.setting_controller.SetDLName(i_dl_name, i_real_name_unix, i_real_name_nt, i_father, i_verif_directory)
        return self
    
    def set_dl_name_creationg_right_lock(self, i_locked: bool) -> 'SettingController':
        self.setting_controller.SetDLNameCreationRightLock(i_locked)

    def set_dl_name_lock(self, i_dl_name: str, i_locked: bool) -> 'SettingController':
        self.setting_controller.SetDLNameLock(i_dl_name, i_locked)

    def set_root_dl_name_creation_right_lock(self, i_locked: bool) -> 'SettingController':
        self.setting_controller.SetRootDLNameCreationRightLock(i_locked)    

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'