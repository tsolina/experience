from typing import TYPE_CHECKING
from experience.system.any_object import AnyObject

if TYPE_CHECKING:
    from experience.plm_access_interfaces import PLMScriptService, PLMSearch, SearchService
    from experience.plm_session_builder_interfaces import PLMNewService, PLMOpenService, PLMPropagateService
    from experience.vpm_editor_context_interfaces import PLMProductService, ProductSessionService
    from experience.knowledge_interfaces import KnowledgeServices

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
    

    def open_service(self) -> 'PLMNewService':
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
    
    def __repr__(self):
        return f'Services()'

    #set myDrawService = CATIA.GetSessionService("CATDrawingService")   
    
# return Service(self._com.GetSessionService("IDService"))
