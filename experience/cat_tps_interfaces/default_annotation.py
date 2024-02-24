from experience.system import AnyObject

class DefaultAnnotation(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DefaultAnnotation
    """

    def __init__(self, com):
        super().__init__(com)
        self.default_annotation = com

    def link_wi_geom_type(self) -> str:
        return self.default_annotation.LinkWiGeomType

    def search_algo_type(self) -> str:
        return self.default_annotation.SearchAlgoType

    def is_in_automatic_search_mode(self) -> bool:
        return self.default_annotation.IsInAutomaticSearchMode()