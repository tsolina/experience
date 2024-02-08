from experience.system import AnyObject

class ControledRadius(AnyObject):
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
        self.controled_radius = com

    def modifier(self) -> str:
        return self.controled_radius.Modifier

    def __repr__(self):
        return f'ControlledRadius(name="{self.name}")'
