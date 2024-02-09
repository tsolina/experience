from .boolean_shape import BooleanShape
from .add import Add # BooleanShape
from .assemble import Assemble # BooleanShape
from .intersect import Intersect # BooleanShape
from .remove import Remove # BooleanShape
from .trim import Trim # BooleanShape

from .dress_up_shape import DressUpShape
from .auto_draft import AutoDraft # DressUpShape
from .auto_fillet import AutoFillet # DressUpShape
from .chamfer import Chamfer # DressUpShape
from .defeaturing import Defeaturing # DressUpShape
from .draft import Draft # DressUpShape
from .fillet import Fillet # DressUpShape
from .remove_face import RemoveFace # DressUpShape
from .scaling import Scaling # DressUpShape
from .shell import Shell # DressUpShape
from .thickness import Thickness # DressUpShape
from .thread import Thread # DressUpShape


from .defeaturing_filter import DefeaturingFilter
from .defeaturing_filters import DefeaturingFilters # DefeaturingFilter
from .draft_domain import DraftDomain
from .draft_domains import DraftDomains # DraftDomain

from .limit import Limit

from .repartition import Repartition
from .angular_repartition import AngularRepartition # Repartition
from .linear_repartition import LinearRepartition # Repartition


from .surface_based_shape import SurfaceBasedShape
from .close_surface import CloseSurface # SurfaceBasedShape
from .replace_face import ReplaceFace # SurfaceBasedShape
from .sew_surface import SewSurface # SurfaceBasedShape
from .split import Split # SurfaceBasedShape
from .thick_surface import ThickSurface # SurfaceBasedShape


from .transformation_shape import TransformationShape
from .mirror import Mirror # TransformationShape
from .pattern import Pattern # TransformationShape
from .circ_pattern import CircPattern # Pattern
from .rect_pattern import RectPattern # Pattern
from .user_pattern import UserPattern # Pattern


from .edge_fillet import EdgeFillet # Fillet
from .face_fillet import FaceFillet # Fillet
from .tritangent_fillet import TritangentFillet # Fillet

from .const_rad_edge_fillet import ConstRadEdgeFillet # EdgeFillet
from .var_rad_edge_fillet import VarRadEdgeFillet # EdgeFillet

from .sketch_based_shape import SketchBasedShape
from .revolution import Revolution # SketchBasedShape
from .hole import Hole # SketchBasedShape
from .prism import Prism # SketchBasedShape
from .sweep import Sweep # SketchBasedShape
from .solid_combine import SolidCombine # SketchBasedShape
from .stiffener import Stiffener # SketchBasedShape

from .groove import Groove # Revolution
from .shaft import Shaft # Revolution
from .rib import Rib # Sweep
from .slot import Slot # Sweep

from .pad import Pad # Prism
from .pocket import Pocket # Prism

from .shape_factory import ShapeFactory #- Factory

#BooleanShape, Add, Assemble, Intersect, Remove, Trim, DressUpShape, AutoDraft, AutoFillet, Chamfer, Defeaturing, Draft, Fillet, RemoveFace, Scaling, Shell, Thickness, Thread
#DefeaturingFilter, DefeaturingFilters, DraftDomain, DraftDomains, Limit, Repartition, AngularRepartition, LinearRepartition
#SurfaceBasedShape, CloseSurface, ReplaceFace, SewSurface, Split, ThickSurface, TransformationShape, Mirror, Pattern, CircPattern, RectPattern, UserPattern
#EdgeFillet, FaceFillet, TritangentFillet, ConstRadEdgeFillet, VarRadEdgeFillet, SketchBasedShape, Revolution, Hole, Prism, Sweep, SolidCombine, Stiffener
#Groove, Shaft, Rib, Slot, Pad, Pocket, ShapeFactory