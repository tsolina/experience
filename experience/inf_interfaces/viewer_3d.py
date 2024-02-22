from typing import TYPE_CHECKING, Union
from experience.inf_interfaces.inf_types import *
from experience.inf_interfaces import Viewer

if TYPE_CHECKING:
    from experience.inf_interfaces import LightSources, Viewpoint3D

class Viewer3D(Viewer):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Viewer
                |                         Viewer3D
    """

    def __init__(self, com):
        super().__init__(com)
        self.viewer_3d = com

    def clipping_mode(self, value: CatClippingMode = None) -> Union['Viewer3D', CatClippingMode]:
        if value is not None:
            self.viewer_3d.ClippingMode = int(value)
            return self
        return CatClippingMode.item(self.viewer_3d.ClippingMode)

    def far_limit(self, value: float = None) -> Union['Viewer3D', float]:
        if value is not None:
            self.viewer_3d.FarLimit = value
            return self
        return self.viewer_3d.FarLimit

    def foggy(self, value: bool = None) -> Union['Viewer3D', bool]:
        if value is not None:
            self.viewer_3d.Foggy = value
            return self
        return self.viewer_3d.Foggy

    def ground(self, value: bool = None) -> Union['Viewer3D', bool]:
        if value is not None:
            self.viewer_3d.Ground = value
            return self
        return self.viewer_3d.Ground

    def light_sources(self) -> 'LightSources':
        from experience.inf_interfaces import LightSources
        return LightSources(self.viewer_3d.LightSources)

    def lighting_intensity(self, value: float = None) -> Union['Viewer3D', float]:
        if value is not None:
            self.viewer_3d.LightingIntensity = value
            return self
        return self.viewer_3d.LightingIntensity

    def lighting_mode(self, value: CatLightingMode = None) -> Union['Viewer3D', CatLightingMode]:
        if value is not None:
            self.viewer_3d.LightingMode = int(value)
            return self
        return CatLightingMode.item(self.viewer_3d.LightingMode)

    def navigation_style(self, value: CatNavigationStyle = None) -> Union['Viewer3D', CatNavigationStyle]:
        if value is not None:
            self.viewer_3d.NavigationStyle = int(value)
            return self
        return CatNavigationStyle.item(self.viewer_3d.NavigationStyle)

    def near_limit(self, value: float = None) -> Union['Viewer3D', float]:
        if value is not None:
            self.viewer_3d.NearLimit = value
            return self
        return self.viewer_3d.NearLimit

    def rendering_mode(self, value: CatRenderingMode = None) -> Union['Viewer3D', CatRenderingMode]:
        if value is not None:
            self.viewer_3d.RenderingMode = int(value)
            return self
        return CatRenderingMode.item(self.viewer_3d.RenderingMode)

    def viewpoint_3d(self, value: 'Viewpoint3D' = None) -> Union['Viewer3D', 'Viewpoint3D']:
        if value is not None:
            self.viewer_3d.Viewpoint3D = value
            return self
        from experience.inf_interfaces import Viewpoint3D
        return Viewpoint3D(self.viewer_3d.Viewpoint3D)

    def rotate(self, i_axis: tuple, i_angle: float) -> 'Viewer3D':
        self.viewer_3d.Rotate(i_axis, i_angle)
        return self

    def translate(self, i_vector: tuple) -> 'Viewer3D':
        self.viewer_3d.Translate(i_vector)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'