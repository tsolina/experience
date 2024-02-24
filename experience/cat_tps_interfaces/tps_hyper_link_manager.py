from experience.system import AnyObject
from experience.types import cat_variant

class TPSHyperLinkManager(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.tps_manager = com

    def get_nbr_url_2(self) -> int:
        return self.tps_manager.GetNbrURL2()

    def url(self, i_index: cat_variant) -> str:
        return self.tps_manager.URL(i_index)