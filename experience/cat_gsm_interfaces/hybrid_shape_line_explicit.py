from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Line

class HybridShapeLineExplicit(Line):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Line
                |                             HybridShapeLineExplicit
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_line_explicit = com

    def __repr__(self):
        return f'HybridShapeLineExplicit(name="{self.name}")'