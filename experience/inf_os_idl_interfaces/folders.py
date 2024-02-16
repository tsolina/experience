from typing import Iterator

from experience.inf_os_idl_interfaces.folder import Folder
from experience.system.collection import Collection

class Folders(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Folders
    """

    def __init__(self, com):
        super().__init__(com, child=Folder)
        self.folders = com

    def item(self, i_number: int) -> Folder:
        return Folder(self.folders.Item(i_number))

    def __getitem__(self, n: int) -> Folder:
        if (n + 1) > self.count():
            raise StopIteration

        return Folder(self.folders.item(n + 1))

    def __iter__(self) -> Iterator[Folder]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'Folders(name="{self.name()}")'
