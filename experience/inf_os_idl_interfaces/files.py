from typing import Iterator

from experience.inf_os_idl_interfaces.file import File
from experience.system.collection import Collection

class Files(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Files

    """

    def __init__(self, com):
        super().__init__(com, child=File)
        self.files = com

    def item(self, i_number: int) -> File:
        return File(self.files.Item(i_number))

    def __getitem__(self, n: int) -> File:
        if (n + 1) > self.count():
            raise StopIteration

        return File(self.files.item(n + 1))

    def __iter__(self) -> Iterator[File]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'Files(name="{self.name()}")'
