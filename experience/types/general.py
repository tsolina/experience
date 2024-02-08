from typing import TypeVar, Type
from experience.knowledge_interfaces.bool_param import BoolParam
from experience.knowledge_interfaces.int_param import IntParam
from experience.knowledge_interfaces.str_param import StrParam
from experience.knowledge_interfaces.real_param import RealParam

cat_variant = TypeVar('cat_variant', int, str)
list_str = TypeVar('list_str', list, str)
any_parameter = TypeVar('any_parameter', BoolParam, IntParam, StrParam, RealParam)
