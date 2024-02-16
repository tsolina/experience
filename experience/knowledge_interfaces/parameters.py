from typing import Iterator, TYPE_CHECKING, Optional

from pywintypes import com_error

from experience.exceptions import CATIAApplicationException
from experience.knowledge_interfaces import Parameter
from experience.system import AnyObject, Collection

if TYPE_CHECKING:
    from experience.knowledge_interfaces import ParameterSet
    from experience.knowledge_interfaces import BoolParam, Dimension, IntParam, ListParameter, RealParam, StrParam, Units
    from experience.types import cat_variant, any_parameter

class Parameters(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Parameters
    """

    def __init__(self, com):
        super().__init__(com, child=Parameter)
        self.parameters = com

    def root_parameter_set(self) -> 'ParameterSet':
        from experience.knowledge_interfaces import ParameterSet
        return ParameterSet(self.parameters.RootParameterSet)

    def units(self) -> 'Units':
        from experience.knowledge_interfaces import Units
        return Units(self.parameters.Units)

    def all_parameters(self):
        from experience.knowledge_interfaces import Parameter
        parameters = []

        if self.has_parameters():
            for i in range(self.parameters.Count):
                para = Parameter(self.parameters.Item(i + 1))
                parameters.append(para)

        return parameters

    def create_boolean(self, i_name: str, i_value: bool) -> 'BoolParam':
        from experience.knowledge_interfaces import BoolParam
        return BoolParam(self.parameters.CreateBoolean(i_name, i_value))

    def create_dimension(self, i_name: str, i_magnitude: str, i_value: float) -> 'Dimension':
        from experience.knowledge_interfaces import Dimension
        return Dimension(self.parameters.CreateDimension(i_name, i_magnitude, i_value))

    def create_integer(self, i_name: str, i_value: int) -> 'IntParam':
        from experience.knowledge_interfaces import IntParam
        return IntParam(self.parameters.CreateInteger(i_name, i_value))

    def create_list(self, i_name: str) -> 'ListParameter':
        from experience.knowledge_interfaces import ListParameter
        return ListParameter(self.parameters.CreateList(i_name))

    def create_real(self, i_name: str, i_value: float) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.parameters.CreateReal(i_name, i_value))

    def create_set_of_parameters(self, i_father: AnyObject) -> 'Parameters':
        return self.parameters.CreateSetOfParameters(i_father._com)

    def create_string(self, i_name: str, i_value: str) -> 'StrParam':
        from experience.knowledge_interfaces import StrParam
        return StrParam(self.parameters.CreateString(i_name, i_value))

    def get_name_to_use_in_relation(self, i_object: AnyObject) -> str:
        return self.parameters.GetNameToUseInRelation(i_object._com)

    def has_parameters(self) -> bool:
        if self.parameters.Count > 0:
            return True

        return False

    def is_parameter(self, index: 'cat_variant') -> bool:
        from experience.types import cat_variant
        try:
            if self.parameters.Item(index):
                return True
        except com_error:
            return False

    def is_list_parameter(self, index: 'cat_variant') -> bool:
        from experience.types import cat_variant
        try:
            if self.parameters.Item(index).ValueList:
                return True
        except AttributeError:
            return False

    def item(self, index: 'cat_variant') -> 'any_parameter':
        from experience.knowledge_interfaces import BoolParam, IntParam, StrParam, RealParam
        from experience.types import cat_variant, any_parameter
        p: any_parameter

        if not self.is_parameter(index):
            raise CATIAApplicationException(f'Could not find parameter name "{index}".')

        if not self.is_list_parameter(index):

            if isinstance(self.parameters.Item(index).value, bool):
                p = BoolParam(self.parameters.Item(index))

            elif isinstance(self.parameters.Item(index).value, int):
                p = IntParam(self.parameters.Item(index))

            elif isinstance(self.parameters.Item(index).value, str):
                p = StrParam(self.parameters.Item(index))

            elif isinstance(self.parameters.Item(index).value, float):
                p = RealParam(self.parameters.Item(index))

            else:
                raise CATIAApplicationException(f'Could not assign parameter name "{index}".')

        else:
            p = ListParameter(self.parameters.Item(index))

        return p

    def remove(self, i_index: 'cat_variant') -> 'Parameters':
        from experience.types import cat_variant
        self.parameters.Remove(i_index)
        return self

    def sub_list(self, i_object: AnyObject, i_recursively: bool) -> 'Parameters':
        return Parameters(self.parameters.SubList(i_object._com, i_recursively))

    def __getitem__(self, n: int) -> Parameter:
        if (n + 1) > self.count:
            raise StopIteration

        return Parameter(self.parameters.item(n + 1))

    def __iter__(self) -> Iterator[Parameter]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'Parameters(name="{self.name()}")'
