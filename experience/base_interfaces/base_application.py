from win32com.client import Dispatch

from experience.inf_interfaces.application import Application

_app_instance : Application

def experience_application() -> Application:
    return Application(Dispatch('CATIA.Application'))

def set_application(app) -> Application:
    _app_instance = app
    return _app_instance

def get_application() ->Application:
    return _app_instance

#"C:\Program Files\Dassault Systemes\B426_Cloud\win_b64\code\bin\DSYAutomation.chm"