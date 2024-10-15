# basic example to show access to inertia
# part must be open to run this example
# one solid / hybridShape must be selected

from experience import *
import traceback

# - accessing app and selected element
app = experience_application()
sel = app.active_editor().selection()
dd = sel.item(1).value()

# - access inertia box service and get bounding box information
ibs = app.active_editor().services().inertia_box_service()
bb = ibs.get_inertia_box_element(dd).get_bounding_box()

print(bb)

# - access inertia service and get mass of selected item
iss = app.active_editor().services().inertia_service()
bs = iss.get_inertia_element(dd).get_mass()

print(bs)