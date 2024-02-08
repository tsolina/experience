from experience.system import AnyObject
from experience.cat_annotation_interfaces import DrawingText
from experience.cat_tps_interfaces import TPSParallelOnScreen

class Text(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.text_com = com


    def text(self, value: str = None) -> str:
        if value is not None:
            self.text_com.Text = value
            return self
        return self.text_com.Text

    def get_2d_annot(self) -> DrawingText:
        return DrawingText(self.text_com.Get2dAnnot())

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        return TPSParallelOnScreen(self.text_com.TPSParallelOnScreen())

    def __repr__(self):
        return f'Text(name="{self.name}")'
