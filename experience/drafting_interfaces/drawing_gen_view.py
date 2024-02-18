from typing import TYPE_CHECKING, Union, Optional, Type, TypeVar
T = TypeVar('T')

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.drafting_interfaces import DrawingGenViewProperties, DrawingView

class DrawingGenView(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingGenView
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_gen_view = com

    def gvs_name(self, value: str = None) -> Union['DrawingGenView', str]:
        if value is not None:
            self.drawing_gen_view.GVSName = value
            return self
        return self.drawing_gen_view.GVSName
    
    def gen_view_properties(self, value: 'DrawingGenViewProperties') -> Union['DrawingGenView', 'DrawingGenViewProperties']:
        if value is not None:
            self.drawing_gen_view.GenViewProperties = value._com
            return self        
        from experience.drafting_interfaces import DrawingGenViewProperties
        return DrawingGenViewProperties(self.drawing_gen_view.GenViewProperties)
    
    def number_of_breakouts(self) -> int:
        return self.drawing_gen_view.NumberOfBreakouts
    
    def number_of_breaks(self) -> int:
        return self.drawing_gen_view.NumberOfBreaks

    def number_of_links(self) -> int:
        return self.drawing_gen_view.NumberOfLinks

    def gen_view_properties(self, value: 'DrawingGenViewProperties') -> 'DrawingView':   
        from experience.drafting_interfaces import DrawingView
        return DrawingView(self.drawing_gen_view.ParentView)
    
    def add_breakout(self, i_profil: list, i_plane1: list, i_plane2: list) -> 'DrawingGenView':
        self.drawing_gen_view.AddBreakout(i_profil, i_plane1, i_plane2)
        return self
    
    def add_broken_view(self, i_broken_lines_extremities: list, ix_direction: float, iy_direction: float) -> 'DrawingGenView':
        self.drawing_gen_view.AddBrokenView(i_broken_lines_extremities, ix_direction, iy_direction)
        return self
    
    def add_clipping_box(self, i_box_definition: list) -> 'DrawingGenView':
        self.drawing_gen_view.AddClippingBox(i_box_definition)
        return self
    
    def add_clipping_with_circle(self, x_center: float, y_center: float, radius: float, compute_mode: bool) -> 'DrawingGenView':
        self.drawing_gen_view.AddClippingWithCircle(x_center, y_center, radius, compute_mode)
        return self
    
    def add_clipping_with_profile(self, profil: list, compute_mode: bool) -> 'DrawingGenView':
        self.drawing_gen_view.AddClippingWithProfile(profil, compute_mode)
        return self
    
    def add_link(self, i_info_on_view_link: list) -> 'DrawingGenView':
        """
        Dim ViewLink1 (2) as CATSafeArrayVariant
        ViewLink1 (0)= myPartBody
        ViewLink1 (1)= myPLMRepInst
        ViewLink1 (2)= myPLMOcc1

        """
        self.drawing_gen_view.AddLink(i_info_on_view_link)
        return self
    
    def apply_breakout_to(self, i_destination_view: 'DrawingGenView') -> 'DrawingGenView':
        self.drawing_gen_view.ApplyBreakoutTo(i_destination_view)
        return self
    
    def apply_clipping_box_to(self, i_destination_view: 'DrawingGenView') -> 'DrawingGenView':
        self.drawing_gen_view.ApplyClippingBoxTo(i_destination_view)
        return self    
    
    def force_update(self) -> 'DrawingGenView':
        self.drawing_gen_view.ForceUpdate()
        return self    
    
    def get_associated_root_product(self, value: Optional[Type[T]] = None) -> T:
        """ - Default: AnyObject
            - Optional: VPMReference - """
        if value is not None:
            return value(self.drawing_gen_view.GetAssociatedRootProduct())
        return AnyObject(self.drawing_gen_view.GetAssociatedRootProduct())
    
    def get_axis_system(self) -> tuple[AnyObject, AnyObject]:
        return self.gen_view_properties.GetAxisSystem()
    
    def get_link(self, i_index_link: int) -> tuple:
        return self._get_safe_array(self.drawing_gen_view, "GetLink", 3, i_index_link)
    
    def get_number_of_info_for_link(self, i_index_link: int) -> int:
        return self.drawing_gen_view.GetNumberOfInfoForLink(i_index_link)
    
    def is_clipped(self) -> bool:
        return self.drawing_gen_view.IsClipped()
    
    def modify_projection_plane(self, i_proj_plane: list) -> 'DrawingGenView':
        self.drawing_gen_view.ModifyProjectionPlane(i_proj_plane)
        return self 
    
    def put_links(self, i_nb_link: int) -> tuple:
        return self._get_safe_array(self.drawing_gen_view, "PutLinks", 3, i_nb_link)
    
    def remove_gvs(self) -> 'DrawingGenView':
        self.drawing_gen_view.RemoveGVS()
        return self 
    
    def remove_link(self) -> 'DrawingGenView':
        self.drawing_gen_view.RemoveLink()
        return self 

    def set_axis_system(self, i_product: AnyObject, i_axis_system: AnyObject) -> 'DrawingGenView':
        self.drawing_gen_view.SetAxisSystem(i_product, i_axis_system)
        return self 
    
    def un_break(self) -> 'DrawingGenView':
        self.drawing_gen_view.UnBreak()
        return self 

    def un_breakout(self) -> 'DrawingGenView':
        self.drawing_gen_view.UnBreakout()
        return self

    def un_clip(self) -> 'DrawingGenView':
        self.drawing_gen_view.UnClip()
        return self
            
    def update(self) -> 'DrawingGenView':
        self.drawing_gen_view.Update()
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'