from typing import Union, TYPE_CHECKING, overload
from experience.system import AnyObject, SystemService
from experience.inf_interfaces.inf_types import *

if TYPE_CHECKING:
    from experience.inf_interfaces import Editor, Editors, Printer, Printers, Service, Window, Windows
    from experience.inf_os_idl_interfaces import FileSystem, SystemConfiguration
    from experience.inf_interfaces import Services
    from experience.inf_os_idl_interfaces.inf_os_types import *
    from experience.inf_os_idl_interfaces.setting_controllers import SettingControllers

class Application(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self._com = com

    def active_editor(self) -> 'Editor':
        from experience.inf_interfaces import Editor
        return Editor(self._com.ActiveEditor)


    def active_printer(self) -> 'Printer':
        from experience.inf_interfaces import Printer
        return Printer(self._com.ActivePrinter)

    def active_window(self) -> 'Window':
        from experience.inf_interfaces import Window
        return Window(self._com.ActiveWindow)

    @overload
    def cache_size(self, value:int) -> 'Application': ...

    @overload
    def cache_size(self, value:None=None) -> int: ... 

    def cache_size(self, value: int = None) -> Union['Application', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self._com.CacheSize = value
            return self
        return self._com.CacheSize

    @overload
    def caption(self, value:str) -> 'Application': ...

    @overload
    def caption(self, value:None=None) -> str: ... 

    def caption(self, value: str = None) -> Union['Application', str]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self._com.Caption = value
            return self
        return self._com.Caption

    @overload
    def display_file_alerts(self, value:bool) -> 'Application': ...

    @overload
    def display_file_alerts(self, value:None=None) -> bool: ... 

    def display_file_alerts(self, value: bool = None) -> Union['Application', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self._com.DisplayFileAlerts = value
            return self
        return self._com.DisplayFileAlerts


    def editors(self) -> 'Editors':
        from experience.inf_interfaces import Editors
        return Editors(self._com.Editors)


    def file_system(self) -> 'FileSystem':
        from experience.inf_os_idl_interfaces import FileSystem
        return FileSystem(self._com.FileSystem)

    def full_name(self) -> str:
        return self._com.FullName

    @overload
    def hso_synchronized(self, value:bool) -> 'Application': ...

    @overload
    def hso_synchronized(self, value:None=None) -> bool: ... 

    def hso_synchronized(self, value: bool = None) -> Union['Application', bool]:
        if value is not None:
            self._com.HSOSynchronized = value
            return self
        return self._com.HSOSynchronized

    @overload
    def height(self, value:float) -> 'Application': ...

    @overload
    def height(self, value:None=None) -> float: ... 

    def height(self, value: float = None) -> Union['Application', float]:
        if value is not None:
            self._com.Height = value
            return self
        return self._com.Height

    @overload
    def interactive(self, value:bool) -> 'Application': ...

    @overload
    def interactive(self, value:None=None) -> bool: ... 
    
    def interactive(self, value: bool = None) -> Union['Application', bool]:
        if value is not None:
            self._com.Interactive = value
            return self
        return self._com.Interactive

    @overload
    def left(self, value:float) -> 'Application': ...

    @overload
    def left(self, value:None=None) -> float: ... 

    def left(self, value: float = None) -> Union['Application', float]:
        if value is not None:
            self._com.Left = value
            return self
        return self._com.Left

    @overload
    def local_cache(self, value:str) -> 'Application': ...

    @overload
    def local_cache(self, value:None=None) -> str: ... 

    def local_cache(self, value: str = None) -> Union['Application', str]:
        if value is not None:
            self._com.LocalCache = value
            return self
        return self._com.LocalCache

    def path(self) -> str:
        return self._com.Path


    def printers(self) -> 'Printers':
        from experience.inf_interfaces import Printers
        return Printers(self._com.Printers)

    @overload
    def refresh_display(self, value:bool) -> 'Application': ...

    @overload
    def refresh_display(self, value:None=None) -> bool: ... 

    def refresh_display(self, value: bool = None) -> Union['Application', bool]:
        if value is not None:
            self._com.RefreshDisplay = value
            return self
        return self._com.RefreshDisplay

    @overload
    def script_command(self, value:CatScriptCommand) -> 'Application': ...

    @overload
    def script_command(self, value:None=None) -> CatScriptCommand: ...

    def script_command(self, value: CatScriptCommand = None) -> Union['Application', CatScriptCommand]:
        if value is not None:
            self._com.ScriptCommand = int(value)
            return self
        return CatScriptCommand.item(self._com.ScriptCommand)
    
    def setting_controllers(self) -> 'SettingControllers':
        from experience.inf_os_idl_interfaces.setting_controllers import SettingControllers
        return SettingControllers(self._com.SettingControllers)

    @overload
    def status_bar(self, value:str) -> 'Application': ...

    @overload
    def status_bar(self, value:None=None) -> str: ...

    def status_bar(self, value: str = None) -> Union['Application', str]:
        if value is not None:
            self._com.StatusBar = value
            return self
        return self._com.StatusBar


    def system_configuration(self) -> 'SystemConfiguration':
        from experience.inf_os_idl_interfaces import SystemConfiguration
        return SystemConfiguration(self._com.SystemConfiguration)


    def system_service(self) -> SystemService:
        return SystemService(self._com.SystemService)
    
    @overload
    def top(self, value:float) -> 'Application': ...

    @overload
    def top(self, value:None=None) -> float: ...

    def top(self, value: float = None) -> Union['Application', float]:
        if value is not None:
            self._com.Top = value
            return self
        return self._com.Top
    
    @overload
    def undo_redo_lock(self, value:bool) -> 'Application': ...

    @overload
    def undo_redo_lock(self, value:None=None) -> bool: ... 

    def undo_redo_lock(self, value: bool = None) -> Union['Application', bool]:
        if value is not None:
            self._com.UndoRedoLock = value
            return self
        return self._com.UndoRedoLock

    def user_interface_language(self) -> str:
        return self._com.UserInterfaceLanguage
    
    @overload
    def visible(self, value:bool) -> 'Application': ...

    @overload
    def visible(self, value:None=None) -> bool: ... 

    def visible(self, value: bool = None) -> Union['Application', bool]:
        if value is not None:
            self._com.Visible = value
            return self
        return self._com.Visible
    
    @overload
    def width(self, value:float) -> 'Application': ...

    @overload
    def width(self, value:None=None) -> float: ...

    def width(self, value: float = None) -> Union['Application', float]:
        if value is not None:
            self._com.Width = value
            return self
        return self._com.Width


    def windows(self) -> 'Windows':
        from experience.inf_interfaces import Windows
        return Windows(self._com.Windows)

    def disable_new_undo_redo_transaction(self) -> 'Application':
        self._com.DisableNewUndoRedoTransaction()
        return self

    def enable_new_undo_redo_transaction(self) -> 'Application':
        self._com.EnableNewUndoRedoTransaction()
        return self

    def file_selection_box(self, i_title: str, i_extension: str, i_mode: 'CatFileSelectionMode') -> str:
        return self._com.FileSelectionBox(i_title, i_extension, int(i_mode))

    def folder_selection_box(self, i_title: str) -> str:
        return self._com.FolderSelectionBox(i_title)

    def get_session_service(self, i_service: str) -> 'Service':
        from experience.inf_interfaces import Service
        return Service(self._com.GetSessionService(i_service))

    def services(self) -> 'Services':
        from experience.inf_interfaces import Services
        return Services(self._com)

    def get_workbench_id(self) -> str:
        return self._com.GetWorkbenchId()

    def help(self, i_help_id: str) -> 'Application':
        self._com.Help(i_help_id)
        return self

    def quit(self) -> 'Application':
        self._com.Quit()
        return self

    def start_command(self, i_command_id: str) -> 'Application':
        self._com.StartCommand(i_command_id)
        return self

    def start_workbench(self, iworkbench_id: str) -> 'Application':
        self._com.StartWorkbench(iworkbench_id)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
