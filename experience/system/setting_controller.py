from experience.system import AnyObject

class SettingController(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SettingController
    """

    def __init__(self, com):
        super().__init__(com)
        self.setting_controller = com

    def commit(self) -> 'SettingController':
        return self.setting_controller.Commit()

    def reset_to_admin_values(self) -> 'SettingController':
        return self.setting_controller.ResetToAdminValues()
    
    def reset_to_admin_values_by_name(self, i_att_list: tuple) -> 'SettingController':
        return self.setting_controller.ResetToAdminValuesByName(i_att_list)

    def rollback(self) -> 'SettingController':
        return self.setting_controller.Rollback()
    
    def save_repository(self) -> 'SettingController':
        return self.setting_controller.SaveRepository()

    def __repr__(self):
        return f'SettingController(name="{self.name()}")'