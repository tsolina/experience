from typing import TYPE_CHECKING, Union
from experience.system.any_object import AnyObject
from experience.inf_interfaces.inf_types import *

if TYPE_CHECKING:
    from experience.inf_interfaces import PageSetup, Viewer, Viewers

class Window(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Window
    """

    def __init__(self, com):
        super().__init__(com)
        self.window = com

    def active_viewer(self) -> 'Viewer':
        from experience.inf_interfaces import Viewer
        return Viewer(self.window.ActiveViewer)

    def caption(self, value: str = None) -> Union['Window', str]:
        if value is not None:
            self.window.Caption = value
            return self
        return self.window.Caption

    def height(self, value: int = None) -> Union['Window', int]:
        if value is not None:
            self.window.Height = value
            return self
        return self.window.Height

    def left(self, value: int = None) -> Union['Window', int]:
        if value is not None:
            self.window.Left = value
            return self
        return self.window.Left

    def page_setup(self, value: 'PageSetup' = None) -> Union['Window', 'PageSetup']:
        if value is not None:
            self.window.Left = value
            return self
        from experience.inf_interfaces import PageSetup
        return PageSetup(self.window.PageSetup)

    def top(self, value: int = None) -> Union['Window', int]:
        if value is not None:
            self.window.Top = value
            return self
        return self.window.Top

    def viewers(self) -> 'Viewers':
        from experience.inf_interfaces import Viewers
        return Viewers(self.window.Viewers)

    def width(self, value: int = None) -> Union['Window', int]:
        if value is not None:
            self.window.Width = value
            return self
        return self.window.Width

    def window_state(self, value: CatWindowState = None) -> Union['Window', CatWindowState]:
        if value is not None:
            self.window.WindowState = int(value)
            return self
        return CatWindowState.item(self.window.WindowState)

    def activate(self) -> 'Window':
        self.window.Activate()
        return self

    def activate_next(self) -> 'Window':
        self.window.ActivateNext()
        return self

    def activate_previous(self) -> 'Window':
        self.window.ActivatePrevious()
        return self

    def close(self) -> 'Window':
        self.window.Close()
        return self

    def new_window(self) -> 'Window':
        return Window(self.window.NewWindow())

    def print_out(self) -> 'Window':
        self.window.PrintOut()
        return self

    def print_to_file(self, file_name: str) -> 'Window':
        self.window.PrintToFile(file_name)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'