from typing import TYPE_CHECKING, Union
from experience.system import SettingController

if TYPE_CHECKING:
    from experience.system.system_types import CATScriptLanguage

class MacrosSettingAtt(SettingController):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         MacrosSettingAtt
    """

    def __init__(self, com):
        super().__init__(com)
        self.macros_setting_att = com

    def get_default_macro_libraries(self) -> tuple:
        return self.macros_setting_att.GetDefaultMacroLibraries()
    
    def get_default_macro_libraries_info(self) -> tuple[bool, str, str]:
        return self.macros_setting_att.GetDefaultMacroLibrariesInfo()
    
    def get_external_references(self) -> tuple:
        return self.macros_setting_att.GetExternalReferences()
    
    def get_external_references_info(self) -> tuple[bool, str, str]:
        return self.macros_setting_att.GetExternalReferencesInfo()
    
    def get_language_editor(self, i_language: 'CATScriptLanguage') -> str:
        return self.macros_setting_att.GetLanguageEditor(int(i_language))
    
    def get_language_editor_info(self) -> tuple[bool, str, str]:
        return self.macros_setting_att.GetLanguageEditorInfo()
    
    def set_default_macro_libraries(self, i_libraries: tuple) -> 'MacrosSettingAtt':
        self.macros_setting_att.SetDefaultMacroLibraries(i_libraries)
        return self
    
    def set_default_macro_libraries_lock(self, i_locked: bool) -> 'MacrosSettingAtt':
        self.macros_setting_att.SetDefaultMacroLibrariesLock(i_locked)
        return self

    def set_external_references(self, i_references: tuple) -> 'MacrosSettingAtt':
        self.macros_setting_att.SetExternalReferences(i_references)
        return self
    
    def set_external_references_lock(self, i_locked: bool) -> 'MacrosSettingAtt':
        self.macros_setting_att.SetExternalReferencesLock(i_locked)
        return self
    
    def set_language_editor(self, i_language: 'CATScriptLanguage', i_editor_path: str) -> 'MacrosSettingAtt':
        self.macros_setting_att.SetLanguageEditor(int(i_language), i_editor_path)
        return self
    
    def set_language_editor_lock(self, i_locked: bool) -> 'MacrosSettingAtt':
        self.macros_setting_att.SetLanguageEditorLock(i_locked)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'