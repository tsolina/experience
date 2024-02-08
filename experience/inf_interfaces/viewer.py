from typing import TYPE_CHECKING

from experience.inf_interfaces import Camera
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.inf_interfaces import Viewer2D, Viewer3D

class Viewer(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.viewer = com

    def full_screen(self, value: bool = None) -> bool:
        if value is not None:
            self.viewer.FullScreen = value
            return self
        return self.viewer.FullScreen

    def height(self, value: int = None) -> int:
        if value is not None:
            self.viewer.Height = value
            return self
        return self.viewer.Height

    def width(self, value: int = None) -> int:
        if value is not None:
            self.viewer.Width = value
            return self
        return self.viewer.Width

    def activate(self) -> 'Viewer':
        self.viewer.Activate()
        return self

    def capture_to_file(self, i_format: int, i_file: str) -> 'Viewer':
        return self.viewer.CaptureToFile(i_format, i_file)
        return self

    def get_background_color(self) -> tuple:
        return self._get_safe_array(self._com, "GetBackgroundColor", 2)

    def create_viewer_2d(self) -> 'Viewer2D':
        from experience.inf_interfaces.viewer_2d import Viewer2D

        return Viewer2D(self._vba_cast(self.viewer, "Viewer2D"))

    def create_viewer_3d(self) -> 'Viewer3D':
        from experience.inf_interfaces import Viewer3D

        # return Viewer3D(self._vba_cast(self.viewer, "Viewer3D"))
        return self.as_pyclass(Viewer3D)

    @property
    def new_camera(self) -> Camera:
        return Camera(self.viewer.NewCamera())

    def put_background_color(self, color: tuple) -> 'Viewer':
        self.viewer.PutBackgroundColor(color)
        return self

    def reframe(self) -> 'Viewer':
        self.viewer.Reframe()
        return self

    def update(self) -> 'Viewer':
        self.viewer.Update()
        return self

    def zoom_in(self) -> 'Viewer':
        self.viewer.ZoomIn()
        return self

    def zoom_out(self) -> 'Viewer':
        self.viewer.ZoomOut()
        return self

    def __repr__(self):
        return f'Viewer(name="{self.name}")'
