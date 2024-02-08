from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Plane

class HybridShapePlaneExplicit(Plane):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneExplicit
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_plane_explicit = com

    def __repr__(self):
        return f'HybridShapePlaneExplicit(name="{self.name}")'