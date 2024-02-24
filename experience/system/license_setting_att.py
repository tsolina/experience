from typing import TYPE_CHECKING, Union
from experience.system import SettingController


class LicenseSettingAtt(SettingController):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         LicenseSettingAtt
    """

    def __init__(self, com):
        super().__init__(com)
        self.license_setting_att = com

    def frequency(self, value: float = None) -> Union['LicenseSettingAtt', float]:
        if value is not None:
            self.license_setting_att.Frequency = value
            return self
        return self.license_setting_att.Frequency
    
    def nodelock_alert(self, value: int = None) -> Union['LicenseSettingAtt', int]:
        if value is not None:
            self.license_setting_att.NodelockAlert = value
            return self
        return self.license_setting_att.NodelockAlert
    
    def server_time_out(self, value: float = None) -> Union['LicenseSettingAtt', float]:
        if value is not None:
            self.license_setting_att.ServerTimeOut = value
            return self
        return self.license_setting_att.ServerTimeOut
    
    def show_license(self, value: bool = None) -> Union['LicenseSettingAtt', bool]:
        if value is not None:
            self.license_setting_att.ShowLicense = value
            return self
        return self.license_setting_att.ShowLicense
    
    def get_frequency_info(self) -> tuple: # should be bool, str, str
        return self.license_setting_att.GetFrequencyInfo()
    
    def get_license(self, i_license: str) -> str:
        return self.license_setting_att.GetLicense(i_license)
    
    def get_license_info(self, i_license: str) -> tuple: # should be bool, str, str
        return self.license_setting_att.GetLicenseInfo(i_license)
    
    def get_licenses_list(self, i_default_licenses: int) -> tuple:
        return self.license_setting_att.GetLicensesList(i_default_licenses)
    
    def get_license_list_info(self) -> tuple: # should be bool, str, str
        return self.license_setting_att.GetLicensesListInfo()
    
    def get_nodelock_alert_info(self) -> tuple: # should be bool, str, str
        return self.license_setting_att.GetNodelockAlertInfo()
    
    def get_server_time_out_info(self) -> tuple: # should be bool, str, str
        return self.license_setting_att.GetServerTimeOutInfo()
    
    def get_show_license_info(self) -> tuple: # should be bool, str, str
        return self.license_setting_att.GetShowLicenseInfo()
    
    def set_frequency_lock(self, i_lock: bool) -> 'LicenseSettingAtt':
        self.license_setting_att.SetFrequencyLock(i_lock)
        return self
    
    def set_license(self, i_license: str, i_value: str) -> 'LicenseSettingAtt':
        self.license_setting_att.SetLicense(i_license, i_value)
        return self
    
    def set_license_lock(self, i_license: str, i_lock: bool) -> 'LicenseSettingAtt':
        self.license_setting_att.SetLicenseLock(i_license, i_lock)
        return self
    
    def set_licenses_list_lock(self, i_lock: bool) -> 'LicenseSettingAtt':
        self.license_setting_att.SetLicensesListLock(i_lock)
        return self
    
    def set_nodelock_alert_lock(self, i_lock: bool) -> 'LicenseSettingAtt':
        self.license_setting_att.SetNodelockAlertLock(i_lock)
        return self
    
    def set_server_time_out_lock(self, i_lock: bool) -> 'LicenseSettingAtt':
        self.license_setting_att.SetServerTimeOutLock(i_lock)
        return self
    
    def set_show_licenses_lock(self, i_lock: bool) -> 'LicenseSettingAtt':
        self.license_setting_att.SetShowLicenseLock(i_lock)
        return self

    # def __repr__(self):
    #     return f'{self.__class__.__name__}(name="{self.name()}")'