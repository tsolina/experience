from experience.cat_gsm_interfaces import Point

class HybridShapePointExplicit(Point):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Point
                |                             HybridShapePointExplicit
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_point_explicit = com

    def __repr__(self):
        return f'HybridShapePointExplicit(name="{self.name}")'