from experience.system import AnyObject
from experience.cat_tps_interfaces import Text, TPSHyperLinkManager

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from experience.cat_tps_interfaces import Annotations

class TPSView(AnyObject):

    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TPSView
    """

    def __init__(self, com):
        super().__init__(com)
        self.tps_view = com

    def annotation_plane(self) -> tuple:
        return self.tps_view.AnnotationPlane

    def annotation_sketch(self, value: AnyObject = None): # -> 'AnnotationSketch':
        if value is not None:
            self.tps_view.AnnotationSketch = value
            return self
        return self.tps_view.AnnotationSketch


    def Annotations(self) -> 'Annotations':
        from experience.cat_tps_interfaces import Annotations
        return Annotations(self.tps_view.Annotations)

    def display_ratio(self, value: float = None) -> float:
        if value is not None:
            self.tps_view.DisplayRatio = value
            return self
        return self.tps_view.DisplayRatio

    def view_type(self) -> int:
        return self.tps_view.ViewType

    def add_view_text(self) -> Text:
        return self.tps_view.Text()

    def get_view_text(self) -> Text:
        return self.tps_view.GetViewText()

    def has_view_text(self) -> bool:
        return self.tps_view.HasViewText()


    def hyper_link_manager(self) -> TPSHyperLinkManager:
        return TPSHyperLinkManager(self.tps_view.TPSHyperLinkManager())

    def __repr__(self):
        return f'TPSView(name="{ self.name() }")'
