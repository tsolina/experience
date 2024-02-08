from experience.inf_os_idl_interfaces.file_component import FileComponent
from experience.inf_os_idl_interfaces.text_stream import TextStream

class File(FileComponent):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.FileComponent
                |                         File
    """

    def __init__(self, com):
        super().__init__(com)
        self.file = com

    def size(self) -> int:
        return self.file.Size

    def type(self) -> str:
        return self.file.Type

    def open_as_text_stream(self, i_mode: str) -> TextStream:
        return TextStream(self.file.OpenAsTextStream(i_mode))

    def __repr__(self):
        return f'File(name="{ self.name }")'
