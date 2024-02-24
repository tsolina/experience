from experience.system import AnyObject
from experience.cat_tps_interfaces import TPSParallelOnScreen
from experience.cat_annotation_interfaces import DrawingWelding

class Weld(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Weld
    """

    def __init__(self, com):
        super().__init__(com)
        self.weld = com


    def get_2d_annot(self) -> DrawingWelding:
        return DrawingWelding(self.weld.DrawingWelding())


    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        return TPSParallelOnScreen(self.weld.TPSParallelOnScreen())