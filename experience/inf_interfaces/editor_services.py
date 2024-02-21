from typing import TYPE_CHECKING
from experience.system.any_object import AnyObject

if TYPE_CHECKING:
    from experience.inf_interfaces import VisuServices
    from experience.drafting_interfaces import DrawingService
    from experience.vpm_editor_context_interfaces import PLMProductService
    from experience.cat_opns_measure_interfaces import MeasureService, MeasurableService

class EditorServices():
    def __init__(self, com):
        self.editor_services = com

    def visu_service(self) -> 'VisuServices':
        from experience.inf_interfaces import VisuServices
        return VisuServices(self.editor_services.GetService("VisuServices"))

    def drawing_service(self) -> 'DrawingService':
        from experience.drafting_interfaces import DrawingService
        return DrawingService(self.editor_services.GetService("CATDrawingService"))

    def plm_product_service(self) -> 'PLMProductService':
        from experience.vpm_editor_context_interfaces import PLMProductService
        return PLMProductService(self.editor_services.GetService("PLMProductService"))
    
    def measure_service(self) -> 'MeasureService':
        # - seems to have issues with inputs, use measurable_service instead -
        from experience.cat_opns_measure_interfaces import MeasureService
        return MeasureService(self.editor_services.GetService("MeasureService"))
    
    def measurable_service(self) -> 'MeasurableService':
        from experience.cat_opns_measure_interfaces import MeasurableService
        return MeasurableService(self.editor_services.GetService("MeasurableService"))

    def __repr__(self):
        return f'EditorServices()'