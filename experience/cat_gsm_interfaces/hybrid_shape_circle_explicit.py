
from experience.cat_gsm_interfaces import HybridShapeCircle

class HybridShapeCircleExplicit(HybridShapeCircle):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircleExplicit
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_circle_explicit = com

    def __repr__(self):
        return f'HybridShapeCircleExplicit(name="{self.name}")'