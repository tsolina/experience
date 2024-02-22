from typing import TYPE_CHECKING
from experience.knowledge_interfaces import RealParam

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Unit

class Dimension(RealParam):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.Parameter
                |                         KnowledgeInterfaces.RealParam
                |                             Dimension
    """

    def __init__(self, com):
        super().__init__(com)
        self.dimension = com

    def unit(self) -> 'Unit':
        from experience.knowledge_interfaces import Unit
        return Unit(self.dimension.Unit)

    def value_as_string2(self, i_nb_decimals: int, i_show_trailing_zeros: bool) -> str:
        return self.dimension.ValueAsString2(i_nb_decimals, i_show_trailing_zeros)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'