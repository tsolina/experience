from typing import TYPE_CHECKING
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_annotation_interfaces import DrawingCoordDim

class CoordDim(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ControledRadius
    """

    def __init__(self, com):
        super().__init__(com)
        self.coord_dim = com


    def get_2d_annot(self) -> 'DrawingCoordDim':
        from experience.cat_annotation_interfaces import DrawingCoordDim
        return DrawingCoordDim(self.coord_dim.Get2dAnnot())