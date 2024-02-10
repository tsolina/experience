from win32com.client import Dispatch

from experience.inf_interfaces.application import Application

def experience_application() -> Application:
    return Application(Dispatch('CATIA.Application'))

#"C:\Program Files\Dassault Systemes\B426_Cloud\win_b64\code\bin\DSYAutomation.chm"