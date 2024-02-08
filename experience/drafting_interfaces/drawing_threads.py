from typing import Iterator

from experience.drafting_interfaces import DrawingThread
from experience.system import CATBaseDispatch, Collection, AnyObject

class DrawingThreads(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingThreads
    """

    def __init__(self, com):
        super().__init__(com, _child=DrawingThread)
        self.drawing_threads = com

    def add(self, i_geom_elem: AnyObject) -> DrawingThread:
        return DrawingThread(self.drawing_threads.Add(i_geom_elem._com))

    def item(self, i_index: int) -> DrawingThread:
        return DrawingThread(self.drawing_threads.Item(i_index))

    def remove(self, i_index: int) -> 'DrawingThreads':
        self.drawing_threads.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> DrawingThread:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingThread(self.drawing_threads.item(n + 1))

    def __iter__(self) -> Iterator[DrawingThread]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'DrawingThreads(name="{self.name}")'
