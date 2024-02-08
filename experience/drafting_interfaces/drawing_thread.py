from experience.system import AnyObject
from experience.types import cat_variant

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

    def type(self, value: int = None) -> int:
        if value is not None:
            self.drawing_thread.Type = value
            return self
        return self.drawing_thread.Type

    def is_linked_to(self) -> int:
        return self.drawing_thread.IsLinkedTo()

    def __repr__(self):
        return f'DrawingThread(name="{self.name}")'
