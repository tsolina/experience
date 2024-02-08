from experience.system import AnyObject

class MaterialCondition(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MaterialCondition
    """

    def __init__(self, com):
        super().__init__(com)
        self.material_condition = com

    def modifier(self) -> str:
        return self.material_condition.Modifier

    def __repr__(self):
        return f'MaterialCondition(name="{ self.name }")'
