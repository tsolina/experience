from typing import Union
from experience.system import AnyObject
from experience.drafting_interfaces.drafting_types import *

class DrawingThread(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingThread
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_thread = com

    def type(self, value: CatThreadType = None) -> Union['DrawingThread', CatThreadType]:
        if value is not None:
            self.drawing_thread.Type = int(value)
            return self
        return CatThreadType.item(self.drawing_thread.Type)

    def is_linked_to(self) -> CatThreadLinkedTo:
        return CatThreadLinkedTo.item(self.drawing_thread.IsLinkedTo())

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
