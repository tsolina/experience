from typing import Union
from experience.exceptions import CATIAApplicationException
from experience.system import AnyObject

from experience.cat_annotation_interfaces.annotation_types import *

from experience.types.enum_item import EnumItem
class SymbolIndex(EnumItem):
    first_symbol = 1
    second_symbol = 2
    leader_symbol = 3

class DrawingDimLine(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingDimLine
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_dim_line = com

    def color(self, value: int = None) -> Union['DrawingDimLine', int]:
        if value is not None:
            self.drawing_dim_line.Color = value
            return self
        return self.drawing_dim_line.Color

    def dim_line_graph_rep(self, value: CatDimLineGraphRep = None) -> Union['DrawingDimLine', CatDimLineGraphRep]:
        if value is not None:
            self.drawing_dim_line.DimLineGraphRep = int(value)
            return self
        return CatDimLineGraphRep.item(self.drawing_dim_line.DimLineGraphRep)

    def dim_line_orientation(self, value: CatDimOrientation = None) -> Union['DrawingDimLine', CatDimOrientation]:
        if value is not None:
            self.drawing_dim_line.DimLineOrientation = int(value)
            return self
        return CatDimOrientation.item(self.drawing_dim_line.DimLineOrientation)

    def dim_line_reference(self, value: CatDimReference = None) -> Union['DrawingDimLine', CatDimReference]:
        if value is not None:
            self.drawing_dim_line.DimLineReference = int(value)
            return self
        return CatDimReference.item(self.drawing_dim_line.DimLineReference)

    def dim_line_rep(self) -> CatDimLineRep:
        return CatDimLineRep.item(self.drawing_dim_line.DimLineRep)

    def dim_line_type(self) -> int:
        return self.drawing_dim_line.DimLineType

    def thickness(self, value: float = None) -> Union['DrawingDimLine', float]:
        if value is not None:
            self.drawing_dim_line.Thickness = value
            return self
        return self.drawing_dim_line.Thickness

    def get_dim_line_dir(self) -> tuple[float, float]: #, o_dir_x: float, o_dir_y: float
        if self.dim_line_rep() == CatDimLineRep.catDimUserDefined:
            return self._get_multi([self.drawing_dim_line], ('DrawingDimLine', 'GetDimLineDir'), ('Double', 'Double'))
        else:
            raise CATIAApplicationException("This method can be used only if dim line is CatDimLineRep.catDimUserDefined")

    def get_geom_info(self) -> tuple: #, o_geom_infos: tuple
        """ - returning tuple with 6 undocumented items - """
        return self._get_safe_array(self.drawing_dim_line, "GetGeomInfo", 5)

    def get_symb_color(self, index: SymbolIndex) -> int:
        return self.drawing_dim_line.GetSymbColor(int(index))

    def get_symb_thickness(self, index: SymbolIndex) -> float:
        return self.drawing_dim_line.GetSymbThickness(int(index))

    def get_symb_type(self, index: SymbolIndex) -> CatDimSymbols:
        return CatDimSymbols.item(self.drawing_dim_line.GetSymbType(int(index)))

    def set_symb_color(self, index: SymbolIndex, i_color_symb: int) -> 'DrawingDimLine':
        self.drawing_dim_line.SetSymbColor(int(index), i_color_symb)
        return self

    def set_symb_thickness(self, index: SymbolIndex, i_thick_symb: float) -> 'DrawingDimLine':
        self.drawing_dim_line.SetSymbThickness(int(index), i_thick_symb)
        return self

    def set_symb_type(self, index: SymbolIndex, i_symb_type: CatDimSymbols) -> 'DrawingDimLine':
        self.drawing_dim_line.SetSymbType(int(index), int(i_symb_type))
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
