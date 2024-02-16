from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference, References
from experience.cat_part_interfaces import EdgeFillet

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class ConstRadEdgeFillet(EdgeFillet):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             PartInterfaces.Fillet
                |                                 PartInterfaces.EdgeFillet
                |                                     ConstRadEdgeFillet
    """

    def __init__(self, com):
        super().__init__(com)
        self.const_rad_edge_fillet = com

    def objects_to_fillet(self) -> References:
        return References(self.const_rad_edge_fillet.ObjectsToFillet)

    def radius(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.const_rad_edge_fillet.Radius)

    def add_object_to_fillet(self, i_object_to_fillet: Reference) -> 'ConstRadEdgeFillet':
        self.const_rad_edge_fillet.AddObjectToFillet(i_object_to_fillet._com)
        return self
    
    def switch_to_var_fillet_type(self) -> 'ConstRadEdgeFillet':
        self.const_rad_edge_fillet.SwitchToVarFilletType()
        return self    

    def withdraw_object_to_fillet(self, i_object_to_withdraw: Reference) -> 'ConstRadEdgeFillet':
        self.const_rad_edge_fillet.WithdrawObjectToFillet(i_object_to_withdraw._com)
        return self

    def __repr__(self):
        return f'ConstRadEdgeFillet(name="{self.name()}")'