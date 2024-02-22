from typing import TYPE_CHECKING
from experience.inf_interfaces.inf_types import *
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.inf_interfaces import Selection

class VisPropertySet(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.vis_property_set = com
        self._parent = None

    def get_layer(self) -> tuple[CatVisPropertyStatus, CatVisLayerType, int]:
        """
        returning tuple(CatVisProperyStatus, layertype, layer)
        """

        vba_function_name = "get_layer"
        vba_code = f"""
        Public Function {vba_function_name}(VisPropertySet)
            Dim layer, layertype As CatVisLayerType, rVal as CatVisPropertyStatus
            layer = clng(0)
            rVal = VisPropertySet.GetLayer(layertype, layer)
            {vba_function_name} = Array(rVal, layertype, layer)
        End Function
        """

        r_val = self.application().system_service().evaluate(vba_code, 1, vba_function_name, [self.vis_property_set])
        return (CatVisPropertyStatus.item(r_val[0]), CatVisLayerType.item(r_val[1]), r_val[2])
        #return self.application().system_service().evaluate(vba_code, 1, vba_function_name, [self.vis_property_set])

    def get_pick(self) -> tuple[CatVisPropertyStatus, CatVisPropertyPick]:
        r_val = self.vis_property_set.GetPick()
        return (CatVisPropertyStatus.item(r_val[0]), CatVisPropertyPick.item(r_val[1]))

    def get_real_color(self) -> tuple[CatVisPropertyStatus, int, int, int]:
        r_val = self.vis_property_set.GetRealColor()
        return (CatVisPropertyStatus.item(r_val[0]), r_val[1], r_val[2], r_val[3])

    def get_real_inheritance(self, i_property_type: CatVisPropertyType) -> tuple[CatVisPropertyStatus, int]:
        r_val = self.vis_property_set.GetRealInheritance(int(i_property_type))
        return (CatVisPropertyStatus.item(r_val[0]), r_val[1])

    def get_real_line_type(self) -> tuple[CatVisPropertyStatus, int]:
        r_val = self.vis_property_set.GetRealLineType()
        return (CatVisPropertyStatus.item(r_val[0]), r_val[1])

    def get_real_opacity(self) -> tuple[CatVisPropertyStatus, int]:
        r_val = self.vis_property_set.GetRealOpacity()
        return (CatVisPropertyStatus.item(r_val[0]), r_val[1])

    def get_real_width(self) -> tuple[CatVisPropertyStatus, int]:
        r_val = self.vis_property_set.GetRealWidth()
        return (CatVisPropertyStatus.item(r_val[0]), r_val[1])

    def get_show(self) -> tuple[CatVisPropertyStatus, CatVisPropertyShow]:
        r_val = self.vis_property_set.GetShow()
        return (CatVisPropertyStatus.item(r_val[0]), CatVisPropertyShow(r_val[1]))

    def get_symbol_type(self) -> tuple[CatVisPropertyStatus, InfSymbolType]:
        r_val = self.vis_property_set.GetSymbolType()
        return (CatVisPropertyStatus.item(r_val[0]), InfSymbolType.item(r_val[1]))

    def get_visible_color(self) -> tuple[CatVisPropertyStatus, int, int, int]:
        r_val = self.vis_property_set.GetVisibleColor()
        return (CatVisPropertyStatus.item(r_val[0]), r_val[1], r_val[2], r_val[3])

    def get_visible_inheritance(self, i_property_type: CatVisPropertyType) -> tuple[CatVisPropertyStatus, int]:
        r_val = self.vis_property_set.GetVisibleInheritance(int(i_property_type))
        return (CatVisPropertyStatus.item(r_val[0]), r_val[1])

    def get_visible_line_type(self) -> tuple[CatVisPropertyStatus, int]:
        r_val = self.vis_property_set.GetVisibleLineType()
        return (CatVisPropertyStatus.item(r_val[0]), r_val[1])

    def get_visible_opacity(self) -> tuple[CatVisPropertyStatus, int]:
        r_val = self.vis_property_set.GetVisibleOpacity()
        return (CatVisPropertyStatus.item(r_val[0]), r_val[1])

    def get_visible_width(self) -> tuple[CatVisPropertyStatus, int]:
        r_val = self.vis_property_set.GetVisibleWidth()
        return (CatVisPropertyStatus.item(r_val[0]), r_val[1])

    def set_layer(self, i_layer_type: CatVisLayerType, i_layer_value: int) -> 'VisPropertySet':
        self.vis_property_set.SetLayer(i_layer_type, int(i_layer_value))
        return self

    def set_pick(self, i_pick: CatVisPropertyPick) -> 'VisPropertySet':
        self.vis_property_set.SetPick(int(i_pick))
        return self

    def set_real_color(self, i_red: int, i_green: int, i_blue: int, i_inheritance: int) -> 'VisPropertySet':
        self.vis_property_set.SetRealColor(i_red, i_green, i_blue, i_inheritance)
        return self

    def set_real_line_type(self, i_line_type: int, i_inheritance: int) -> 'VisPropertySet':
        self.vis_property_set.SetRealLineType(i_line_type, i_inheritance)
        return self

    def set_real_opacity(self, i_opacity: int, i_inheritance: int) -> 'VisPropertySet':
        self.vis_property_set.SetRealOpacity(i_opacity, i_inheritance)
        return self

    def set_real_width(self, i_line_width: int, i_inheritance: int) -> 'VisPropertySet':
        self.vis_property_set.SetRealWidth(i_line_width, i_inheritance)
        return self

    def set_show(self, i_show: CatVisPropertyShow) -> 'VisPropertySet':
        self.vis_property_set.SetShow(int(i_show))
        return self

    def set_symbol_type(self, i_symbol_type: InfSymbolType) -> 'VisPropertySet':
        self.vis_property_set.SetSymbolType(int(i_symbol_type))
        return self
    
    def set_visible_color(self, i_red: int, i_green: int, i_blue: int, i_inheritance: int) -> 'VisPropertySet':
        self.vis_property_set.SetVisibleColor(i_red, i_green, i_blue, i_inheritance)
        return self
    
    def set_visible_line_type(self, i_line_type: int, i_inheritance: int) -> 'VisPropertySet':
        self.vis_property_set.SetVisibleLineType(i_line_type, i_inheritance)
        return self
    
    def set_visible_opacity(self, i_opacity: int, i_inheritance: int) -> 'VisPropertySet':
        self.vis_property_set.SetVisibleOpacity(i_opacity, i_inheritance)
        return self
    
    def set_visible_width(self, i_line_width: int, i_inheritance: int) -> 'VisPropertySet':
        self.vis_property_set.SetVisibleWidth(i_line_width, i_inheritance)
        return self
    
    def set_parent(self, value: "Selection") -> 'VisPropertySet':
        self._parent = value
        return self
    
    def parent(self) -> 'Selection':
        return self._parent

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'