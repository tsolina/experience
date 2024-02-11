# try:
from .enumeration import enumeration_types
from .exceptions import CATIAApplicationException

from .base_interfaces import experience_application, Experience, PartReady, ProductReady

from .system import AnyObject, CATBaseDispatch, CATBaseUnknown, Collection, IDispatch, IUnknown, SystemService

from .cat_annotation_interfaces import DrawingArrow, DrawingArrows, DrawingCoordDim, DrawingCoordDims, DrawingDimension, DrawingDimensions, DrawingDimExtLine, DrawingDimLine, DrawingDimValue, DrawingGDT, DrawingGDTs, DrawingLeader, DrawingLeaders, DrawingTable, DrawingTables, DrawingText, DrawingTextProperties, DrawingTextRange, DrawingTexts,DrawingWelding,DrawingWeldings

from .inf_interfaces import Application, Camera, Cameras, Camera3D, Editor, Editors, LightSource, LightSources, PageSetup, Printer, Printers, Reference, References
from .inf_interfaces import SelectedElement, Selection, Service, Viewer, Viewpoint2D, Viewer2D, Viewpoint3D, Viewer3D, Viewers, VisPropertySet, Window, Windows, Workbench
from .inf_interfaces import Move, Position, Services, VisuServices

from .inf_os_idl_interfaces import FileComponent, FileSystem, File, Files, Folder, Folders, SystemConfiguration, TextStream
from .knowledge_interfaces import BoolParam, EnumParam, IntParam, KnowledgeActivateObject, KnowledgeObject, Parameter, RealParam, Relation, StrParam, Relations
from .cat_sketcher_interfaces import GeometricElement, Axis2D, Geometry2D, Point2D, Curve2D, Hyperbola2D, ControlPoint2D, Ellipse2D, Circle2D, Parabola2D, Line2D, Spline2D, Factory2D, Sketch

from .cat_part_interfaces import BooleanShape, Add, Assemble, Intersect, Remove, Trim, DressUpShape, AutoDraft, AutoFillet, Chamfer, Defeaturing, Draft, Fillet, RemoveFace, Scaling, Shell, Thickness, Thread
from .cat_part_interfaces import DefeaturingFilter, DefeaturingFilters, DraftDomain, DraftDomains, Limit, Repartition, AngularRepartition, LinearRepartition
from .cat_part_interfaces import SurfaceBasedShape, CloseSurface, ReplaceFace, SewSurface, Split, ThickSurface, TransformationShape, Mirror, Pattern, CircPattern, RectPattern, UserPattern
from .cat_part_interfaces import EdgeFillet, FaceFillet, TritangentFillet, ConstRadEdgeFillet, VarRadEdgeFillet, SketchBasedShape, Revolution, Hole, Prism, Sweep, SolidCombine, Stiffener
from .cat_part_interfaces import Groove, Shaft, Rib, Slot, Pad, Pocket, ShapeFactory

from .cat_gsm_interfaces import HybridShapeFactory
from .mecmod_interfaces import AxisSystem, AxisSystems, Boundary, Constraint, Constraints, HybridShape,HybridShapeInstance, HybridShapes, OriginElements, PartServices, Shape, ShapeInstance, Shapes, Solid, Sketches, Factory, InstanceFactory, GeometricElements, HybridBody, HybridBodies, OrderedGeometricalSet, OrderedGeometricalSets, Body, Bodies, Part
from .types import cat_variant, list_str, any_parameter

from .plm_modeler_base_interfaces import PLMEntity, PLMEntities, PLMOccurrence, PLMOccurrences
from .product_structure_client_interfaces import Shape3D, Shape3Ds, VPMRepOccurrence, VPMRepOccurrences, ParentVPMRepInstances, VPMRepReference, VPMRootOccurrence, VPMReference, VPMRepInstance, VPMRepInstances
from .product_structure_client_interfaces import VPMPublication, VPMPublications, VPMInstance, VPMInstances, VPMOccurrence, VPMOccurrences

from .plm_access_interfaces import DatabaseSearch, IndexedSearch, PLMPlay, PLMScriptService, PLMSearch, PLMSearches, PLMSearchService, SearchService
from .plm_session_builder_interfaces import PLMNewService, PLMOpenService, PLMPropagateService
from .vpm_editor_context_interfaces import PLMProductService, ProductSessionService

from .plm_application_context_interfaces import PLMAppContext # incomplete

# from cat_logger import create_logger
# except Exception as e:
#     print(f"Top: {e}" )