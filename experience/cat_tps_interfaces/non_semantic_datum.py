from experience.system import AnyObject

class NonSemanticDatum(AnyObject):
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

    def label(self, value: str = None) -> str:
        if value is not None:
            self.non_semantic_datum.Label = value
            return self
        return self.non_semantic_datum.Label

    def __repr__(self):
        return f'NonSemanticDatum(name="{self.name()}")'
