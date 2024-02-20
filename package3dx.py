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

from enum import Enum
class Status(Enum):
    IN_PROGRESS = 1
    COMPLETED = 2
    CANCELLED = 3

    def __str__(self):
        return str(self.value)
    

    def __int__(self):
        return self.value
    
    def name(self):
        return self.__class__.__name__
    
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'

try:
    from experience import *

    with DrawingReady() as cat:
        print("ready")      
        app = cat.app

        sel = app.active_editor().selection()
        print("sel", sel.count())
        if sel.count():
            obj = sel.item(1).value(DrawingTable)
            print(obj.get_cell_border_type(1,1))
            border = obj.get_cell_border(1, 3).backslash(False).slash(False)
            print(border, border.col(), border.row())
            obj.set_cell_border(border)

            border1 = DrawingCellBorder(0, 2, 3).backslash(True).slash(True)
            obj.set_cell_border(border1)

            border2 = DrawingCellBorder().col(5).row(2).backslash(True).slash(True)
            obj.set_cell_border(border2)

            obj.set_cell_border(DrawingCellBorder(0, 2, 1).top(True).bottom(True).slash(True).backslash(True))
            obj.set_cell_border(DrawingCellBorder(0, 1, 1).activate_all().backslash(False))
            #print(obj.get_bault_text(AnnotationValueIndex.main_value))
            #print(obj.drawing_dim_line.GetDimLineDir())

            #print(cat.drawing.active_sheet().print_area().get_area())


        # def some_func(i_type: Status):
        #     print(i_type, type(i_type))
        #     print(int(i_type) + 3)

        # some_func(Status.IN_PROGRESS)
        # some_func(1)
        
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