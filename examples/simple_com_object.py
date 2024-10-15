import logging
import win32com.server
import win32com.server.register
import os
import sys
from bounding_box_dependent import bounding_box

logging.basicConfig(filename='com_object.log', level=logging.DEBUG)
logging.debug("Starting COM server...")

class SimpleCOMObject:
    _reg_progid_ = "Python.SimpleCOMObject"
    _reg_clsid_ = "{A1B2C3D4-E5F6-7A8B-9A0B-C1D2E3F4A5B6}"
    _public_methods_ = ['hello', 'boundingBox']


    def hello(self):
        logging.debug("hello method called")
        return "Hello from COM!"
    
    def boundingBox(self, i_catia):
        app = win32com.client.Dispatch(i_catia)
        return bounding_box(app)

if __name__ == '__main__':
    logging.debug("Registering COM object")
    # Unregister the existing COM object
    win32com.server.register.UnregisterServer("{A1B2C3D4-E5F6-7A8B-9A0B-C1D2E3F4A5B6}")

    # Update LocalServer32 path manually in the registry
    import win32api
    import win32con

    # Define your script path
    script_path = os.path.abspath(sys.argv[0])  # This will get the path to your current script
    python_path = r"C:\Users\Tom\AppData\Local\Programs\Python\Python313\pythonw.exe"

    # Register the COM object
    win32com.server.register.UseCommandLine(SimpleCOMObject, pythonInstString=script_path)

    # Build the command for LocalServer32
    command = f'"{python_path}" "{script_path}" {{A1B2C3D4-E5F6-7A8B-9A0B-C1D2E3F4A5B6}}'
    logging.debug("command: %s", command)

    # Set the LocalServer32 path in the registry
    registry_key = win32api.RegOpenKeyEx(win32con.HKEY_CLASSES_ROOT, 
                                           f'CLSID\\{{A1B2C3D4-E5F6-7A8B-9A0B-C1D2E3F4A5B6}}\\LocalServer32', 
                                           0, 
                                           win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(registry_key, '', 0, win32con.REG_SZ, command)
    win32api.RegCloseKey(registry_key)

    logging.debug("COM object registered successfully.")
    print("COM object registered successfully.")


'''
if __name__ == '__main__':
    win32com.server.register.UnregisterServer("{A1B2C3D4-E5F6-7A8B-9A0B-C1D2E3F4A5B6}")
    win32com.server.register.UseCommandLine(SimpleCOMObject)
'''

'''
Sub testLib()
    Dim com As Object
    Set com = CreateObject("Python.SimpleCOMObject")
    Debug.Print com.hello
End Sub
'''
