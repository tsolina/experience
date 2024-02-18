from .system_types import CATScriptLanguage, CatScriptLibraryType

from .i_unknown import IUnknown 
from .i_dispatch import IDispatch #IUnknown
from .cat_base_unknown import CATBaseUnknown # IDispatch
from .cat_base_dispatch import CATBaseDispatch # CATBaseUnknown

from .any_object import AnyObject
from .collection import Collection # AnyObject

from .system_service import SystemService # AnyObject
from .setting_controller import SettingController # AnyObject

from .dl_name_setting_att import DLNameSettingAtt # SettingController
from .dyn_license_setting_att import DynLicenseSettingAtt # SettingController
from .setting_repository import SettingRepository # SettingController
from .license_setting_att import LicenseSettingAtt # SettingController

# from system import CATScriptLanguage, CatScriptLibraryType, AnyObject, CATBaseDispatch, CATBaseUnknown, Collection, IDispatch, IUnknown, SystemService, SettingController
# from system import DLNameSettingAtt, DynLicenseSettingAtt, SettingRepository, LicenseSettingAtt
