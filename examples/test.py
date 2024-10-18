from experience import *
import traceback

# accessing application
app = experience_application()



def layout_2d():
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

def expert_rule():
    part = app.active_editor().active_object(Part)
    rbs = part.get_item("KnowledgeObjects", KnowledgeObjects).get_knowledge_root_set(True, KnowledgeSetType.kweRuleBasesType).as_pyclass(ExpertRuleBasesSet)
    rbf = rbs.factory().as_pyclass(ExpertRuleBasesFactory)
    rb = rbf.create_rule_base("testRule")
    rbr = rb.volatile_copy().rule_set()
    print(dir(rbr))
    #print(rb.relation.Value)
    rbr.comment("Rule Comment")

    print(rbr.comment)

# ssec = app.active_editor().services().section_service()
# print(ssec.count())
# if ssec.count():
#     sec = ssec.item(1)
#     sec.export(app.active_editor().active_object())

ctrl = app.setting_controllers().item("SectioningSettings").as_pyclass(SectioningSettingAtt)
print(ctrl._com.GetAttr("SectionMode"))
print(ctrl.section_mode(2).section_mode())
# print(ctrl.com_type())

ctrl = app.setting_controllers().item("SectioningSettings").as_pyclass(SettingRepository)
print(ctrl.get_attr("SectionMode"))
print(ctrl.get_attr_info("SectionMode"))

print("ok")