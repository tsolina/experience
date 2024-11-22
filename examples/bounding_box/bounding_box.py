from typing import TYPE_CHECKING

from experience import *

if TYPE_CHECKING:
    from examples.bounding_box.bounding_box_model import BoundingBoxModel

class BoundingBox():
    def __init__(self, catia_com: Application = None):
        if catia_com == None:
            self.app = experience_application()
        else:
            self.app = catia_com
        self._shape: AnyObject = None
        self._axis: AxisSystem = None 

    def select_shape(self) -> str:
        sel = self.app.active_editor().selection()
        status =sel.select_element(["Shape", "Body", "HybridShape"], "Select body or shape", True)

        if status == "Normal":
            self._shape = sel.item(1).value(AnyObject)
            return self._shape.name()
        else:
            return ""
    
    def select_axis(self) -> str:
        sel = self.app.active_editor().selection()
        status =sel.select_element(["AxisSystem"], "Select axis system", True)

        if status == "Normal":
            self._axis = sel.item(1).value(AxisSystem)
            return self._axis.name()
        else:
            return ""
        
    def execute(self, bbm: 'BoundingBoxModel'):
        part = self.app.active_editor().active_object(Part)
        hsf = part.hybrid_shape_factory()

        result = part.hybrid_bodies().add().name("result").as_pyclass(HybridBody)

        shape_reference = part.create_reference_from_object(self._shape)
        if self._shape.com_type() == Body.__name__ or self._shape.com_type() == Shape.__name__:
            self._shape = hsf.add_new_extract(shape_reference).compute()

        if self._axis is None:
            dir_x = hsf.add_new_direction(part.origin_elements().plane_yz()).compute()
            dir_y = hsf.add_new_direction(part.origin_elements().plane_zx()).compute()
            dir_z = hsf.add_new_direction(part.origin_elements().plane_xy()).compute()

            plane_xy = part.origin_elements().plane_xy()
            plane_zx = part.origin_elements().plane_zx()
            plane_yz = part.origin_elements().plane_yz()
        else:
            coords_x = self._axis.get_x_axis()
            dir_x = hsf.add_new_direction_by_coord(coords_x[0], coords_x[1], coords_x[2]).compute()
            coords_y = self._axis.get_y_axis()
            dir_y = hsf.add_new_direction_by_coord(coords_y[0], coords_y[1], coords_y[2]).compute()
            coords_z = self._axis.get_z_axis()
            dir_z = hsf.add_new_direction_by_coord(coords_z[0], coords_z[1], coords_z[2]).compute()

            plane_xy = hsf.add_new_plane2_lines(dir_x, dir_y)
            plane_zx = hsf.add_new_plane2_lines(dir_x, dir_z)
            plane_yz = hsf.add_new_plane2_lines(dir_y, dir_z)

        ext_x_1 = hsf.add_new_extremum(self._shape, dir_x, 1).direction2(dir_y).direction3(dir_z).compute()
        ext_x_2 = hsf.add_new_extremum(self._shape, dir_x, 0).direction2(dir_y).direction3(dir_z).compute()
        ext_y_1 = hsf.add_new_extremum(self._shape, dir_y, 1).direction2(dir_x).direction3(dir_z).compute()
        ext_y_2 = hsf.add_new_extremum(self._shape, dir_y, 0).direction2(dir_x).direction3(dir_z).compute()
        ext_z_1 = hsf.add_new_extremum(self._shape, dir_z, 1).direction2(dir_x).direction3(dir_y).compute()
        ext_z_2 = hsf.add_new_extremum(self._shape, dir_z, 0).direction2(dir_x).direction3(dir_y).compute()

        trans_px = hsf.add_new_translate(ext_x_1, dir_x, bbm.px_value).compute()
        trans_nx = hsf.add_new_translate(ext_x_2, dir_x, -bbm.nx_value).compute()
        trans_py = hsf.add_new_translate(ext_y_1, dir_y, bbm.py_value).compute()
        trans_ny = hsf.add_new_translate(ext_y_2, dir_y, -bbm.ny_value).compute()
        trans_pz = hsf.add_new_translate(ext_z_1, dir_z, bbm.nz_value).compute()
        trans_nz = hsf.add_new_translate(ext_z_2, dir_z, -bbm.nz_value).compute()

        plane_x1 = hsf.add_new_plane_offset_pt(plane_yz, trans_px).compute()
        plane_x2 = hsf.add_new_plane_offset_pt(plane_yz, trans_nx).compute()
        plane_y1 = hsf.add_new_plane_offset_pt(plane_zx, trans_py).compute()
        plane_y2 = hsf.add_new_plane_offset_pt(plane_zx, trans_ny).compute()
        plane_z1 = hsf.add_new_plane_offset_pt(plane_xy, trans_pz).compute()
        plane_z2 = hsf.add_new_plane_offset_pt(plane_xy, trans_nz).compute()

        intersect1 = hsf.add_new_intersection(plane_x1, plane_y1).compute()
        intersect2 = hsf.add_new_intersection(plane_x2, plane_y1).compute()
        intersect3 = hsf.add_new_intersection(plane_x1, plane_y2).compute()
        intersect4 = hsf.add_new_intersection(plane_x2, plane_y2).compute()    

        intersect5 = hsf.add_new_intersection(plane_z1, plane_y1).compute()
        intersect6 = hsf.add_new_intersection(plane_z2, plane_y1).compute()
        intersect7 = hsf.add_new_intersection(plane_z1, plane_y2).compute()
        intersect8 = hsf.add_new_intersection(plane_z2, plane_y2).compute()

        p1 = hsf.add_new_intersection(intersect1, intersect5).compute()
        p2 = hsf.add_new_intersection(intersect2, intersect5).compute()
        p3 = hsf.add_new_intersection(intersect1, intersect6).compute()
        p4 = hsf.add_new_intersection(intersect2, intersect6).compute()

        p5 = hsf.add_new_intersection(intersect3, intersect7).compute()
        p6 = hsf.add_new_intersection(intersect4, intersect7).compute()
        p7 = hsf.add_new_intersection(intersect3, intersect8).compute()
        p8 = hsf.add_new_intersection(intersect4, intersect8).compute()

        line1 = hsf.add_new_line_pt_pt(p1, p2).compute()
        line2 = hsf.add_new_line_pt_pt(p3, p4).compute()
        line3 = hsf.add_new_line_pt_pt(p5, p6).compute()
        line4 = hsf.add_new_line_pt_pt(p7, p8).compute()

        line5 = hsf.add_new_line_pt_pt(p1, p5).compute()
        line6 = hsf.add_new_line_pt_pt(p2, p6).compute()
        line7 = hsf.add_new_line_pt_pt(p3, p7).compute()
        line8 = hsf.add_new_line_pt_pt(p4, p8).compute()

        face1 = hsf.add_new_blend().set_curve(1,line1).set_curve(2, line2).compute()
        face2 = hsf.add_new_blend().set_curve(1,line3).set_curve(2, line4).compute()
        face3 = hsf.add_new_blend().set_curve(1,line5).set_curve(2, line7).compute()
        face4 = hsf.add_new_blend().set_curve(1,line6).set_curve(2, line8).compute()
        face5 = hsf.add_new_blend().set_curve(1,line1).set_curve(2, line3).compute()
        face6 = hsf.add_new_blend().set_curve(1,line2).set_curve(2, line4).compute()

        bounding_box = hsf.add_new_join(face1, face2).add_element(face3).add_element(face4).add_element(face5).add_element(face6).compute().append_to(result).name("Bounding box")

        self.app.active_editor().selection().clear().add(bounding_box).vis_properties().set_real_opacity(127, 0).parent().clear()