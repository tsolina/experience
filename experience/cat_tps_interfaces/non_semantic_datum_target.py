from experience.system import AnyObject

class NonSemanticDatumTarget(AnyObject):
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

    def low_label(self, value: str = None) -> str:
        if value is not None:
            self.non_semantic_datum.LowLabel = value
            return self
        return self.non_semantic_datum.LowLabel

    def type_specifier(self, value: str = None) -> str:
        if value is not None:
            self.non_semantic_datum.TypeSpecifier = value
            return self
        return self.non_semantic_datum.TypeSpecifier

    def up_label(self, value: str = None) -> str:
        if value is not None:
            self.non_semantic_datum.UpLabel = value
            return self
        return self.non_semantic_datum.UpLabel