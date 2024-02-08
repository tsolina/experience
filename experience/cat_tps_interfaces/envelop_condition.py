from experience.system import AnyObject


class EnvelopCondition(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     EnvelopCondition
    """

    def __init__(self, com):
        super().__init__(com)
        self.envelope_condition = com

    def modifier(self) -> str:
        return self.envelope_condition.Modifier

    def __repr__(self):
        return f'EnvelopCondition(name="{self.name}")'
