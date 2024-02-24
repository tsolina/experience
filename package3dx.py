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
    app = experience_application()

    # sel = app.active_editor().selection()
    # print("sel", sel.count())
    # if sel.count():
    #     #obj = sel.item(1).value(HybridShape)f
    #     vp = sel.vis_properties()
    #     print("test:", vp.get_symbol_type())
    #     vp.set_symbol_type(InfSymbolType.two_unfilled_concentric_circles)

    part = app.active_editor().active_object(Part)
    axis = part.axis_systems().item(1)

    print(axis.name(), axis.get_vectors())

    app.refresh_display(True)
        
except Exception as e:
    traceback_str = traceback.format_exc()
    print("traceback", traceback_str)

def start():
    print("OK")



start()
#input("Done")

class Base():
    def method(self) -> 'Base':
        return self
    
class Derived(Base):
    def other_method(self)-> 'Derived':
        return self
    
Derived().method()