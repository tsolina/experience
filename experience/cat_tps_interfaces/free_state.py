from experience.system import AnyObject

class FreeState(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FreeState
    """

    def __init__(self, com):
        super().__init__(com)
        self.free_state = com

    def modifier(self) -> str:
        return self.free_state.Modifier