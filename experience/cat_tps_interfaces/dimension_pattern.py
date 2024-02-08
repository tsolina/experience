from experience.system import AnyObject

class DimensionPattern(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DimensionPattern
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.dimension_pattern = com_object

    def instance_count(self) -> float:
        return self.dimension_pattern.InstanceCount

    def __repr__(self):
        return f'DimensionPattern(name="{ self.name }")'
