from experience import *
import traceback

app = experience_application()
sel = app.active_editor().selection()
#dd = DrawingDimension(sel.item(1).value()._com)
dd = sel.item(1).value(DrawingDimension)

#print(dd.get_value().value())
#print(dd.get_boundary_box()) # to test more
# print(dd.get_tolerances())

if dd.is_clipped():
     print(dd.unclip().name())

print(dd.name())

#print(dd.unclip())