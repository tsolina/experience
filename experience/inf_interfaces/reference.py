from experience.system import AnyObject

class Reference(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Reference
    """
    def __init__(self, com):
        super().__init__(com)
        self.reference = com

    def display_name(self) -> str:
        return self.reference.DisplayName

    def compose_with(self, i_reference: 'Reference') -> 'Reference':
        return Reference(self.reference.ComposeWith(i_reference._com))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'