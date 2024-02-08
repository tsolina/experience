from typing import TYPE_CHECKING

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_tps_interfaces import Annotation, Annotation2


class AssociatedRefFrame(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AssociatedRefFrame
    """

    def __init__(self, com):
        super().__init__(com)
        self.associated_ref_frame = com


    def reference_frame(self) -> 'Annotation':
        from experience.cat_tps_interfaces import Annotation
        return Annotation(self.associated_ref_frame.ReferenceFrame)


    def reference_frame_2(self) -> 'Annotation2':
        from experience.cat_tps_interfaces import Annotation2
        return Annotation2(self.associated_ref_frame.ReferenceFrame2)

    def __repr__(self):
        return f'AssociatedRefFrame(name="{self.name}")'
