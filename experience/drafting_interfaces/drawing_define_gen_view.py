from typing import Union, Optional, TYPE_CHECKING

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.drafting_interfaces.drafting_types import *
    from experience.drafting_interfaces import DrawingView, DrawingGenViewProperties
    from experience.types import cat_variant


class DrawingDefineGenView(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingDefineGenView
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_define_gen_view = com

    def define_auxiliary_view(self, i_xpos: float, i_ypos: float, i_x_start_point: float, i_y_start_point: float, i_x_end_point: float, i_y_end_point: float, 
                              i_side_to_draw: int, i_parent_view: 'DrawingView', i_view_style: str, i_compute_update: bool, i_view_prop: 'DrawingGenViewProperties') -> 'DrawingView':
        from experience.drafting_interfaces import DrawingView
        return DrawingView(self.drawing_define_gen_view.DefineAuxiliaryView(i_xpos, i_ypos, i_x_start_point, i_y_start_point, i_x_end_point, i_y_end_point, i_side_to_draw,
                                                        i_parent_view._com, i_view_style, i_compute_update, i_view_prop))

    def define_circular_detail_view(self, i_xpos: float, i_ypos: float, i_x_center: float, i_y_center: float, i_radius: float, i_parent_view: 'DrawingView',
                                    i_view_style: str, i_compute_update: bool, i_view_prop: 'DrawingGenViewProperties') -> 'DrawingView':
        from experience.drafting_interfaces import DrawingView
        return DrawingView(self.drawing_define_gen_view.DefineCircularDetailView(i_xpos, i_ypos, i_x_center, i_y_center, i_radius, i_parent_view._com,
                                                                                 i_view_style, i_compute_update, i_view_prop))
    
    def define_front_view(self, i_xpos: float, i_ypos: float, i_list_of_prd_inst: list, i_plane: list, i_view_style: str, 
                          i_compute_update: bool, i_view_prop: 'DrawingGenViewProperties') -> 'DrawingView':
        from experience.drafting_interfaces import DrawingView
        return DrawingView(self.drawing_define_gen_view.DefineFrontView(i_xpos, i_ypos, i_list_of_prd_inst, i_plane, i_view_style, i_compute_update, i_view_prop))

    def define_isometric_view(self, i_xpos: float, i_ypos: float, i_list_of_prd_inst: list, i_plane: list, i_view_style: str,
                              i_compute_update: bool, i_view_prop: 'DrawingGenViewProperties') -> 'DrawingView':
        from experience.drafting_interfaces import DrawingView
        return DrawingView(self.drawing_define_gen_view.DefineIsometricView(i_xpos, i_ypos, i_list_of_prd_inst, i_plane, i_view_style, i_compute_update, i_view_prop))
    
    def define_polygonal_detail_view(self, i_xpos: float, i_ypos: float, i_profile: list, i_parent_view: 'DrawingView', i_view_style: str,
                                     i_compute_update: bool, i_view_prop: 'DrawingGenViewProperties') -> 'DrawingView':
        from experience.drafting_interfaces import DrawingView
        return DrawingView(self.drawing_define_gen_view.DefinePolygonalDetailView(i_xpos, i_ypos, i_profile, i_parent_view._com, i_view_style, i_compute_update, i_view_prop))

    def define_projection_view(self, i_xpos: float, i_ypos: float, i_parent_view: 'DrawingView', i_type: 'CatProjViewType', i_view_style: str,
                                     i_compute_update: bool, i_view_prop: 'DrawingGenViewProperties') -> 'DrawingView':
        from experience.drafting_interfaces import DrawingView
        return DrawingView(self.drawing_define_gen_view.DefineProjectionView(i_xpos, i_ypos, i_parent_view._com, int(i_type), i_view_style, i_compute_update, i_view_prop))
    
    def define_section_view(self, i_xpos: float, i_ypos: float, i_profile: list, i_section_type: str, i_profile_type: str, i_side_to_draw: int, 
                            i_parent_view: 'DrawingView', i_view_style: str, i_compute_update: bool, i_view_prop: 'DrawingGenViewProperties') -> 'DrawingView':
        from experience.drafting_interfaces import DrawingView
        return DrawingView(self.drawing_define_gen_view.DefineSectionView(i_xpos, i_ypos, i_profile, i_section_type, i_profile_type, i_side_to_draw, i_parent_view._com, 
                                                                          i_view_style, i_compute_update, i_view_prop))    

    def define_standalone_section(self, i_xpos: float, i_ypos: float, i_list_of_prd_ints: list, profil: list, type_of_section: str,
                                  type_of_profile: str, i_plane: list, i_side: int,
                                  i_view_style: str, i_compute_update: bool, i_view_prop: 'DrawingGenViewProperties') -> 'DrawingView':
        from experience.drafting_interfaces import DrawingView
        return DrawingView(self.drawing_define_gen_view.DefineStandAloneSection(i_xpos, i_ypos, i_list_of_prd_ints, profil, type_of_section, type_of_profile, i_plane, i_side, 
                                                                          i_view_style, i_compute_update, i_view_prop))  

    def define_unfolded_view(self, i_xpos: float, i_ypos: float, i_list_of_prd_ints: list, i_plane: list,
                                  i_view_style: str, i_compute_update: bool, i_view_prop: 'DrawingGenViewProperties') -> 'DrawingView':
        from experience.drafting_interfaces import DrawingView
        return DrawingView(self.drawing_define_gen_view.DefineUnfoldedView(i_xpos, i_ypos, i_list_of_prd_ints, i_plane,
                                                                          i_view_style, i_compute_update, i_view_prop))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'