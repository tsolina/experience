import traceback
import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {elapsed_time} seconds")


def test():
    app.script_command(2).status_bar("test").script_command(1)
    # print("full name: ", app.full_name())

    with Timer():
        print(app.active_window().active_viewer().get_background_color())
        print(app.active_window().active_viewer().create_viewer_3d().rendering_mode())
        app.active_window().active_viewer().create_viewer_3d().full_screen(True)

    # sel = app.active_editor().selection()
    # sel.search(".'Axis System',all")
    # rVal = sel.vis_properties().get_real_color()    
    # print(rVal)

    from experience.mecmod_interfaces import Part
    p = app.active_editor().active_object(Part)
    p.axis_systems().item(1).is_current(True).is_current()
    # print(dir(p.part_services()))
    # print("show", app.active_editor().selection().add(p).vis_properties().get_show())
    print("mainbody", p.main_body().name())
    hsf = p.hybrid_shape_factory()
    firstSet = p.hybrid_bodies().item(1)
    firstShape = firstSet.hybrid_shapes().item(1)
    
    from experience.cat_gsm_interfaces import HybridShapeCurvePar
    pt = hsf.add_new_point_coord(100,50, 30)
    pt1 = hsf.add_new_point_coord(200,50, 30)

    line = hsf.add_new_line_pt_pt(pt, pt1).compute()
    firstSet.append_hybrid_shape(line)

    pt.x().valuate_from_string("58mm")
    pt.compute()
    line.compute()
    
    print(pt.get_coordinates(), pt1.get_coordinates())

    p.shape_factory().add_new_auto_fillet(5)

    # from experience.base_interfaces.base_application import experience_application as exp3d
    #from experience import *

try:
    from experience import *
    """
    with PartReady() as cat:
        print("part is ready")      
        app = cat.app()

        print(app.name(), cat.part().main_body().name())

        sel = app.active_editor().selection()
        print("sel", sel.count())
    """
    with DrawingReady() as dr:
        sel = dr.app.active_editor().selection()
        
        ddim = sel.item(1).value(DrawingText)

        print(ddim.name(), ddim.text_properties)
        
except Exception as e:
    traceback_str = traceback.format_exc()
    print("traceback", traceback_str)

def start():
    print("OK")



start()
input("Done")

class Base():
    def method(self) -> 'Base':
        return self
    
class Derived(Base):
    def other_method(self)-> 'Derived':
        return self
    
Derived().method()