from typing import TYPE_CHECKING, Union
from experience.system import SettingController


class DynLicenseSettingAtt(SettingController):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         DynLicenseSettingAtt
    """

    def __init__(self, com):
        super().__init__(com)
        self.dyn_license_setting_att = com

    def get_license(self, i_license: str) -> str:
        return self.dyn_license_setting_att.GetLicense()
    
    def get_license_info(self, i_license: str) -> tuple:
        return self.dyn_license_setting_att.GetLicenseInfo(i_license)
    
    def get_licenses_list(self) -> tuple:
        return self.dyn_license_setting_att.GetLicensesList()
    
    def get_licenses_list_info(self) -> tuple:
        return self.dyn_license_setting_att.GetLicensesListInfo()
    
    def set_license(self, i_license: str, i_value: str) -> 'DynLicenseSettingAtt':
        self.dyn_license_setting_att.SetLicense(i_license, i_value)
        return self
    
    def set_license_lock(self, i_license: str, i_lock: bool) -> 'DynLicenseSettingAtt':
        self.dyn_license_setting_att.SetLicense(i_license, i_lock)
        return self
    
    def set_licenses_list_lock(self, i_lock: bool) -> 'DynLicenseSettingAtt':
        self.dyn_license_setting_att.SetLicensesListLock(i_lock)
        return self
    

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'