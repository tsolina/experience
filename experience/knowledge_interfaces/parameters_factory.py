from typing import Union, TYPE_CHECKING

from experience.system import AnyObject
from experience.knowledge_interfaces import KnowledgeFactory

if TYPE_CHECKING:
    from experience.knowledge_interfaces import BoolParam, Dimension, IntParam, List, ParmsSet, RealParam, StrParam

class ParametersFactory(KnowledgeFactory):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeFactory
                |                         ParametersFactory
    """

    def __init__(self, com):
        super().__init__(com)
        self.parameters_factory = com

    def create_boolean(self, i_name: str, i_value: bool) -> 'BoolParam':
        from experience.knowledge_interfaces import BoolParam
        return BoolParam(self.parameters_factory.CreateBoolean(i_name, i_value))

    def create_dimension(self, i_name: str, i_magnitude: str, i_value: float) -> 'Dimension':
        from experience.knowledge_interfaces import Dimension
        return Dimension(self.parameters_factory.CreateDimension(i_name, i_magnitude, i_value))   

    def create_integer(self, i_name: str, i_value: int) -> 'IntParam':
        from experience.knowledge_interfaces import IntParam
        return IntParam(self.parameters_factory.CreateInteger(i_name, i_value))
    
    def create_list(self, i_name: str) -> 'List':
        from experience.knowledge_interfaces import List
        return List(self.parameters_factory.CreateList(i_name))
    
    def create_parameter_set(self, i_name: str) -> 'ParmsSet':
        from experience.knowledge_interfaces import ParmsSet
        return ParmsSet(self.parameters_factory.CreateParametersSet(i_name))

    def create_real(self, i_name: str, i_value: float) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.parameters_factory.CreateReal(i_name, i_value))
    
    def create_string(self, i_name: str, i_value: str) -> 'StrParam':
        from experience.knowledge_interfaces import StrParam
        return StrParam(self.parameters_factory.CreateString(i_name, i_value))
    
    def get_name_to_use_in_relation(self, i_object: AnyObject) -> str:
        return self.parameters_factory.GetNameToUseInRelation(i_object._com)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'