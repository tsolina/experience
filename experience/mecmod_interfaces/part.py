from typing import Union
from experience.cat_part_interfaces.shape_factory import ShapeFactory
from experience.cat_tps_interfaces import AnnotationSets
from experience.exceptions import CATIAApplicationException
from experience.knowledge_interfaces import Parameters, Relations
from experience.system import AnyObject, Collection
from experience.inf_interfaces import Reference

from .axis_system import AxisSystem #- AnyObject
from .axis_systems import AxisSystems #- Collection
from .body import Body #- AnyObject
from .bodies import Bodies #- Collection
from .constraints import Constraints #- Collection
from .hybrid_bodies import HybridBodies #- Collection
from .ordered_geometrical_sets import OrderedGeometricalSets #- Collection
from .origin_elements import OriginElements #- AnyObject
from .part_services import PartServices #- AnyObject
from .shape import Shape #- AnyObject
from .shapes import Shapes #- Collection
from .sketches import Sketches #- Collection


from .factory import Factory # AnyObject
from experience.cat_gsm_interfaces import HybridShapeFactory
from .geometric_elements import GeometricElements # Collection, GeometricElement

class Part(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.part = com
        self._com = com

    def annotation_sets(self) -> Collection:
        return AnnotationSets(self.part.AnnotationSets)

    def axis_systems(self) -> AxisSystems:
        return AxisSystems(self.part.AxisSystems)

    def bodies(self) -> Bodies:
        return Bodies(self.part.Bodies)

    def constraints(self) -> Constraints:
        return Constraints(self.part.Constraints)

    def density(self) -> float:
        return self.part.Density

    def geometric_elements(self) -> GeometricElements:
        return GeometricElements(self.part.GeometricElements)

    def hybrid_bodies(self) -> HybridBodies:
        return HybridBodies(self.part.HybridBodies)

    def hybrid_shape_factory(self) -> HybridShapeFactory:
        return HybridShapeFactory(self.part.HybridShapeFactory)

    def in_work_object(self, value: AnyObject = None) -> Union['Part', AnyObject]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.part.InWorkObject = value
            return self
        return AnyObject(self.part.InWorkObject)

    def main_body(self, value: Body = None) -> Union[Body, 'Part']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.part.MainBody = value
            return self
        return Body(self.part.MainBody)

    def ordered_geometrical_sets(self) -> OrderedGeometricalSets:
        return OrderedGeometricalSets(self.part.OrderedGeometricalSets)

    def origin_elements(self) -> OriginElements:
        return OriginElements(self.part.OriginElements)

    def parameters(self) -> Parameters:
        return Parameters(self.part.Parameters)
    
    def part_services(self) -> PartServices:
        return PartServices(self.part.GetItem("CATPartServices"))

    def relations(self) -> Relations:
        return Relations(self.part.Relations)

    def shape_factory(self) -> ShapeFactory:
        return ShapeFactory(self.part.ShapeFactory)

    # @property
    # def sheet_metal_factory(self) -> Factory:
    #     return Factory(self.part.SheetMetalFactory)

    # @property
    # def sheet_metal_parameters(self) -> AnyObject:
    #     return AnyObject(self.part.SheetMetalParameters)

    def user_surfaces(self) -> Collection:
        return Collection(self.part.UserSurfaces)

    def activate(self, i_object: AnyObject) -> 'Part':
        self.part.Activate(i_object._com)
        return self

    def create_reference_from_b_rep_name(self, i_label: str, i_object_context: AnyObject) -> 'Reference':
        return Reference(self.part.CreateReferenceFromBRepName(i_label, i_object_context._com))

    def create_reference_from_geometry(self, i_object: AnyObject) -> 'Reference':
        return Reference(self.part.CreateReferenceFromGeometry(i_object._com))

    def create_reference_from_name(self, i_label: str) -> 'Reference':
        return Reference(self.part.CreateReferenceFromName(i_label))

    def create_reference_from_object(self, i_object: AnyObject) -> 'Reference':
        return Reference(self.part.CreateReferenceFromObject(i_object._com))

    def deactivate(self, i_object: AnyObject) -> 'Part':
        self.part.Inactivate(i_object._com)
        return self

    def find_object_by_name(self, i_obj_name: str) -> AnyObject:
        if self.part.FindObjectByName(i_obj_name):
            return AnyObject(self.part.FindObjectByName(i_obj_name))
        else:
            raise CATIAApplicationException('Could not find object.')

    def freeze(self, i_object: AnyObject) -> 'Part':
        self.part.Freeze(i_object)
        return self

    def get_customer_factory(self, i_factory_iid: str) -> Factory:
        return Factory(self.part.GetCustomerFactory(i_factory_iid))

    def inactivate(self, i_object: AnyObject) -> 'Part':
        self.part.Inactivate(i_object._com)
        return self

    def is_frozen(self, i_object: AnyObject) -> bool:
        return self.part.IsFrozen(i_object)

    def is_inactive(self, i_object: AnyObject) -> bool:
        return self.part.IsInactive(i_object._com)

    def is_up_to_date(self, i_object: AnyObject) -> bool:
        return self.part.IsUpToDate(i_object._com)

    def unfreeze(self, i_object: AnyObject) -> 'Part':
        self.part.Unfreeze()
        return self

    def update(self) -> 'Part':
        self.part.Update()
        return self

    def update_object(self, i_object: AnyObject) -> 'Part':
        self.part.UpdateObject(i_object._com)
        return self