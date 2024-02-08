from typing import TYPE_CHECKING

from experience.system import AnyObject
from experience.types import cat_variant

if TYPE_CHECKING:
    from experience.cat_tps_interfaces import Annotations
    from experience.cat_tps_interfaces import UserSurface


class ReferenceFrame(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ReferenceFrame
    """

    def __init__(self, com):
        super().__init__(com)
        self.reference_frame = com


    def all_datums_simple(self) -> 'Annotations':
        from experience.cat_tps_interfaces import Annotations
        return Annotations(self.reference_frame.AllDatumsSimple)

    def frame(self, o_first_box: str, o_second_box: str, o_third_box: str) -> tuple: #, o_first_box: str, o_second_box: str, o_third_box: str
        return self.reference_frame.Frame(o_first_box, o_second_box, o_third_box)

    def get_axis_system_ttrs(self, op_axis_system_ttrs: 'UserSurface') -> tuple: #, op_axis_system_ttrs: UserSurface
        return self.reference_frame.GetAxisSystemTTRS(op_axis_system_ttrs._com)

    def get_degrees_of_freedom(self, in_box: cat_variant, o_value: str) -> tuple: #, o_value: str
        return self.reference_frame.GetDegreesOfFreedom(in_box, o_value)

    def set_axis_system_ttrs(self, ip_axis_system_ttrs: 'UserSurface') -> 'ReferenceFrame':
        self.reference_frame.SetAxisSystemTTRS(ip_axis_system_ttrs._com)
        return self

    def set_degrees_of_freedom(self, in_box: cat_variant, i_value: str) -> 'ReferenceFrame':
        self.reference_frame.SetDegreesOfFreedom(in_box, i_value)
        return self

    def set_frame(self, i_first_box: str, i_second_box: str, i_third_box: str) -> 'ReferenceFrame':
        self.reference_frame.SetFrame(i_first_box, i_second_box, i_third_box)
        return self

    def __repr__(self):
        return f'ReferenceFrame(name="{self.name}")'
