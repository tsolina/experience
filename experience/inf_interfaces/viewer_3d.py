from experience.inf_interfaces import LightSources, Viewer, Viewpoint3D

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

    def clipping_mode(self, value: int = None) -> int:
        if value is not None:
            self.viewer_3d.ClippingMode = value
            return self
        return self.viewer_3d.ClippingMode

    def far_limit(self, value: float = None) -> float:
        if value is not None:
            self.viewer_3d.FarLimit = value
            return self
        return self.viewer_3d.FarLimit

    def foggy(self, value: bool = None) -> bool:
        if value is not None:
            self.viewer_3d.Foggy = value
            return self
        return self.viewer_3d.Foggy

    def ground(self, value: bool = None) -> bool:
        if value is not None:
            self.viewer_3d.Ground = value
            return self
        return self.viewer_3d.Ground

    def light_sources(self) -> LightSources:
        return LightSources(self.viewer_3d.LightSources)

    def lighting_intensity(self, value: float = None) -> float:
        if value is not None:
            self.viewer_3d.LightingIntensity = value
            return self
        return self.viewer_3d.LightingIntensity

    def lighting_mode(self, value: int = None) -> int:
        if value is not None:
            self.viewer_3d.LightingMode = value
            return self
        return self.viewer_3d.LightingMode

    def navigation_style(self, value: int = None) -> int:
        if value is not None:
            self.viewer_3d.NavigationStyle = value
            return self
        return self.viewer_3d.NavigationStyle

    def near_limit(self, value: float = None) -> float:
        if value is not None:
            self.viewer_3d.NearLimit = value
            return self
        return self.viewer_3d.NearLimit

    def rendering_mode(self, value: int = None) -> int:
        if value is not None:
            self.viewer_3d.RenderingMode = value
            return self
        return self.viewer_3d.RenderingMode

    def viewpoint_3d(self, value: Viewpoint3D = None) -> Viewpoint3D:
        if value is not None:
            self.viewer_3d.Viewpoint3D = value
            return self
        return Viewpoint3D(self.viewer_3d.Viewpoint3D)

    def rotate(self, i_axis: tuple, i_angle: float) -> 'Viewer3D':
        self.viewer_3d.Rotate(i_axis, i_angle)
        return self

    def translate(self, i_vector: tuple) -> 'Viewer3D':
        self.viewer_3d.Translate(i_vector)
        return self

    def __repr__(self):
        return f'Viewer3D(name="{self.name}")'
