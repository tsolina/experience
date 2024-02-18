# - this example shows the possibility to directly work in part context -
import traceback

try:
    from experience import PartReady

    with PartReady() as cat:
        # - perform the ckeck if part is ready and executes the code -
        print("part is ready")

        # - access Application object from wrapper -     
        app = cat.app

        # - print name of of main body - 
        print(cat.part.main_body().name())

        # - print 3DExperience name -
        print(app.name())

        sel = cat.app.active_editor().selection()
        print(sel.vis_properties().get_pick())
        
except Exception as e:
    # - throws the error in case that part was not active -
    traceback_str = traceback.format_exc()
    print("traceback", traceback_str)

input("Press enter to continue...")