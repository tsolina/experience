from experience.system.any_object import AnyObject
from experience.inf_os_idl_interfaces.file import File
from experience.inf_os_idl_interfaces.folder import Folder

class FileSystem(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FileSystem
    """

    def __init__(self, com):
        super().__init__(com)
        self.file_system = com

    def file_separator(self) -> str:
        return self.file_system.FileSeparator

    def path_separator(self) -> str:
        return self.file_system.PathSeparator

    @property
    def temporary_directory(self) -> Folder:
        return Folder(self.file_system.TemporaryDirectory)

    def concatenate_paths(self, i_path_chunk1: str, i_path_chunk2: str) -> str:
        return self.file_system.ConcatenatePaths(i_path_chunk1, i_path_chunk2)

    def copy_file(self, i_path_source: str, i_path_destination: str, i_overwrite: bool) -> 'FileSystem':
        self.file_system.CopyFile(i_path_source, i_path_destination, i_overwrite)
        return self

    def copy_folder(self, i_source_path: str, i_destination_path: str) -> 'FileSystem':
        self.file_system.CopyFolder(i_source_path, i_destination_path)
        return self

    def create_file(self, i_path: str, i_overwrite: bool) -> File:
        return File(self.file_system.CreateFile(i_path, i_overwrite))

    def create_folder(self, i_path: str) -> Folder:
        return Folder(self.file_system.CreateFolder(i_path))

    def delete_file(self, i_path: str) -> 'FileSystem':
        self.file_system.DeleteFile(i_path)
        return self

    def delete_folder(self, i_path: str) -> 'FileSystem':
        self.file_system.DeleteFolder(i_path)
        return self

    def file_exists(self, i_path: str) -> bool:
        return self.file_system.FileExists(i_path)

    def folder_exists(self, i_path: str) -> bool:
        return self.file_system.FolderExists(i_path)

    def get_file(self, i_path: str) -> File:
        return File(self.file_system.GetFile(i_path))

    def get_folder(self, i_path: str) -> Folder:
        return Folder(self.file_system.GetFolder(i_path))

    def __repr__(self):
        return f'FileSystem(name="{self.name}")'
