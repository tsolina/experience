from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference, References
from experience.cat_part_interfaces import EdgeFillet

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class VarRadEdgeFillet(EdgeFillet):
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
                |                                     VarRadEdgeFillet
    """

    def __init__(self, com):
        super().__init__(com)
        self.var_rad_edge_fillet = com

    def bitangency_type(self, value: int = None) -> Union['EdgeFillet', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.var_rad_edge_fillet.BitangencyType = value
            return self
        return self.var_rad_edge_fillet.BitangencyType

    def edges_to_fillet(self) -> References:
        return References(self.var_rad_edge_fillet.EdgesToFillet)

    def fillet_spine(self, value: Reference = None) -> Union['EdgeFillet', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.var_rad_edge_fillet.FilletSpine = value._com
            return self
        return Reference(self.var_rad_edge_fillet.FilletSpine)

    def fillet_variation(self, value: int = None) -> Union['EdgeFillet', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.var_rad_edge_fillet.FilletVariation = value
            return self
        return self.var_rad_edge_fillet.FilletVariation

    def imposed_vertices(self) -> References:
        return References(self.var_rad_edge_fillet.ImposedVertices)
    
    def sharp_edge_removal_mode(self, value: int = None) -> Union['EdgeFillet', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.var_rad_edge_fillet.SharpEdgeRemovalMode = value
            return self
        return self.var_rad_edge_fillet.SharpEdgeRemovalMode    

    def add_edge_to_fillet(self, i_edge: Reference, i_radius: float) -> 'EdgeFillet':
        self.var_rad_edge_fillet.AddEdgeToFillet(i_edge._com, i_radius)
        return self

    def add_imposed_vertex(self, i_vertex: Reference, i_radius: float) -> 'EdgeFillet':
        self.var_rad_edge_fillet.AddImposedVertex(i_vertex._com, i_radius)
        return self

    def imposed_vertex_radius(self, i_imposed_vertex: Reference) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.var_rad_edge_fillet.ImposedVertexRadius(i_imposed_vertex._com))

    def switch_to_const_fillet_type(self) -> int:
        return self.var_rad_edge_fillet.SwitchToConstFilletType()

    def withdraw_edge_to_fillet(self, i_edge: Reference) -> 'EdgeFillet':
        self.var_rad_edge_fillet.WithdrawEdgeToFillet(i_edge._com)
        return self

    def withdraw_imposed_vertex(self, i_vertex: Reference) -> 'EdgeFillet':
        self.var_rad_edge_fillet.WithdrawImposedVertex(i_vertex._com)
        return self

    def __repr__(self):
        return f'VarRadEdgeFillet(name="{self.name()}")'