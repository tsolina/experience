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

    def __init__(self, com):
        super().__init__(com)
        self.dimension_pattern = com

    def instance_count(self) -> float:
        return self.dimension_pattern.InstanceCount

    def __repr__(self):
        return f'DimensionPattern(name="{ self.name() }")'
