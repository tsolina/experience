from typing import TYPE_CHECKING

from experience.inf_os_idl_interfaces.file_component import FileComponent
from experience.inf_os_idl_interfaces.files import Files

if TYPE_CHECKING:
    from experience.inf_os_idl_interfaces.folders import Folders

class Folder(FileComponent):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.FileComponent
                |                         Folder
    """

    def __init__(self, com):
        super().__init__(com)
        self.folder = com

    def files(self) -> Files:
        return Files(self.folder.Files)

    def sub_folders(self) -> 'Folders':
        from experience.inf_os_idl_interfaces.folders import Folders 
        return Folders(self.folder.SubFolders)

    def __repr__(self):
        return f'Folder(name="{self.name()}")'
