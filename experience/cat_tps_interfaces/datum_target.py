from experience.system import AnyObject
from experience.cat_tps_interfaces import UserSurface


class DatumTarget(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DatumTarget
    """

    def __init__(self, com):
        super().__init__(com)
        self.datum_target = com


    def datum(self) -> AnyObject:
        return AnyObject(self.datum_target.Datum)

    def label(self) -> str:
        return self.datum_target.Label

    def get_area_form(self, o_area_form: str) -> tuple: #, o_area_form: str
        return self.datum_target.GetAreaForm(o_area_form)

    def get_circular_area_size(self, o_area_size: float) -> tuple: #, o_area_size: float
        return self.datum_target.GetCircularAreaSize(o_area_size)

    def get_movable_direction_ttrs(self, op_direction_ttrs: UserSurface) -> tuple: #, op_direction_ttrs: UserSurface - op_direction_ttrs.com_object
        return self.datum_target.GetMovableDirectionTTRS(op_direction_ttrs._com)

    def get_rectangular_area_size(self, o_length: float, o_width: float) -> tuple: #, o_length: float, o_width: float
        return self.datum_target.GetRectangularAreaSize(o_length, o_width)

    def set_area_form(self, i_area_form: str) -> 'DatumTarget':
        self.datum_target.SetAreaForm(i_area_form)
        return self

    def set_circular_area_size(self, i_area_size: float) -> 'DatumTarget':
        self.datum_target.SetCircularAreaSize(i_area_size)
        return self

    def set_movable_direction_ttrs(self, ip_direction_ttrs: UserSurface) -> 'DatumTarget':
        self.datum_target.SetMovableDirectionTTRS(ip_direction_ttrs._com)
        return self

    def set_rectangular_area_size(self, i_length: float, i_width: float) -> 'DatumTarget':
        self.datum_target.SetRectangularAreaSize(i_length, i_width)
        return self

    def __repr__(self):
        return f'DatumTarget(name="{self.name()}")'
