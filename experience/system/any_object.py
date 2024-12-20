import re
from typing import TYPE_CHECKING, Type, TypeVar, Union, Optional, overload
from experience.base_interfaces.experience import Experience
from experience.system.system_types import CATScriptLanguage

if TYPE_CHECKING:    
    from experience.inf_interfaces import Application
    from experience.cat_gsm_interfaces.hybrid_shape_factory import HybridShapeFactory
    from experience.mecmod_interfaces.part import Part
    from experience.product_structure_client_interfaces.vpm_reference import VPMReference

T = TypeVar('T')
U = TypeVar('U')

class AnyObject(Experience):
    """docstring for AnyObject."""

    def __init__(self, com):
        super().__init__()
        self._com = com

    def application(self) -> 'Application':
        from experience.inf_interfaces.application import Application
        return  Application(self._com.Application)

    @overload
    def name(self, value:str) -> 'Application': ...

    @overload
    def name(self, value:None=None) -> str: ...

    def name(self, value: str = None) -> Union['Application', str]:
        if value is not None:
            self._com.Name = value
            return self
        return self._com.Name
    
    # def parent(self, value: Optional[Type[U]] = None) -> Union[U, 'AnyObject']:        
    #     if value is not None:
    #         return value(self._com.Parent)
    #     return AnyObject(self._com.Parent)
    
    @overload
    def parent(self, cast_to: Type[T]) -> T: ...
    
    @overload
    def parent(self, cast_to: None = None) -> "AnyObject": ...

    def parent(self, value: Optional[Type[T]] = None) -> Union[T, 'AnyObject']:
        """
        Returns the parent object of the current COM object.
        If `value` is provided, casts the parent to the specified type.
        If `value` is not provided, dynamically infers the type from COM metadata.
        """
        parent_com = self._com.Parent

        if value is not None:
            # Return the parent cast to the explicitly specified type
            return value(parent_com)

        # Dynamically infer the type name
        inferred_type_name = parent_com._oleobj_.GetTypeInfo(0).GetDocumentation(-1)[0]

        # Map the inferred type name to a Python class (type registry)
        inferred_type = globals().get(inferred_type_name, AnyObject)  # Replace `globals()` with your type registry
        return inferred_type(parent_com)
    

    # def get_item(self, id_name: str, as_type: Optional[Type[T]] = None) -> Union[T, 'AnyObject']:
    #     if as_type is not None:
    #         return as_type(self._com.GetItem(id_name))
    #     return AnyObject(self._com.GetItem(id_name))

    @overload
    def get_item(self, id_name:str, cast_to:Type[T]) -> T: ...
    
    @overload
    def get_item(self, id_name:str, cast_to: None = None) -> "AnyObject": ...
    
    def get_item(self, id_name: str, as_type: Optional[Type[T]] = None) -> Union[T, 'AnyObject']:
        com_item = self._com.GetItem(id_name)
        if as_type is not None:
            return as_type(com_item)
        
        inferred_type_name = com_item._oleobj_.GetTypeInfo(0).GetDocumentation(-1)[0]
        inferred_type = globals().get(inferred_type_name, AnyObject)
        return inferred_type(com_item)


    # def com_type(self) -> str:
    #     vba_function_name = "com_type"
    #     vba_code = f"""
    #     Public Function {vba_function_name}(obj As AnyObject) as String
    #         {vba_function_name} = typename(obj)
    #     End Function
    #     """
    #     # print(__name__, "com_type", self.name())
    #     return self.application().system_service().evaluate(vba_code, CATScriptLanguage.CATVBALanguage, vba_function_name, [self._com])
    
    def com_type(self) -> str:
        return self._com._oleobj_.GetTypeInfo(0).GetDocumentation(-1)[0]

    def _vba_cast(self, com_object, vba_class_name):
        vba_function_name = 'generalizedCastToVBA'
        vba_code = f"""
        Public Function generalizedCastToVBA(obj as AnyObject) as {vba_class_name}
            set generalizedCastToVBA = obj
        End Function
        """
        return self.application().system_service().evaluate(vba_code, CATScriptLanguage.CATVBALanguage, vba_function_name, [com_object])

    def as_pyclass(self, target_class: Type[T], vba_class_name: str = None) -> T:
        if vba_class_name is None:
            vba_class_name = target_class.__name__

        vba_function_name = 'generalizedCastToVBA'
        vba_code = f"""
        Public Function generalizedCastToVBA(obj as AnyObject) as {vba_class_name}
            set generalizedCastToVBA = obj
        End Function
        """

        # TODO: at least verify that target_class is instance of AnyObject
        #return target_class(self._com.Application.SystemService.Evaluate(vba_code, CATScriptLanguage.CATVBScriptLanguage, vba_function_name, [self._com]))
        return target_class(self.application().system_service().evaluate(vba_code, CATScriptLanguage.CATVBALanguage, vba_function_name, [self._com]))

    def _get_safe_array(self, com_obj: 'AnyObject', method: str, tuple_length: int, i_pos: Union[float, int, bool, str] = None) -> tuple:
        """
            _get_safe_array(self._com, "Method", 2)
            _get_safe_array(self._com, "Method", 2, .5)
            _get_safe_array(self._com, "Method", 2, True)
        """
        if i_pos is not None:
            i_pos = str(i_pos) + ", "
        else:
            i_pos = ""
        vba_function_name = 'get_safe_array'
        vba_code = f"""
        Public Function {vba_function_name}({com_obj.__class__.__name__})
            Dim arr({tuple_length})
            {com_obj.__class__.__name__}.{method} {i_pos}arr
            {vba_function_name} = arr
        End Function
        """
        #print(vba_code)
        return self.application().system_service().evaluate(vba_code, CATScriptLanguage.CATVBScriptLanguage, vba_function_name, [com_obj])
    
    def _get_safe_array_multi(self, com_obj: 'AnyObject', method: str, lengths: tuple, i_pos: any = None) -> tuple:
        if isinstance(lengths, int):
            return self._get_safe_array(com_obj, method, lengths, i_pos)

        if i_pos is not None:
            i_pos = str(i_pos) + ", "
        else:
            i_pos = ""       

        # if isinstance(lengths, int):
        #     dim_out = f"out({lengths})"
        #     args_out = f"out"
        # else:
        dim_out = ", ".join([f"out{i}({value})" for i, value in enumerate(lengths)])
        args_out = ", ".join([f"out{i}" for i, _ in enumerate(lengths)])

        vba_function_name = 'get_safe_array'
        vba_code = f"""
        Public Function {vba_function_name}({com_obj.__class__.__name__})
            Dim {dim_out}
            {com_obj.__class__.__name__}.{method} {i_pos}{args_out}
            {vba_function_name} = Array({args_out})
        End Function
        """   
        return self.application().system_service().evaluate(vba_code, CATScriptLanguage.CATVBScriptLanguage, vba_function_name, [com_obj])
    
    def _replace_args(self, i_string: str) -> str:
        pattern = r'\b(\w+)\b\s+As\s+\((\d*)\)\s*(\w*)'

        def replace_match(match):
            name = match.group(1)
            index = match.group(2) if match.group(2) else ""
            type_str = match.group(3)
            return f"{name}({index}) As {type_str}" if type_str else f"{name}({index})"
        
        return re.sub(pattern, replace_match, i_string)

    def _get_multi(self, params, ins, outs) -> tuple:
        """
        _get_multi([shape, 1],("HybridShapeLoft", "GetSectionFromLoft", "Integer"),("Reference", "Long", "Reference"))
        """ 
        
        com_type = ins[0]
        method = ins[1]
        str_ins = ins[2:]
        # dim_in = ", ".join([f"in{i} As {value}" for i, value in enumerate(str_ins)]).replace(" As ()", "() As ")
        # dim_out = ", ".join([f"out{i} As {value}" for i, value in enumerate(outs)]).replace(" As ()", "() As ")
        dim_in = self._replace_args(", ".join([f"in{i} As {value}" for i, value in enumerate(str_ins)]))
        dim_out = self._replace_args(", ".join([f"out{i} As {value}" for i, value in enumerate(outs)]))
        args_in = ", ".join([f"in{i}" for i, _ in enumerate(str_ins)])
        args_out = ", ".join([f"out{i}" for i, _ in enumerate(outs)])
        if len(str_ins) == 0:
            args = args_out
            dim_in = ""
        else:
            args = ", ".join((args_in, args_out))
            dim_in = ", " + dim_in
        vba_function_name = "func"
        vba_code = f"""
            Public Function {vba_function_name}(obj As {com_type}{dim_in}) As Variant
                Dim {dim_out}
                obj.{method} {args}
                {vba_function_name} = Array({args_out})
            End Function
        """
        # print(vba_code)
        # print(dir(self))
        return self.application().system_service().evaluate(vba_code, CATScriptLanguage.CATVBScriptLanguage, vba_function_name, params)
    
    def _get_multi_with_result(self, params, ins, outs, rval) -> tuple:
        """
        _get_multi([shape, 1],("HybridShapeLoft", "GetSectionFromLoft", "Integer"),("Reference", "Long", "Reference"), "Long")
        """ 
        
        com_type = ins[0]
        method = ins[1]
        str_ins = ins[2:]
        # dim_in = ", ".join([f"in{i} As {value}" for i, value in enumerate(str_ins)]).replace(" As ()", "() As ")
        # dim_out = ", ".join([f"out{i} As {value}" for i, value in enumerate(outs)]).replace(" As ()", "() As ")
        dim_in = self._replace_args(", ".join([f"in{i} As {value}" for i, value in enumerate(str_ins)]))
        dim_out = self._replace_args(", ".join([f"out{i} As {value}" for i, value in enumerate(outs)]))
        args_in = ", ".join([f"in{i}" for i, _ in enumerate(str_ins)])
        args_out = ", ".join([f"out{i}" for i, _ in enumerate(outs)])
        if len(str_ins) == 0:
            args = args_out
            dim_in = ""
        else:
            args = ", ".join((args_in, args_out))
            dim_in = ", " + dim_in
        vba_function_name = "func"
        vba_code = f"""
            Public Function {vba_function_name}(obj As {com_type}{dim_in}) As Variant
                Dim {dim_out}, {rval}
                {rval} = obj.{method}({args})
                {vba_function_name} = Array({rval}, {args_out})
            End Function
        """
        #print(vba_code)
        # print(dir(self))
        return self.application().system_service().evaluate(vba_code, CATScriptLanguage.CATVBScriptLanguage, vba_function_name, params)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'