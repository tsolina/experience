# basic example to create a line and assign it to new set in GSD
# part must be open to run this example
from experience import *

# accessing application
app = experience_application()

# accessing part and hsf
p = app.active_editor().active_object(Part)
hsf = p.hybrid_shape_factory()

# creation of two points without directly adding them to the tree
pt = hsf.add_new_point_coord(100,50, 30)
pt1 = hsf.add_new_point_coord(200,50, 30)

# creating line and computing it
line = hsf.add_new_line_pt_pt(pt, pt1).compute()

# assigning line to new set named example
first_set = p.hybrid_bodies().add().name("example")
first_set.append_hybrid_shape(line)