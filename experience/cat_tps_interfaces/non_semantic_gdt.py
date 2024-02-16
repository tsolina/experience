from experience.system import AnyObject
from experience.cat_tps_interfaces import TPSParallelOnScreen
from experience.cat_annotation_interfaces import DrawingGDT

class NonSemanticGDT(AnyObject):
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
        self.non_semantic_gdt = com


    def get_2d_annot(self, value: str = None) -> DrawingGDT:
        return DrawingGDT(self.non_semantic_gdt.Get2dAnnot())


    def tps_parallel_on_screen(self, value: str = None) -> TPSParallelOnScreen:
        return self.non_semantic_gdt.TPSParallelOnScreen()

    def __repr__(self):
        return f'NonSemanticGDT(name="{self.name()}")'
