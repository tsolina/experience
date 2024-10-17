from experience import *
import traceback

# accessing application
app = experience_application()

# accessing part and hsf
part = app.active_editor().active_object(Part)

def layout_2d():
    root = part.layout_2d_root()
    if root is None:
        root = part.layout_2d_factory().create_2d_layout("LayoutRoot")

    sheet = root.active_sheet()
    # sheet.activate().views().add_primary(0, 0)
    view = sheet.views().active_view()

    print(root.rendering_mode())
    print(view.get_view_name())

    print(root.layout_services() is None)

rbs = part.get_item("KnowledgeObjects", KnowledgeObjects).get_knowledge_root_set(True, KnowledgeSetType.kweRuleBasesType).as_pyclass(ExpertRuleBasesSet)
rbf = rbs.factory().as_pyclass(ExpertRuleBasesFactory)
rb = rbf.create_rule_base("testRule")
rbr = rb.volatile_copy().rule_set()
print(dir(rbr))
#print(rb.relation.Value)
rbr.comment("Rule Comment")

print(rbr.comment)
#
print("ok")