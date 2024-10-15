import win32com.client

try:
    com_object = win32com.client.Dispatch("Python.SimpleCOMObject")
    print(com_object.hello())
except Exception as e:
    print(f"Error: {e}")