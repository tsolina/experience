from experience.system import AnyObject

class MedianFeature(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MedianFeature
    """

    def __init__(self, com):
        super().__init__(com)
        self.median_feature = com

    def modifier(self) -> str:
        return self.median_feature.Modifier()

    def __repr__(self):
        return f'MedianFeature(name="{self.name}")'
