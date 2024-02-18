from typing import TYPE_CHECKING, Union
from experience.system import SettingController

if TYPE_CHECKING:
    from experience.types import cat_variant

class SettingRepository(SettingController):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         SettingRepository
    """

    def __init__(self, com):
        super().__init__(com)
        self.setting_repository = com

    def get_attr(self, i_attr_name: str) -> tuple:
        return self.setting_repository.GetAttr(i_attr_name)
    
    def get_attr_array(self, i_attr_name: str) -> tuple:
        return self.setting_repository.GetAttrArray(i_attr_name)
    
    def get_attr_info(self, i_attr_name: str) -> tuple[bool, str, str, bool]:
        return self.setting_repository.GetAttrInfo(i_attr_name)
    
    def put_attr(self, i_attr_name: str, i_attr: 'cat_variant') -> 'SettingRepository':
        self.setting_repository.PutAttr(i_attr_name, i_attr)
        return self

    def put_attr_array(self, i_attr_name: str, i_array: tuple) -> 'SettingRepository':
        self.setting_repository.PutAttrArray(i_attr_name, i_array)
        return self

    def set_attr_lock(self, i_attr_name: str, i_locked: bool) -> 'SettingRepository':
        self.setting_repository.SetAttrLock(i_attr_name, i_locked)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'