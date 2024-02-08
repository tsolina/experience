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

    def get_direction(self, o_direction: tuple) -> tuple:
        return self.light_source.GetDirection(o_direction)

    def put_direction(self, o_direction: tuple) -> tuple:
        return self.light_source.PutDirection(o_direction)

    def __repr__(self):
        return f'LightSource(name="{ self.name }")'
