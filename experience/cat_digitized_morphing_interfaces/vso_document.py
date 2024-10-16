from experience.system import AnyObject

class VSODocument(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     VSODocument
    """

    def __init__(self, com):
        super().__init__(com)
        self.vso_document = com

    def synchronize(self) -> 'VSODocument':
        self.vso_document.Synchronize()
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'