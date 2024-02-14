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

    def VisuService(self) -> 'VisuServices':
        from experience.inf_interfaces import VisuServices
        return VisuServices(self.editor_services.GetService("VisuServices"))

    def DrawingService(self) -> 'DrawingService':
        from experience.drafting_interfaces import DrawingService
        return DrawingService(self.editor_services.GetService("CATDrawingService"))

    def PLMProductService(self) -> 'PLMProductService':
        from experience.vpm_editor_context_interfaces import PLMProductService
        return PLMProductService(self.editor_services.GetService("PLMProductService"))
    
    def MeasureService(self) -> 'MeasureService':
        from experience.cat_opns_measure_interfaces import MeasureService
        return MeasureService(self.editor_services.GetService("MeasureService"))
    
    def MeasurableService(self) -> 'MeasurableService':
        from experience.cat_opns_measure_interfaces import MeasurableService
        return MeasurableService(self.editor_services.GetService("MeasurableService"))

    def __repr__(self):
        return f'EditorServices()'