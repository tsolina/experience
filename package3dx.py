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


try:
    from experience import *

    with PartReady() as cat:
        print("part is ready")      
        app = cat.app

        print(app.name(), cat.part.main_body().name())

        sel = app.active_editor().selection()
        print("sel", sel.count())
        
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