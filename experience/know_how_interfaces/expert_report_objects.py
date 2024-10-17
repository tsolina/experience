from typing import Iterator, TYPE_CHECKING

from .expert_report_object import ExpertReportObject
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class ExpertReportObjects(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ExpertReportObjects
    """

    def __init__(self, com):
        super().__init__(com, child=ExpertReportObject)
        self.expert_report_objects = com

    def count_fail(self) -> int:
        return self.expert_report_objects.CountFail
    
    def count_succeed(self) -> int:
        return self.expert_report_objects.CountSucceed
    
    def fail_item(self, i_index: 'cat_variant') ->ExpertReportObject:
        return ExpertReportObject(self.expert_report_objects.FailItem(i_index))

    def item(self, i_index: 'cat_variant') -> ExpertReportObject:
        return ExpertReportObject(self.expert_report_objects.Item(i_index))
    
    def succeed_item(self, i_index: 'cat_variant') -> ExpertReportObject:
        return ExpertReportObject(self.expert_report_objects.SucceedItem(i_index))

    def __getitem__(self, n: int) -> ExpertReportObject:
        if (n + 1) > self.count():
            raise StopIteration

        return ExpertReportObject(self.expert_report_objects.item(n + 1))

    def __iter__(self) -> Iterator[ExpertReportObject]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
