from experience.cat_tps_interfaces import TPSView
from experience.system import AnyObject
from experience.inf_interfaces import Reference
from experience.types import cat_variant

class TPSViewFactory(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TPSViewFactory
    """

    def __init__(self, com):
        super().__init__(com)
        self.tps_view_factory = com

    def create_view(self, i_plane: Reference, i_view_type: cat_variant) -> TPSView:
        return TPSView(self.tps_view_factory.CreateView(i_plane, i_view_type))

    def __repr__(self):
        return f'TPSViewFactory(name="{self.name()}")'
