from typing import TYPE_CHECKING

from experience.cat_material_interfaces import MaterialDomainContent
from experience.cat_material_interfaces.cat_material_types import *

if TYPE_CHECKING:
    from experience.types import cat_variant

class AnalysisLinearElasticDomain(MaterialDomainContent):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMaterialIDLItf.MaterialDomainContent
                |                         AnalysisLinearElasticDomain
    """

    def __init__(self, com):
        super().__init__(com)
        self.analysis_linear_elastic_domain = com

    def domain_type(self) -> LinearElasticDomainType:
        """ - deprecated - """
        return self.analysis_linear_elastic_domain.DomainType
       
    def domain_parameters_check(self) -> 'AnalysisLinearElasticDomain':
        """ - deprecated - """
        self.analysis_linear_elastic_domain.DomainParametersCheck()
        return self
    
    def get_domain_parameter(self, i_param_name: str) -> 'cat_variant':
        """ - deprecated - """
        return self.analysis_linear_elastic_domain.GetDomainParameter(i_param_name)
    
    def set_domain_parameter(self, i_param_name: str, i_param_value: 'cat_variant') -> 'AnalysisLinearElasticDomain':
        """ - deprecated - """
        self.analysis_linear_elastic_domain.SetDomainParameter(i_param_name, i_param_value)
        return self