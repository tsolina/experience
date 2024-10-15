from typing import TYPE_CHECKING
from experience.system.any_object import AnyObject

if TYPE_CHECKING:
    from experience.inf_interfaces import VisuServices
    from experience.drafting_interfaces import DrawingService
    from experience.vpm_editor_context_interfaces import PLMProductService
    from experience.cat_opns_measure_interfaces import MeasureService, MeasurableService
    from experience.plm_validation_interfaces import VALValidationService
    from experience.cat_opns_inertia_interfaces import InertiaService, InertiaBoxService

class EditorServices():
    def __init__(self, com):
        self.editor_services = com

    def drawing_service(self) -> 'DrawingService':
        from experience.drafting_interfaces import DrawingService
        return DrawingService(self.editor_services.GetService("CATDrawingService"))
    
    def inertia_box_service(self) -> 'InertiaBoxService':
        from experience.cat_opns_inertia_interfaces import InertiaBoxService
        return InertiaBoxService(self.editor_services.GetService("InertiaBoxService"))
    
    def inertia_service(self) -> 'InertiaService':
        from experience.cat_opns_inertia_interfaces import InertiaService
        return InertiaService(self.editor_services.GetService("InertiaService"))

    def measure_service(self) -> 'MeasureService':
        '''
        # - seems to have issues with inputs, use measurable_service instead -
        '''        
        from experience.cat_opns_measure_interfaces import MeasureService
        return MeasureService(self.editor_services.GetService("MeasureService"))
    
    def measurable_service(self) -> 'MeasurableService':
        from experience.cat_opns_measure_interfaces import MeasurableService
        return MeasurableService(self.editor_services.GetService("MeasurableService"))

    def plm_product_service(self) -> 'PLMProductService':
        from experience.vpm_editor_context_interfaces import PLMProductService
        return PLMProductService(self.editor_services.GetService("PLMProductService"))
    
    def validation_service(self) -> 'VALValidationService':
        from experience.plm_validation_interfaces import VALValidationService
        return VALValidationService(self.editor_services.GetService("ValidationService"))

    def visu_service(self) -> 'VisuServices':
        from experience.inf_interfaces import VisuServices
        return VisuServices(self.editor_services.GetService("VisuServices"))


    def __repr__(self):
        return f'EditorServices()'