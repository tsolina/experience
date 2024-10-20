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

def expert_rulex():
    part = app.active_editor().active_object(Part)
    rbs = part.get_item("KnowledgeObjects", KnowledgeObjects).get_knowledge_root_set(True, KnowledgeSetType.kweRuleBasesType).as_pyclass(ExpertRuleBasesSet)
    rbf = rbs.factory().as_pyclass(ExpertRuleBasesFactory)
    rb = rbf.create_rule_base("testRule")
    rbr = rb.volatile_copy().rule_set()
    print(dir(rbr))
    #print(rb.relation.Value)
    rbr.comment("Rule Comment")

    print(rbr.comment)

def sectionx():
    # - no such interface available anymore -
    ssec = app.active_editor().services().section_service()
    print(ssec.count())
    if ssec.count():
        sec = ssec.item(1)
        sec.export(app.active_editor().active_object())

def settings():
    ctrl = app.setting_controllers().item("SectioningSettings").as_pyclass(SectioningSettingAtt)
    print(ctrl._com.GetAttr("SectionMode"))
    print(ctrl.section_mode(2).section_mode())
    # print(ctrl.com_type())

    ctrl = app.setting_controllers().item("SectioningSettings").as_pyclass(SettingRepository)
    print(ctrl.get_attr("SectionMode"))
    print(ctrl.get_attr_info("SectionMode"))

def access_part():
    rref = app.active_editor().active_object(VPMRootOccurrence).occurrences().item(1).instance_occurrence_of().reference_instance_of().rep_instances().item(1).reference_instance_of()
    p = rref.part()
    print(p.main_body().name("reference").name())
    print(rref.is_machanism())

ec  = app.active_editor().active_object(VPMRootOccurrence).reference_root_occurrence_of()
conn = ec.get_item("CATEngConnections", EngConnections)
print(conn.count())

print(ec.eng_connections().count())
print(ec.eng_connections().item(1).type())

#Dim myEngConnections As EngConnections. 
#set myEngConnections = myPLMProductReference.GetItem("CATEngConnections").

print("ok")