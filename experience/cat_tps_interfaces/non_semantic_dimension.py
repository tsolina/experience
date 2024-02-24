from experience.system import AnyObject
from experience.cat_annotation_interfaces import DrawingDimension
from experience.cat_tps_interfaces import DimensionLimit

class NonSemanticDimension(AnyObject):
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
        self.non_semantic_datum = com


    def dimension_limit(self) -> DimensionLimit:
        return DimensionLimit(self.non_semantic_datum.DimensionLimit())


    def get_2d_annot(self) -> DrawingDimension:
        return DrawingDimension(self.non_semantic_datum.Get2dAnnot())

    def has_dimension_limit(self) -> bool:
        return self.non_semantic_datum.HasDimensionLimit()