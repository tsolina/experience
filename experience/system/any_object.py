from typing import TYPE_CHECKING, Type, TypeVar, Union, Optional
from experience.base_interfaces.experience import Experience

if TYPE_CHECKING:
    from experience.inf_interfaces import Application

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

    def name(self, value: str = None) -> Union['Application', str]:
        if value is not None:
            self._com.Name = value
            return self
        return self._com.Name

    # def parent(self) -> 'AnyObject':
    #     return AnyObject(self._com.Parent)

    def parent(self, value: Optional[Type[U]] = None) -> U:
        if value is not None:
            return value(self._com.Parent)
        return AnyObject(self._com.Parent)

    def get_item(self, id_name: str) -> 'AnyObject':
        return AnyObject(self._com.GetItem(id_name))

    def com_type(self) -> str:
        vba_function_name = "com_type"
        vba_code = f"""
        Public Function {vba_function_name}(obj As AnyObject) as String
            {vba_function_name} = typename(obj)
        End Function
        """
        return self.application().system_service().evaluate(vba_code, 1, vba_function_name, [self._com])

    def _vba_cast(self, com_object, vba_class_name):
        vba_function_name = 'generalizedCastToVBA'
        vba_code = f"""
        Public Function generalizedCastToVBA(obj as AnyObject) as {vba_class_name}
            set generalizedCastToVBA = obj
            MsgBox(typename(generalizedCastToVBA))
        End Function
        """
        print(vba_code)
        return self.application().system_service().evaluate(vba_code, 1, vba_function_name, [com_object])

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
        return target_class(self._com.Application.SystemService.Evaluate(vba_code, 1, vba_function_name, [self._com]))

    def _get_safe_array(self, com_obj: 'AnyObject', method: str, tuple_length: int, i_pos: float or int = None) -> tuple:
        """
            _get_safe_array(self._com, "Method", 2)
            _get_safe_array(self._com, "Method", 2, .5)
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
        return self.application().system_service().evaluate(vba_code, 1, vba_function_name, [com_obj])

    def _get_multi(self, params, ins, outs) -> tuple:
        ### _get_multi((shape, 1),("HybridShapeLoft", "GetSectionFromLoft", "Integer"),("Reference", "Long", "Reference")) ###
        com_type = ins[0]
        method = ins[1]
        str_ins = ins[2:]
        dim_in = ", ".join([f"in{i} As {value}" for i, value in enumerate(str_ins)])
        dim_out = ", ".join([f"out{i} As {value}" for i, value in enumerate(outs)])
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
        #print(vba_code)
        return self.application().system_service().evaluate(vba_code, 1, vba_function_name, params)

    def __repr__(self):
        return f'AnyObject(name="{self.name}")'
