from typing import TYPE_CHECKING
from experience.system.any_object import AnyObject

if TYPE_CHECKING:
    from experience.plm_access_interfaces import PLMScriptService, PLMSearch, SearchService
    from experience.plm_session_builder_interfaces import PLMNewService, PLMOpenService, PLMPropagateService
    from experience.vpm_editor_context_interfaces import PLMProductService, ProductSessionService
    from experience.knowledge_interfaces import KnowledgeServices
    from experience.drafting_interfaces import DrawingGenService
    from experience.plm_application_context_interfaces import PLMRefreshService
    from experience.plm_application_context_interfaces import PnOService
    from experience.cat_material_interfaces import MATPLMService

class Services():
    def __init__(self, com):
        self.services = com

    def plm_script_service(self) -> 'PLMScriptService':
        from experience.plm_access_interfaces import PLMScriptService
        return PLMScriptService(self.services.Application.GetSessionService("PLMScriptService"))
    
    def plm_search(self) -> 'PLMSearch':
        """ Deprecated, use SearchService instead """
        from experience.plm_access_interfaces import PLMSearch
        return PLMSearch(self.services.Application.GetSessionService("PLMSearch"))
    
    def search_service(self) -> 'SearchService':
        from experience.plm_access_interfaces import SearchService
        return SearchService(self.services.Application.GetSessionService("Search"))
    

    def new_service(self) -> 'PLMNewService':
        from experience.plm_session_builder_interfaces import PLMNewService
        return PLMNewService(self.services.Application.GetSessionService("PLMNewService"))

    def open_service(self) -> 'PLMOpenService':
        from experience.plm_session_builder_interfaces import PLMOpenService
        return PLMOpenService(self.services.Application.GetSessionService("PLMOpenService"))

    def propagate_service(self) -> 'PLMPropagateService':
        from experience.plm_session_builder_interfaces import PLMPropagateService
        return PLMPropagateService(self.services.Application.GetSessionService("PLMPropagateService"))  
      
    
    # def product_service(self) -> 'PLMProductService':
    #     from experience.vpm_editor_context_interfaces import PLMProductService
    #     return PLMProductService(self.services.Application.GetSessionService("PLMProductService"))

    def product_session_service(self) -> 'ProductSessionService':
        from experience.vpm_editor_context_interfaces import ProductSessionService
        return ProductSessionService(self.services.Application.GetSessionService("ProductSessionService")) 
    
    def knowledge_services(self) -> 'KnowledgeServices':
        from experience.knowledge_interfaces import KnowledgeServices
        return KnowledgeServices(self.services.Application.GetSessionService("KnowledgeServices")) 
    
    def drawing_gen_service(self) -> 'DrawingGenService':
        from experience.drafting_interfaces import DrawingGenService
        return DrawingGenService(self.services.Application.GetSessionService("CATDrawingGenService")) 
    
    def plm_refresh_service(self) -> 'PLMRefreshService':
        from experience.plm_application_context_interfaces.plm_refresh_service import PLMRefreshService
        return PLMRefreshService(self.services.Application.GetSessionService("PLMRefreshService")) 
    
    def pno_service(self) -> 'PnOService':
        from experience.plm_application_context_interfaces import PnOService
        return PnOService(self.services.Application.GetSessionService("PnOService")) 

    def mat_plm_service(self) -> 'MATPLMService':
        from experience.cat_material_interfaces import MATPLMService
        return MATPLMService(self.services.Application.GetSessionService("MATPLMService"))    

    def __repr__(self):
        return f'Services()'

    #set myDrawService = CATIA.GetSessionService("CATDrawingService")   
    
# return Service(self._com.GetSessionService("IDService"))
