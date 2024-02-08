from experience.inf_interfaces import Camera#, ViewPoint3D


class Camera3D(Camera):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Camera
                |                         Camera3D
    """

    def __init__(self, com):
        super().__init__(com)
        self.camera_3d = com

    def viewpoint_3d(self, value: 'ViewPoint3D' = None) -> 'ViewPoint3D':
        from experience.inf_interfaces import ViewPoint3D
        if value is not None:
            self.camera_3d.Viewpoint3D = value
            return self
        return ViewPoint3D(self.camera_3d.Viewpoint3D)

    def __repr__(self):
        return f'Camera3D(name="{self.name}")'
