# basic example to hide selected item
# part must be open to run this example
from experience import *

# accessing application
app = experience_application()

app.active_editor().selection().vis_properties().set_show(1)
#or
app.active_editor().selection().vis_properties().set_show(CatVisPropertyShow.catVisPropertyNoShowAttr)
