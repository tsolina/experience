from typing import TYPE_CHECKING

from experience.cat_material_interfaces import MaterialGeneric
from experience.cat_material_interfaces.cat_material_types import *

if TYPE_CHECKING:
    from experience.cat_material_interfaces import MaterialDomains, MaterialBehaviors

class Material(MaterialGeneric):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         CATMaterialIDLItf.MaterialGeneric
                |                             Material
    """

    def __init__(self, com):
        super().__init__(com)
        self.material = com

    def get_domains(self) -> 'MaterialDomains':
        from experience.cat_material_interfaces import MaterialDomains
        return MaterialDomains(self.material.GetDomains())
    
    def get_simulation_behaviors(self) -> 'MaterialBehaviors':
        from experience.cat_material_interfaces import MaterialBehaviors
        return MaterialBehaviors(self.material.GetSimulationBehaviors())