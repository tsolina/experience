from typing import Union, TYPE_CHECKING
from experience.system import AnyObject, SystemService
from experience.inf_interfaces.editor import Editor
from experience.inf_interfaces import Editors, Printer, Printers, Service, Window, Windows
from experience.inf_os_idl_interfaces import FileSystem, SystemConfiguration
# from experience.types import DocumentType

if TYPE_CHECKING:
    from experience.inf_interfaces import Services

class Application(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self._com = com
    '''

    def active_document(self) -> Document:
        try:
            active_doc_com = self.com_object.ActiveDocument
            doc_suffix = active_doc_com.Name.split('.')[-1]
            return document_type[doc_suffix](active_doc_com)
        except com_error:
            raise CATIAApplicationException('Is there an active document?')
    '''

    def active_editor(self) -> Editor:
        return Editor(self._com.ActiveEditor)


    def active_printer(self) -> Printer:
        return Printer(self._com.ActivePrinter)


    def active_window(self) -> Window:
        return Window(self._com.ActiveWindow)

    def cache_size(self, value: int = None) -> Union['Application', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self._com.CacheSize = value
            return self
        return self._com.CacheSize

    def caption(self, value: str = None) -> Union['Application', str]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self._com.Caption = value
            return self
        return self._com.Caption

    def display_file_alerts(self, value: bool = None) -> Union['Application', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self._com.DisplayFileAlerts = value
            return self
        return self._com.DisplayFileAlerts


    def editors(self) -> 'Editors':
        return Editors(self._com.Editors)


    def file_system(self) -> 'FileSystem':
        return FileSystem(self._com.FileSystem)

    def full_name(self) -> str:
        return self._com.FullName

    def hso_synchronized(self, value: bool = None) -> Union['Application', bool]:
        if value is not None:
            self._com.HSOSynchronized = value
            return self
        return self._com.HSOSynchronized

    def height(self, value: float = None) -> Union['Application', float]:
        if value is not None:
            self._com.Height = value
            return self
        return self._com.Height

    def interactive(self, value: bool = None) -> Union['Application', bool]:
        if value is not None:
            self._com.Interactive = value
            return self
        return self._com.Interactive

    def left(self, value: float = None) -> Union['Application', float]:
        if value is not None:
            self._com.Left = value
            return self
        return self._com.Left

    def local_cache(self, value: str = None) -> Union['Application', str]:
        if value is not None:
            self._com.LocalCache = value
            return self
        return self._com.LocalCache

    def path(self) -> str:
        return self._com.Path


    def printers(self) -> Printers:
        return Printers(self._com.Printers)

    def refresh_display(self, value: bool = None) -> Union['Application', bool]:
        if value is not None:
            self._com.RefreshDisplay = value
            return self
        return self._com.RefreshDisplay

    def script_command(self, value: int = None) -> Union['Application', int]:
        if value is not None:
            self._com.ScriptCommand = value
            return self
        return self._com.ScriptCommand

    def status_bar(self, value: str = None) -> Union['Application', str]:
        if value is not None:
            self._com.StatusBar = value
            return self
        return self._com.StatusBar


    def system_configuration(self) -> SystemConfiguration:
        return SystemConfiguration(self._com.SystemConfiguration)


    def system_service(self) -> SystemService:
        return SystemService(self._com.SystemService)

    def top(self, value: float = None) -> Union['Application', float]:
        if value is not None:
            self._com.Top = value
            return self
        return self._com.Top

    def undo_redo_lock(self, value: bool = None) -> Union['Application', bool]:
        if value is not None:
            self._com.UndoRedoLock = value
            return self
        return self._com.UndoRedoLock

    def user_interface_language(self) -> str:
        return self._com.UserInterfaceLanguage

    def visible(self, value: bool = None) -> Union['Application', bool]:
        if value is not None:
            self._com.Visible = value
            return self
        return self._com.Visible

    def width(self, value: float = None) -> Union['Application', float]:
        if value is not None:
            self._com.Width = value
            return self
        return self._com.Width


    def windows(self) -> Windows:
        return Windows(self._com.Windows)


    def disable_new_undo_redo_transaction(self) -> None:
        return self._com.DisableNewUndoRedoTransaction()

    def enable_new_undo_redo_transaction(self) -> None:
        return self._com.EnableNewUndoRedoTransaction()

    def file_selection_box(self, i_title: str, i_extension: str, i_mode: int) -> str:
        return self._com.FileSelectionBox(i_title, i_extension, i_mode)

    def folder_selection_box(self, i_title: str) -> str:
        return self._com.FolderSelectionBox(i_title)

    def get_session_service(self, i_service: str) -> Service:
        return Service(self._com.GetSessionService(i_service))

    def services(self) -> 'Services':
        from experience.inf_interfaces import Services
        return Services(self._com)

    def get_workbench_id(self) -> str:
        return self._com.GetWorkbenchId()

    def help(self, i_help_id: str) -> None:
        return self._com.Help(i_help_id)

    def quit(self) -> None:
        return self._com.Quit()

    def start_command(self, i_command_id: str) -> None:
        return self._com.StartCommand(i_command_id)

    def start_workbench(self, iworkbench_id: str) -> None:
        return self._com.StartWorkbench(iworkbench_id)

    def __repr__(self):
        return f'Application(name="{self.name}")'
