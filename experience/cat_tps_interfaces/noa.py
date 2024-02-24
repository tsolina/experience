from typing import TYPE_CHECKING
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.drafting_interfaces import DrawingComponent
    from experience.cat_tps_interfaces import TPSParallelOnScreen
    from experience.types import cat_variant


class Noa(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Noa
    """

    def __init__(self, com):
        super().__init__(com)
        self.noa = com

    def flag_text(self, value: str = None) -> str:
        if value is not None:
            self.noa.FlagText = value
            return self
        return self.noa.FlagText

    def text(self, value: str = None) -> str:
        if value is not None:
            self.noa.Text = value
            return self
        return self.noa.Text

    def add_url(self, i_url: str) -> 'Noa':
        self.noa.AddURL(i_url)
        return self


    def get_ditto(self) -> 'DrawingComponent':
        from experience.drafting_interfaces import DrawingComponent
        return DrawingComponent(self.noa.GetDitto())


    def get_modifiable_text(self, i_index: 'cat_variant') -> AnyObject:
        return AnyObject(self.noa.GetModifiableText(i_index))

    def get_modifiable_texts_count(self) -> int:
        return self.noa.GetModifiableTextsCount()

    def get_nbr_url_2(self) -> int:
        return self.noa.GetNbrURL2()

    def modify_url(self, i_url: str, i_index: 'cat_variant') -> 'Noa':
        self.noa.ModifyURL(i_url, i_index)
        return self

    def remove_url(self, i_index: 'cat_variant') -> 'Noa':
        self.noa.RemoveURL(i_index)
        return self


    def tps_parallel_on_screen(self) -> 'TPSParallelOnScreen':
        from experience.cat_tps_interfaces import TPSParallelOnScreen
        return TPSParallelOnScreen(self.noa.TPSParallelOnScreen())

    def url(self, i_index: 'cat_variant') -> str:
        return self.noa.URL(i_index)