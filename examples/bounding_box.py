# example to create bounding box around selected shape
# part must be open and shape selected to run this example
from experience import *
import traceback
# accessing application
app = experience_application()

# accessing part and hsf
part = app.active_editor().active_object(Part)
hsf = part.hybrid_shape_factory()
sel = app.active_editor().selection()

shape = sel.item(1).value(HybridShape)

result = part.hybrid_bodies().add().name("result")

dir_x = hsf.add_new_direction(part.origin_elements().plane_yz()).compute()
dir_y = hsf.add_new_direction(part.origin_elements().plane_zx()).compute()
dir_z = hsf.add_new_direction(part.origin_elements().plane_xy()).compute()

ext_x_1 = hsf.add_new_extremum(shape, dir_x, 1).direction2(dir_y).direction3(dir_z).compute()
ext_x_2 = hsf.add_new_extremum(shape, dir_x, 0).direction2(dir_y).direction3(dir_z).compute()
ext_y_1 = hsf.add_new_extremum(shape, dir_y, 1).direction2(dir_x).direction3(dir_z).compute()
ext_y_2 = hsf.add_new_extremum(shape, dir_y, 0).direction2(dir_x).direction3(dir_z).compute()
ext_z_1 = hsf.add_new_extremum(shape, dir_z, 1).direction2(dir_x).direction3(dir_y).compute()
ext_z_2 = hsf.add_new_extremum(shape, dir_z, 0).direction2(dir_x).direction3(dir_y).compute()

plane_x1 = hsf.add_new_plane_offset_pt(part.origin_elements().plane_yz(), ext_x_1).compute()
plane_x2 = hsf.add_new_plane_offset_pt(part.origin_elements().plane_yz(), ext_x_2).compute()
plane_y1 = hsf.add_new_plane_offset_pt(part.origin_elements().plane_zx(), ext_y_1).compute()
plane_y2 = hsf.add_new_plane_offset_pt(part.origin_elements().plane_zx(), ext_y_2).compute()
plane_z1 = hsf.add_new_plane_offset_pt(part.origin_elements().plane_xy(), ext_z_1).compute()
plane_z2 = hsf.add_new_plane_offset_pt(part.origin_elements().plane_xy(), ext_z_2).compute()

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

sel.clear().add(bounding_box).vis_properties().set_real_opacity(127, 0).parent().clear()

input("Done")