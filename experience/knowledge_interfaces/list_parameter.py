from experience.knowledge_interfaces import List, Parameter

class ListParameter(Parameter):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.Parameter
                |                         ListParameter

    """

    def __init__(self, com):
        super().__init__(com)
        self.list_parameter = com

    def value_list(self) -> List:
        return List(self.list_parameter.ValueList)

    def __repr__(self):
        return f'ListParameter(name="{self.name()}")'
