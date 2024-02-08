from experience.mecmod_interfaces import HybridShape

class HybridShapeSurfaceExplicit(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeSurfaceExplicit
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_surface_explicit = com

    def __repr__(self):
        return f'HybridShapeSurfaceExplicit(name="{self.name}")'