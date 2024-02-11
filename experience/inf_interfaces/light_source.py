from experience.system.any_object import AnyObject

class LightSource(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     LightSource
    """

    def __init__(self, com):
        super().__init__(com)
        self.light_source = com

    def get_direction(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.light_source, "GetDirection", 2)

    def put_direction(self, i_direction: tuple[float, float, float]) -> 'LightSource':
        self.light_source.PutDirection(i_direction)
        return self

    def __repr__(self):
        return f'LightSource(name="{ self.name()}")'
