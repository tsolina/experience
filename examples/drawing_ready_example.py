# - this example shows the possibility to directly work in drawing context -
import traceback

try:
    from experience import DrawingReady

    with DrawingReady() as cat:
        # - perform the ckeck if part is ready and executes the code -
        print("drawing is ready")

        # - access Application object from wrapper -     
        app = cat.app

        # - print name of of active sheet - 
        sheet = cat.drawing.active_sheet()
        print(sheet.name())

        # - accessing active view -
        view = sheet.active_view().x(100).y(200)
        print(view.set_view_name("front ", "test view", " some suffix").name())

        # - add text and set its frame and angle -
        view.texts().add("text added", 100, 100).frame_type(5).angle(45)

        # - print 3DExperience name -
        print(app.name())
        
except Exception as e:
    # - throws the error in case that part was not active -
    traceback_str = traceback.format_exc()
    print("traceback", traceback_str)

input("Press enter to continue...")