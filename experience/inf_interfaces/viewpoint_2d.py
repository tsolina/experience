from experience.system.any_object import AnyObject

class Viewpoint2D(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Viewpoint2D
    """

    def __init__(self, com):
        super().__init__(com)
        self.viewpoint_2d = com

    def zoom(self, value: float = None) -> float:
        if value is not None:
            self.viewpoint_2d.Zoom = value
            return self
        return self.viewpoint_2d.Zoom

    def get_origin(self, o_origin: tuple) -> tuple:
        return self.viewpoint_2d.GetOrigin(o_origin)

    def put_origin(self, o_origin: tuple) -> tuple:
        return self.viewpoint_2d.PutOrigin(o_origin)

    def __repr__(self):
        return f'Viewpoint2D(name="{self.name}")'
