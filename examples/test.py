from experience import *
import traceback

# accessing application
app = experience_application()

# accessing part and hsf
part = app.active_editor().active_object(Part)

root = part.layout_2d_root()
if root is None:
    root = part.layout_2d_factory().create_2d_layout("LayoutRoot")

sheet = root.active_sheet()
# sheet.activate().views().add_primary(0, 0)
view = sheet.views().active_view()

print(root.rendering_mode())
print(view.get_view_name())

print(root.layout_services() is None)
#
print("ok")