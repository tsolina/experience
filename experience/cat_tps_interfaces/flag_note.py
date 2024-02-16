from experience.system import AnyObject
from experience.cat_annotation_interfaces import DrawingText
from experience.cat_tps_interfaces import TPSParallelOnScreen
from experience.types import cat_variant

class FlagNote(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FlagNote
    """

    def __init__(self, com):
        super().__init__(com)
        self.flag_note = com

    def flag_note_text(self, value: str = None) -> str:
        if value is not None:
            self.flag_note.FlagNoteText = value
            return self
        return self.flag_note.FlagNoteText

    def text(self, value: str = None) -> str:
        if value is not None:
            self.flag_note.Text = value
            return self
        return self.flag_note.Text

    def add_url(self, i_url: str) -> 'FlagNote':
        self.flag_note.AddURL(i_url)
        return FlagNote


    def get_2d_annot(self) -> DrawingText:
        return DrawingText(self.flag_note.DrawingText())

    def get_nbr_url2(self, o_number_of_url: cat_variant) -> tuple: #, o_number_of_url: cat_variant
        return self.flag_note.GetNbrURL2(o_number_of_url)

    def modify_url(self, i_url: str, i_index: cat_variant) -> 'FlagNote':
        self.flag_note.ModifyURL(i_url, i_index)
        return self

    def remove_url(self, i_index: cat_variant) -> 'FlagNote':
        self.flag_note.RemoveURL(i_index)
        return self


    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        return TPSParallelOnScreen(self.flag_note.TPSParallelOnScreen())

    def url(self, i_index: cat_variant) -> str:
        return self.flag_note.URL(i_index)

    def __repr__(self):
        return f'FlagNote(name="{self.name()}")'
