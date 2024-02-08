from experience.system.any_object import AnyObject

class TextStream(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TextStream
    """

    def __init__(self, com):
        super().__init__(com)
        self.text_stream = com

    def at_end_of_line(self) -> bool:
        return self.text_stream.AtEndOfLine

    def at_end_of_stream(self) -> bool:
        return self.text_stream.AtEndOfStream

    def close(self) -> 'TextStream':
        return self.text_stream.Close()
        return self

    def read(self, i_num_of_char: int) -> str:
        return self.text_stream.Read(i_num_of_char)

    def read_line(self) -> str:
        return self.text_stream.ReadLine()

    def write(self, i_written_string: str) -> 'TextStream':
        self.text_stream.Write(i_written_string)
        return self

    def __repr__(self):
        return f'TextStream(name="{ self.name }")'
