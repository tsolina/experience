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

    def get_origin(self) -> tuple[float, float]:
        return self._get_safe_array(self.viewpoint_2d, "GetOrigin", 1)

    def put_origin(self, o_origin: tuple[float, float]) -> 'Viewpoint2D':
        self.viewpoint_2d.PutOrigin(o_origin)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'