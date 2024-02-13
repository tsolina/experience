from typing import Union, TYPE_CHECKING
from experience.system import AnyObject#, CATBaseDispatch

if TYPE_CHECKING:
    from experience.cat_annotation_interfaces import DrawingLeaders, DrawingTextProperties

class DrawingText(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingText
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_text = com

    def anchor_position(self, value: int = None) -> Union['DrawingText', int]:
        if value is not None:
            self.drawing_text.AnchorPosition = value
            return self
        return self.drawing_text.AnchorPosition

    def angle(self, value: float = None) -> Union['DrawingText', float]:
        if value is not None:
            self.drawing_text.Angle = value
            return self
        return self.drawing_text.Angle

    def associative_element(self, value:AnyObject = None) -> Union['DrawingText', AnyObject]:
        if value is not None:
            self.drawing_text.AssociativeElement = value._com
            return self
        return AnyObject(self.drawing_text.AssociativeElement)

    def frame_type(self, value: int = None) -> Union['DrawingText', int]:
        if value is not None:
            self.drawing_text.FrameType = value
            return self
        return self.drawing_text.FrameType

    def leaders(self) -> 'DrawingLeaders':
        from experience.cat_annotation_interfaces import DrawingLeaders
        return DrawingLeaders(self.drawing_text.Leaders)

    def lock_edition(self, value: bool = None) -> Union['DrawingText', bool]:
        if value is not None:
            self.drawing_text.LockEdition = value
            return self
        return self.drawing_text.FrameType

    def nb_link(self) -> int:
        return self.drawing_text.NbLink

    def orientation_reference(self, value: int = None) -> Union['DrawingText', int]:
        if value is not None:
            self.drawing_text.OrientationReference = value
            return self
        return self.drawing_text.OrientationReference

    def text(self, value: str = None) -> Union['DrawingText', str]:
        if value is not None:
            self.drawing_text.Text = value
            return self
        return self.drawing_text.Text

    def text_properties(self) -> 'DrawingTextProperties':
        from experience.cat_annotation_interfaces import DrawingTextProperties
        return DrawingTextProperties(self.drawing_text.TextProperties)

    def wrapping_width(self, value: float = None) -> Union['DrawingText', float]:
        if value is not None:
            self.drawing_text.WrappingWidth = value
            return self
        return self.drawing_text.WrappingWidth

    def x(self, value: float = None) -> Union['DrawingText', float]:
        if value is not None:
            self.drawing_text.x = value
            return self
        return self.drawing_text.x

    def y(self, value: float = None) -> Union['DrawingText', float]:
        if value is not None:
            self.drawing_text.y = value
            return self
        return self.drawing_text.y

    def activate_frame(self, itype: int) -> 'DrawingText':
        self.drawing_text.ActivateFrame(itype)
        return self

    def get_font_name(self, i_first, inb_character) -> str:
        return self.drawing_text.GetFontName(i_first, inb_character)

    def get_font_size(self, i_first: int, inb_character: int) -> float:
        return self.drawing_text.GetFontSize(i_first, inb_character)

    def get_modifiable_in_2d_component_instances(self) -> bool:
        return self.drawing_text.GetModifiableIn2DComponentInstances()

    def get_parameter_link(self, i_index: int) -> AnyObject:
        return self.drawing_text.GetParameterLink(i_index)

    def get_parameter_on_sub_string(self, i_param: int, i_first: int, inb_character: int) -> int:
        return self.drawing_text.GetParameterOnSubString(i_param, i_first, inb_character)

    def insert_attribute_link(self, i_first: int, inb_character: int, i_owner_att: AnyObject, i_type_internal_name: str, i_att_internal_name: str) -> 'DrawingText':
        self.drawing_text.InserAttributeLink(i_first, inb_character, i_owner_att, i_type_internal_name, i_att_internal_name)
        return self

    def insert_variable(self, i_first: int, inb_character: int, ibase: AnyObject) -> None:
        self.drawing_text.InsertVariable(i_first, inb_character, ibase.com_object)
        return self

    def set_font_name(self, i_first: int, inb_character: int, i_font_name: str) -> 'DrawingText':
        self.drawing_text.SetFontName(i_first, inb_character, i_font_name)
        return self

    def set_font_size(self, i_first: int, inb_character: int, i_font_size: float) -> 'DrawingText':
        self.drawing_text.SetFontSize(i_first, inb_character, i_font_size)
        return self

    def set_modifiable_in_2d_component_instances(self) -> 'DrawingText':
        self.drawing_text.SetModifiableIn2DComponentInstances()
        return self

    def set_parameter_on_sub_string(self, i_param: int, i_first: int, inb_character: int, i_val: int) -> 'DrawingText':
        self.drawing_text.SetParameterOnSubString(i_param, i_first, inb_character, i_val)
        return self

    def solve_link(self, ip_obj: AnyObject) -> 'DrawingText':
        self.drawing_text.SolveLink(ip_obj)
        return self

    def __repr__(self):
        return f'DrawingText(name="{self.name()}")'
