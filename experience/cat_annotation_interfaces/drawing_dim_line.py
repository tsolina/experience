from experience.system import AnyObject

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

    def color(self, value: int = None) -> int:
        if value is not None:
            self.drawing_dim_line.Color = value
            return self
        return self.drawing_dim_line.Color

    def dim_line_graph_rep(self, value: int = None) -> int:
        if value is not None:
            self.drawing_dim_line.DimLineGraphRep = value
            return self
        return self.drawing_dim_line.DimLineGraphRep

    def dim_line_orientation(self, value: int = None) -> int:
        if value is not None:
            self.drawing_dim_line.DimLineOrientation = value
            return self
        return self.drawing_dim_line.DimLineOrientation

    def dim_line_reference(self):
        if value is not None:
            self.drawing_dim_line.DimLineReference = value
            return self
        return self.drawing_dim_line.DimLineReference

    def dim_line_rep(self) -> int:
        return self.drawing_dim_line.DimLineRep

    def dim_line_type(self) -> int:
        return self.drawing_dim_line.DimLineType

    def thickness(self, value: float = None) -> float:
        if value is not None:
            self.drawing_dim_line.Thickness = value
            return self
        return self.drawing_dim_line.Thickness

    def get_dim_line_dir(self, o_dir_x: float, o_dir_y: float) -> float:
        return self.drawing_dim_line.GetDimLineDir(o_dir_x, o_dir_y)

    def get_geom_info(self, o_geom_infos: tuple) -> tuple:
        return self.drawing_dim_line.GetGeomInfo(o_geom_infos)

    def get_symb_color(self, index: int) -> int:
        return self.drawing_dim_line.GetSymbColor(index)

    def get_symb_thickness(self, index: int) -> float:
        return self.drawing_dim_line.GetSymbThickness(index)

    def get_symb_type(self, index: int) -> int:
        return self.drawing_dim_line.GetSymbType(index)

    def set_symb_color(self, index: int, i_color_symb: int) -> 'DrawingDimLine':
        self.drawing_dim_line.SetSymbColor(index, i_color_symb)
        return self

    def set_symb_thickness(self, index: int, i_thick_symb: float) -> 'DrawingDimLine':
        self.drawing_dim_line.SetSymbThickness(index, i_thick_symb)
        return self

    def set_symb_type(self, index: int, i_symb_type: int) -> 'DrawingDimLine':
        self.drawing_dim_line.SetSymbType(index, i_symb_type)
        return self

    def __repr__(self):
        return f'DrawingDimLine(name="{self.name}")'
