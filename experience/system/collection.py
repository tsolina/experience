from typing import Iterator, TYPE_CHECKING, Type, TypeVar, Union, Optional, overload
T = TypeVar('T', bound="Experience")

from experience.base_interfaces.experience import Experience
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.inf_interfaces import Application

class Collection(Experience[T]):
# class Collection():
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 Collection
    """

    def __init__(self, com, child = AnyObject):
        super().__init__()
        self._com = com
        self._child = child

    def application(self) -> 'Application':
        from experience.inf_interfaces.application import Application
        return Application(self._com.Application)

    def count(self) -> int:
        return self._com.Count

    def name(self) -> str:
        return self._com.Name
    
    @overload
    def parent(self, cast_to: Type[T]) -> T: ...
    
    @overload
    def parent(self, cast_to: None = None) -> "AnyObject": ...
    
    def parent(self, value: Optional[Type[T]] = None) -> Union[T, 'AnyObject']:
        if value is not None:
            return value(self._com.Parent)
        return AnyObject(self._com.Parent)

    # def get_item(self, id_name: str, as_type: Optional[Type[T]] = None) -> Union[T, 'Collection']:
    #     if as_type is not None:
    #         return as_type(self._com.GetItem(id_name))
    #     return self._child(self._com.GetItem(id_name))
    def get_item(self:"Collection[T]", id_name:str) -> T:
        return self._child(self._com.GetItem(id_name))

    def get_item_by_index(self, index):
        return self._child(self._com.Item(index))

    def get_item_names(self):
        names = []
        for i in range(self._com.Count):
            name = self._com.Item(i + 1).Name
            names.append(name)

        return names

    def get_item_by_name(self, name):
        for i in range(self._com.Count):
            if self._com.Item(i + 1).Name == name:
                return self._child(self._com.Item(i + 1))

        return None

    def items(self:"Collection[T]"):
        """
        - list comprehension added -
        - com collectoin starts at 1 -
        """
        return [self._child(self._com.Item(i + 1)) for i in range(self._com.Count)]
    
    def __len__(self):
        return self.count

    def __getitem__(self, n: int) -> AnyObject:
        if (n + 1) > self.count():
            raise StopIteration

        return AnyObject(self._com.item(n + 1))

    def __iter__(self) -> Iterator[AnyObject]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def empty(self) -> bool:
        if self.count() == 0:
            return True
        else:
            return False

    # @overload
    # def first(self:"Collection[T]", cast_to: Type[T]) -> T: ...
    
    # @overload
    # def first(self, cast_to: None = None) -> "AnyObject": ...
    
    # def first(self:"Collection[T]", as_type: Optional[Type[T]] = None) -> T:# -> Union[T, 'AnyObject']:
    #     '''
    #     - returns first item of collection -
    #     '''
    #     # if as_type is not None:
    #     #     return self.get_item(1, as_type)
    #     return self.get_item(1, as_type or T)
    def first(self:"Collection[T]") -> T:
        return self.get_item(1, T)

    @overload
    def last(self, cast_to: Type[T]) -> T: ...
    
    @overload
    def last(self, cast_to: None = None) -> "AnyObject": ...

    def last(self,  as_type: Optional[Type[T]] = None) -> Union[T, 'AnyObject']:
        '''
        - returns last item of collection -
        '''
        if as_type is not None:
            return self.get_item(self.count(), as_type)
        return self.get_item(self.count())
    
    def contains(self, name:str) -> bool:
        '''
        returns true if item with specified name exists
        '''
        return any(item.name() == name for item in self.items())
    
    def com_type(self) -> str:
        # vba_function_name = "com_type"
        # vba_code = f"""
        # Public Function {vba_function_name}(obj As AnyObject) as String
        #     {vba_function_name} = typename(obj)
        # End Function
        # """
        # return self.application().system_service().evaluate(vba_code, 1, vba_function_name, [self._com])
        return self._com._oleobj_.GetTypeInfo(0).GetDocumentation(-1)[0]

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
    

from typing import Iterator, TypeVar, Type, Optional, Union

T = TypeVar('T', bound="Experience")  # Generic type for items in collection

class Collection(Experience):
    """
    A collection class for items of type T.
    """
    
    def __init__(self, com, child = AnyObject):
        super().__init__()
        self._com = com
        self._child = child

    def _infer_type(self, obj) -> T:
        return type(self).__orig_bases__[0].__args__[0](obj)

    def application(self) -> 'Application':
        from experience.inf_interfaces.application import Application
        return Application(self._com.Application)

    def count(self) -> int:
        return self._com.Count

    def name(self) -> str:
        return self._com.Name

    def get_item(self, id_name: str) -> T:
        return self._child(self._com.GetItem(id_name))

    def get_item_by_index(self, index) -> T:
        return self._child(self._com.Item(index))
    def get_item_by_index(self, index: int) -> T:
        return self._infer_type(self._com.Item(index))


    def get_item_names(self) -> list:
        return [self._com.Item(i + 1).Name for i in range(self.count())]

    def items(self) -> list:
        return [self._child(self._com.Item(i + 1)) for i in range(self.count())]

    def __len__(self) -> int:
        return self.count()

    def __getitem__(self, n: int) -> T:
        if (n + 1) > self.count():
            raise StopIteration
        return self.get_item(n + 1)

    def __iter__(self) -> Iterator[T]:
        for i in range(self.count()):
            yield self._child(self._com.Item(i + 1))

    def empty(self) -> bool:
        return self.count() == 0

    def first(self) -> T:
        return self.get_item(1)

    def last(self) -> T:
        return self.get_item(self.count())

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name="{self.name()}")'
