# - this example creates two points and line through them and and then performs some measures -
from experience import PartReady

# - select to work in part environment -
with PartReady() as cat:
    # - access hybrid shape facorty -
    hsf = cat.part.hybrid_shape_factory()

    # - create a geometrical set to store geometry -
    g_set = cat.part.hybrid_bodies().add().name("measuring")

    # - create two points, compute, rename and assign them to set -
    p1 = hsf.add_new_point_coord(50, 100, 75).compute().append_to(g_set).name("first point")
    p2 = hsf.add_new_point_coord(150, 30, 105).compute().append_to(g_set).name("last point")

    # - create line trough those points, compute, rename and assign it to the set -
    line = hsf.add_new_line_pt_pt(p1, p2).compute().append_to(g_set).name("line")

    # - access measurable environment -
    measure = cat.app.active_editor().services().MeasurableService()

    # - measure distance between two points -
    print("distance between points: ", measure.get_measurable_between(p1).distance_min_to_value_only(p2))

    # - set measurable line -
    measurable_line = measure.get_measurable_line(line)

    # - print length and origin of the line -
    print("length of the line:", measurable_line.get_length(), "origin of the line:", measurable_line.get_origin())

    # - print start point, middle point and end point -
    print("first, middle, end point:", measurable_line.get_points())


input('Press enter to continue...')