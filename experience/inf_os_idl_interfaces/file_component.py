from typing import TYPE_CHECKING

from experience.system import AnyObject

# if TYPE_CHECKING:
#     from experience.inf_os_idl_interfaces.folder import Folder

class FileComponent(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FileComponent
    """

    def __init__(self, com):
        super().__init__(com)
        self.file_component = com

    @property
    def parent_folder(self) -> 'Folder':
        from experience.inf_os_idl_interfaces.folder import Folder
        return Folder(self.file_component.ParentFolder)

    @parent_folder.setter
    def parent_folder(self, value: 'Folder'):
        self.file_component.ParentFolder = value

    @property
    def path(self) -> str:
        return self.file_component.Path

    def __repr__(self):
        return f'FileComponent(name="{self.name}")'
