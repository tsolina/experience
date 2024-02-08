from experience.system import AnyObject

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
        return DrawingCoordDim(self.coord_dim.Get2dAnnot())

    def __repr__(self):
        return f'CoordDim(name="{self.name}")'
