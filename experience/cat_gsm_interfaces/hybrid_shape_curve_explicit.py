from experience.mecmod_interfaces import HybridShape

class HybridShapeCurveExplicit(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeCurveExplicit
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_curve_explicit = com

    def __repr__(self):
        return f'HybridShapeCurveExplicit(name="{self.name}")'