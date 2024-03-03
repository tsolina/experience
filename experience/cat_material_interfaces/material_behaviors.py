from typing import Iterator, TYPE_CHECKING

from experience.cat_material_interfaces import MaterialBehavior
from experience.plm_modeler_base_interfaces import PLMEntities

if TYPE_CHECKING:
    from experience.types.general import cat_variant

class MaterialBehaviors(PLMEntities):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     PLMModelerBaseIDLItf.PLMEntities
                |                         MaterialBehaviors
    """

    def __init__(self, com):
        super().__init__(com, child=MaterialBehavior)
        self.material_behaviors = com

    def add_simulation_behavior(self) -> MaterialBehavior:
        return self.material_behaviors.AddSimulationBehavior()
    
    def get_behavior(self, i_index: 'cat_variant') -> 'MaterialBehavior':
        return MaterialBehavior(self.material_behaviors.GetBehavior(i_index))
    
    def remove(self, i_behavior: MaterialBehavior) -> 'MaterialBehaviors':
        self.material_behaviors.Remove(i_behavior)
        return self

    def __getitem__(self, n: int) -> MaterialBehavior:
        if (n + 1) > self.count():
            raise StopIteration

        return MaterialBehavior(self.material_behaviors.item(n + 1))

    def __iter__(self) -> Iterator[MaterialBehavior]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))