from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference, References
from experience.cat_part_interfaces import Fillet
from experience.cat_part_interfaces.cat_part_types import *

class EdgeFillet(Fillet):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             PartInterfaces.Fillet
                |                                 EdgeFillet
    """

    def __init__(self, com):
        super().__init__(com)
        self.edge_fillet = com

    def edge_propagation(self, value: CatFilletEdgePropagation = None) -> Union['EdgeFillet', CatFilletEdgePropagation]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.edge_fillet.EdgePropagation = int(value)
            return self
        return CatFilletEdgePropagation.item(self.edge_fillet.EdgePropagation)

    def edges_to_keep(self) -> References:
        return References(self.edge_fillet.EdgesToKeep)

    def add_edge_to_keep(self, i_edge_to_keep: Reference) -> 'EdgeFillet':
        self.edge_fillet.AddEdgeToKeep(i_edge_to_keep._com)
        return self

    def withdraw_edge_to_keep(self, i_edge_to_withdraw: Reference) -> 'EdgeFillet':
        self.edge_fillet.WithdrawEdgeToKeep(i_edge_to_withdraw._com)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'