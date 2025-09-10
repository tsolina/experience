import experience as exp
from experience import PartReady

with PartReady() as cat:
    hsf = cat.part.hybrid_shape_factory()
    axis = cat.part.axis_systems().item(1)
    point = hsf.add_new_point_coord(10,20,10).compute()

    pt_with_ref = hsf.add_new_point_coord(30, 30, 20).pt_ref(point).ref_axis_system(axis).compute()

    cat.part.hybrid_bodies().item(1).append_hybrid_shape(pt_with_ref)
    
    x,y,z = axis.get_x_axis()
    dir_x = hsf.add_new_direction_by_coord(x,y,z).compute()
    origin = axis.origin_type(exp.CATAxisSystemOriginType.catAxisSystemOriginByCoordinates)
    dir_x = axis.x_axis_direction()

    pt:exp.HybridShapePointCoord = hsf.add_new_point_coord(30, 30, 20).pt_ref(point).ref_axis_system(axis).compute()
    x,y,z = pt.get_coordinates()

    