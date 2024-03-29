from typing import Union, Optional, TYPE_CHECKING

from experience.system import AnyObject
from experience.inf_interfaces import Service
from experience.cat_opns_measure_interfaces.opns_measure_types import *

if TYPE_CHECKING:
    from experience.cat_opns_measure_interfaces import MeasurableInContext, MeasurableAxisSystem, MeasurableBetween, MeasurableCircle, MeasurableCone, MeasurableLine
    from experience.cat_opns_measure_interfaces import MeasurableCurve, MeasurableCylinder, MeasurablePlane, MeasurablePoint, MeasurableSphere, MeasurableSurface, MeasurableVolume

class MeasurableService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         MeasurableService
    """

    def __init__(self, com):
        super().__init__(com)
        self.measurable_service = com

    def get_measurable(self, i_measured_item: AnyObject, i_type: CATMeasurableType) -> 'MeasurableInContext':
        from experience.cat_opns_measure_interfaces import MeasurableInContext
        return MeasurableInContext(self.measurable_service.GetMeasurable(i_measured_item._com, int(i_type)))
    
    def get_measurable_axis_system(self, i_measured_item: AnyObject) -> 'MeasurableAxisSystem':
        from experience.cat_opns_measure_interfaces import MeasurableAxisSystem
        return MeasurableAxisSystem(self.get_measurable(i_measured_item, int(CATMeasurableType.CAAMeasurableAxisSystem))._com)
    
    def get_measurable_between(self, i_measured_item: AnyObject) -> 'MeasurableBetween':
        from experience.cat_opns_measure_interfaces import MeasurableBetween
        return MeasurableBetween(self.get_measurable(i_measured_item, int(CATMeasurableType.CAAMeasurableBetween))._com)
    
    def get_measurable_circle(self, i_measured_item: AnyObject) -> 'MeasurableCircle':
        from experience.cat_opns_measure_interfaces import MeasurableCircle
        return MeasurableCircle(self.get_measurable(i_measured_item, int(CATMeasurableType.CAAMeasurableCircle))._com)

    def get_measurable_cone(self, i_measured_item: AnyObject) -> 'MeasurableCone':
        from experience.cat_opns_measure_interfaces import MeasurableCone
        return MeasurableCone(self.get_measurable(i_measured_item,int(CATMeasurableType.CAAMeasurableCone))._com)
    
    def get_measurable_curve(self, i_measured_item: AnyObject) -> 'MeasurableCurve':
        from experience.cat_opns_measure_interfaces import MeasurableCurve
        return MeasurableCurve(self.get_measurable(i_measured_item, int(CATMeasurableType.CAAMeasurableCurve))._com)
    
    def get_measurable_cylinder(self, i_measured_item: AnyObject) -> 'MeasurableCylinder':
        from experience.cat_opns_measure_interfaces import MeasurableCylinder
        return MeasurableCylinder(self.get_measurable(i_measured_item, int(CATMeasurableType.CAAMeasurableCylinder))._com)    

    def get_measurable_line(self, i_measured_item: AnyObject) -> 'MeasurableLine':
        from experience.cat_opns_measure_interfaces import MeasurableLine
        return MeasurableLine(self.get_measurable(i_measured_item, int(CATMeasurableType.CAAMeasurableLine))._com)

    def get_measurable_plane(self, i_measured_item: AnyObject) -> 'MeasurablePlane':
        from experience.cat_opns_measure_interfaces import MeasurablePlane
        return MeasurablePlane(self.get_measurable(i_measured_item, int(CATMeasurableType.CAAMeasurablePlane))._com)
    
    def get_measurable_point(self, i_measured_item: AnyObject) -> 'MeasurablePoint':
        from experience.cat_opns_measure_interfaces import MeasurablePoint
        return MeasurablePoint(self.get_measurable(i_measured_item, int(CATMeasurableType.CAAMeasurablePoint))._com)
    
    def get_measurable_sphere(self, i_measured_item: AnyObject) -> 'MeasurableSphere':
        from experience.cat_opns_measure_interfaces import MeasurableSphere
        return MeasurableSphere(self.get_measurable(i_measured_item, int(CATMeasurableType.CAAMeasurableSphere))._com)
    
    def get_measurable_surface(self, i_measured_item: AnyObject) -> 'MeasurableSurface':
        from experience.cat_opns_measure_interfaces import MeasurableSurface
        return MeasurableSurface(self.get_measurable(i_measured_item, int(CATMeasurableType.CAAMeasurableSurface))._com)

    def get_measurable_volume(self, i_measured_item: AnyObject) -> 'MeasurableVolume':
        from experience.cat_opns_measure_interfaces import MeasurableVolume
        return MeasurableVolume(self.get_measurable(i_measured_item, int(CATMeasurableType.CAAMeasurableVolume))._com)
    
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'