# try:
from .enumeration import enumeration_types
from .exceptions import CATIAApplicationException

from .base_interfaces import *
from .system import *
from .drafting_interfaces import *
from .cat_annotation_interfaces import *
from .cat_opns_measure_interfaces import *
from .inf_interfaces import *
from .inf_os_idl_interfaces import *
from .knowledge_interfaces import *
from .cat_sketcher_interfaces import *
from .cat_part_interfaces import *
from .cat_tps_interfaces import *

from .cat_gsm_interfaces import *
from .mecmod_interfaces import *
from .types import *

from .plm_modeler_base_interfaces import *
from .product_structure_client_interfaces import *

from .plm_access_interfaces import *
from .plm_session_builder_interfaces import *
from .vpm_editor_context_interfaces import *

from .plm_application_context_interfaces import *
from .plm_validation_interfaces import *
from .cat_material_interfaces import *

from .cat_digitized_morphing_interfaces import *
from .drafting_2d_interfaces import *

# from cat_logger import create_logger
# except Exception as e:
#     print(f"Top: {e}" )