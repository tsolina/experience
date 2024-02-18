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

try:
    from experience import *

    with DrawingReady() as cat:
        print("ready")      
        app = cat.app

        sel = app.active_editor().selection()
        print("sel", sel.count())
        if sel.count():
            obj = sel.item(1).value(DrawingComponent)
            #print(obj.drawing_component.GetMatrix())
            #print(obj.get_matrix())
            # return f'{self.__class__.__name__}(name="{self.name()}")'
            print(cat.drawing.active_sheet().print_area().get_area())


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