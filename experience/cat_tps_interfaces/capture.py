from typing import TYPE_CHECKING

from experience.inf_interfaces import Camera3D
from experience.system import AnyObject
from experience.cat_tps_interfaces import TPSView, TPSViews, TPSParallelOnScreen

if TYPE_CHECKING:
    from experience.cat_tps_interfaces import Annotations, AnnotationSet

class Capture(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Capture
    """

    def __init__(self, com):
        super().__init__(com)
        self.capture = com

    def active_view(self, value: TPSView = None) -> TPSView:
        if value is not None:
            self.capture.ActiveView = value
            return self
        return TPSView(self.capture.ActiveView)

    def active_view_state(self, value: bool = None) -> bool:
        if value is not None:
            self.capture.ActiveViewState = value
            return self
        return self.capture.ActiveViewState

    def annotations(self, value: 'Annotations' = None) -> 'Annotations':
        from experience.cat_tps_interfaces import Annotations
        if value is not None:
            self.capture.Annotations = value
            return self
        return Annotations(self.capture.Annotations)

    def camera(self, value: Camera3D = None) -> Camera3D:
        if value is not None:
            self.capture.Camera = value
            return self
        return Camera3D(self.capture.Camera)

    def clipping_plane(self, value: bool = None) -> bool:
        if value is not None:
            self.capture.ClippingPlane = value
            return self
        return self.capture.ClippingPlane

    def current(self, value: bool = None) -> bool:
        if value is not None:
            self.capture.Current = value
            return self
        return self.capture.Current

    def manage_hide_show_body(self, value: bool = None) -> bool:
        if value is not None:
            self.capture.ManageHideShowBody = value
            return self
        return self.capture.ManageHideShowBody


    def set(self) -> 'AnnotationSet':
        from experience.cat_tps_interfaces import AnnotationSet
        return AnnotationSet(self.capture.Set)

    def tps_views(self, value: TPSView = None) -> TPSViews:
        if value is not None:
            self.capture.TPSViews = value
            return self
        return TPSViews(self.capture.TPSViews)

    def view_point(self, value: bool = None) -> bool:
        if value is not None:
            self.capture.ViewPoint = value
            return self
        return self.capture.ViewPoint

    def display_capture(self) -> 'Capture':
        self.capture.DisplayCapture()
        return self

    def display_capture_2(self, ib_apply_mirror: bool) -> 'Capture':
        self.capture.DisplayCapture2(ib_apply_mirror)
        return self


    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        return TPSParallelOnScreen(self.capture.TPSParallelOnScreen())

    def __repr__(self):
        return f'Capture(name="{self.name}")'
