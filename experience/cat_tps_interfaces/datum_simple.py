from typing import TYPE_CHECKING

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_tps_interfaces import Annotations


class DatumSimple(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DatumSimple
    """

    def __init__(self, com):
        super().__init__(com)
        self.datum_simple = com

    def label(self, value: str = None) -> str:
        if value is not None:
            self.datum_simple.Label = value
            return self
        return self.datum_simple.Label

    def targets(self) -> 'Annotations':
        from experience.cat_tps_interfaces import Annotations
        return Annotations(self.datum_simple.Targets)