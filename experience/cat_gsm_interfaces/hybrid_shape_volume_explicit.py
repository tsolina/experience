from experience.mecmod_interfaces import HybridShape

class HybridShapeVolumeExplicit(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeVolumeExplicit
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_volume_explicit = com

    def __repr__(self):
        return f'HybridShapeVolumeExplicit(name="{self.name}")'