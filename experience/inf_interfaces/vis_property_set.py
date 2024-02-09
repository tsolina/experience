from typing import TYPE_CHECKING

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.inf_interfaces import Selection

class VisPropertySet(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.vis_property_set = com
        self._parent = None

    def get_layer(self) -> tuple:
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

        return self.application.system_service.evaluate(vba_code, 1, vba_function_name, [self.vis_property_set])

    def get_pick(self) -> tuple:
        return self.vis_property_set.GetPick()

    def get_real_color(self) -> tuple:
        return self.vis_property_set.GetRealColor()

    def get_real_inheritance(self, i_property_type: int) -> tuple:
        return self.vis_property_set.GetRealInheritance(i_property_type)

    def get_real_line_type(self) -> int:
        return self.vis_property_set.GetRealLineType()

    def get_real_opacity(self) -> int:
        return self.vis_property_set.GetRealOpacity()

    def get_real_width(self) -> tuple:
        return self.vis_property_set.GetRealWidth()

    def get_show(self) -> int:
        return self.vis_property_set.GetShow()[1]

    def get_symbol_type(self) -> int:
        return self.vis_property_set.GetSymbolType()

    def get_visible_color(self) -> int:
        return self.vis_property_set.GetVisibleColor()

    def get_visible_inheritance(self, i_property_type: int) -> tuple:
        return self.vis_property_set.GetVisibleInheritance(i_property_type)

    def get_visible_line_type(self) -> tuple:
        return self.vis_property_set.GetVisibleLineType()

    def get_visible_opacity(self) -> tuple:
        return self.vis_property_set.GetVisibleOpacity()

    def get_visible_width(self) -> tuple:
        return self.vis_property_set.GetVisibleWidth()

    def set_layer(self, i_layer_type: int, i_layer_value: int) -> 'VisPropertySet':
        self.vis_property_set.SetLayer(i_layer_type, i_layer_value)
        return self

    def set_pick(self, i_pick: int) -> 'VisPropertySet':
        self.vis_property_set.SetPick(i_pick)
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

    def set_show(self, i_show: int) -> 'VisPropertySet':
        self.vis_property_set.SetShow(i_show)
        return self

    def set_symbol_type(self, i_symbol_type: int) -> 'VisPropertySet':
        self.vis_property_set.SetSymbolType(i_symbol_type)
        return self
    
    def set_parent(self, value: "Selection") -> 'VisPropertySet':
        self._parent = value
        return self
    
    def parent(self) -> 'Selection':
        return self._parent

    def __repr__(self):
        return f'VisPropertySet(name="{self.name}")'
