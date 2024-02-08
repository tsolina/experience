from experience.system import CATBaseDispatch

class DrawingTextRange(CATBaseDispatch):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 DrawingTextRange
    """

    def __init__(self, com):
        super().__init__()
        self.drawing_text_range = com

    def length(self) -> int:
        return self.drawing_text_range.Length

    def start(self) -> int:
        return self.drawing_text_range.Start

    def text(self, value: str = None) -> str:
        if value is not None:
            self.drawing_text_range.Text = value
            return self
        return self.drawing_text_range.Text

    def get_text_range(self, i_start: int, i_end: int) -> 'DrawingTextRange':
        return DrawingTextRange(self.drawing_text_range.GetTextRange(i_start, i_end))

    def insert_after(self, i_string: str) -> 'DrawingTextRange':
        self.drawing_text_range.InsertAfter(i_string)
        return self

    def insert_before(self, i_string: str) -> 'DrawingTextRange':
        self.drawing_text_range.InsertBefore(i_string)
        return self

    def __repr__(self):
        return f'DrawingTextRange()'
