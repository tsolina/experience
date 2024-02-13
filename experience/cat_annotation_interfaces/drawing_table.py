from experience.system import AnyObject
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from experience.cat_annotation_interfaces import DrawingText, DrawingLeaders, DrawingTextProperties

class DrawingTable(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingTable
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_table = com

    def anchor_point(self, value: int = None) -> Union['DrawingTable', int]:
        if value is not None:
            self.drawing_table.AnchorPoint = value
            return self
        return self.drawing_table.AnchorPoint

    def angle(self, value: float = None) -> Union['DrawingTable', float]:
        if value is not None:
            self.drawing_table.Angle = value
            return self
        return self.drawing_table.Angle

    def compute_mode(self, value: int = None) -> Union['DrawingTable', int]:
        if value is not None:
            self.drawing_table.ComputeMode = value
            return self
        return self.drawing_table.ComputeMode

    def leaders(self) -> 'DrawingLeaders':
        from experience.cat_annotation_interfaces import DrawingLeaders
        return DrawingLeaders(self.drawing_table.Leaders)

    def number_of_columns(self) -> int:
        return self.drawing_table.NumberOfColumns

    def number_of_rows(self) -> int:
        return self.drawing_table.NumberOfRows

    def orientation_reference(self, value: int = None) -> Union['DrawingTable', int]:
        if value is not None:
            self.drawing_table.OrientationReference = value
            return self
        return self.drawing_table.OrientationReference

    def text_properties(self) -> 'DrawingTextProperties':
        from experience.cat_annotation_interfaces import DrawingTextProperties
        return DrawingTextProperties(self.drawing_table.TextProperties)

    def x(self, value: float = None) -> Union['DrawingTable', float]:
        if value is not None:
            self.drawing_table.x = value
            return self
        return self.drawing_table.x

    def y(self, value: float = None) -> Union['DrawingTable', float]:
        if value is not None:
            self.drawing_table.y = value
            return self
        return self.drawing_table.y

    def add_column(self, i_col: int) -> 'DrawingTable':
        self.drawing_table.AddColumn(i_col)
        return self

    def add_row(self, i_row: int) -> 'DrawingTable':
        self.drawing_table.AddRow(i_row)
        return self

    def get_cell_alignment(self, i_row: int, i_col: int) -> int:
        return self.drawing_table.GetCellAlignment(i_row, i_col)

    def get_cell_border_type(self, i_row: int, i_col: int) -> int:
        return self.drawing_table.GetCellBorderType(i_row, i_col)

    def get_cell_name(self, i_row: int, i_col: int) -> str:
        return self.drawing_table.GetCellName(i_row, i_col)

    def get_cell_object(self, i_row: int, i_col: int) -> 'DrawingText':
        from experience.cat_annotation_interfaces import DrawingText
        return DrawingText(self.drawing_table.GetCellObject(i_row, i_col))

    def get_cell_string(self, i_row: int, i_col: int) -> str:
        return self.drawing_table.GetCellString(i_row, i_col)

    def get_cells_merge(self) -> tuple:
        return self._get_safe_array(self.drawing_table, "GetCellsMerge", self.number_of_columns() * self.number_of_rows() -1)
        #return self.drawing_table.GetCellsMerge()

    def get_column_size(self, i_col: int) -> float:
        return self.drawing_table.GetColumnSize(i_col)

    def get_merge_infos(self, i_row: int, i_col: int) -> tuple[int, int, int, int]:
        return self.drawing_table.GetMergeInfos(i_row, i_col)

    def get_row_size(self, i_row: int) -> float:
        return self.drawing_table.GetRowSize(i_row)

    def invert_mode(self, i_mode: int) -> 'DrawingTable':
        self.drawing_table.InvertMode(i_mode)
        return self

    def merge_cells(self, i_first_row, i_first_col, i_nb_row_merge, i_nb_col_merge) -> 'DrawingTable':
        self.drawing_table.MergeCells(i_first_row, i_first_col, i_nb_row_merge, i_nb_col_merge)
        return self

    def move(self, i_delta_x: float, i_delta_y: float) -> 'DrawingTable':
        self.drawing_table.Move(i_delta_x, i_delta_y)
        return self

    def remove_column(self, i_col: int) -> 'DrawingTable':
        self.drawing_table.RemoveColumn(i_col)
        return self

    def remove_row(self, i_row) -> 'DrawingTable':
        self.drawing_table.RemoveRow(i_row)
        return self

    def rotate(self, i_delta_angle: float) -> 'DrawingTable':
        self.drawing_table.Rotate(i_delta_angle)
        return self

    def set_cell_alignment(self, i_row: int, i_col: int, i_align: int) -> 'DrawingTable':
        self.drawing_table.SetCellAlignment(i_row, i_col, i_align)
        return self

    def set_cell_border_type(self, i_row: int, i_col: int, i_type: int) -> 'DrawingTable':
        self.drawing_table.SetCellBorderType(i_row, i_col, i_type)
        return self

    def set_cell_image(self, i_row: int, i_col: int, i_path: str) -> 'DrawingTable':
        self.drawing_table.SetCellImage(i_row, i_col, i_path)
        return self

    def set_cell_name(self, i_row: int, i_col: int, i_name: str) -> 'DrawingTable':
        self.drawing_table.SetCellName(i_row, i_col, i_name)
        return self

    def set_cell_object(self, i_row: int, i_col: int, i_text: 'DrawingText') -> 'DrawingTable':
        self.drawing_table.SetCellObject(i_row, i_col, i_text._com)
        return self

    def set_cell_string(self, i_row: int, i_col: int, i_string: str) -> 'DrawingTable':
        self.drawing_table.SetCellString(i_row, i_col, i_string)
        return self

    def set_column_size(self, i_col: int, i_col_size: float) -> 'DrawingTable':
        self.drawing_table.SetColumnSize(i_col, i_col_size)
        return self

    def set_row_size(self, i_row: int, i_row_size: float) -> 'DrawingTable':
        self.drawing_table.SetRowSize(i_row, i_row_size)
        return self

    def un_merge_cells(self, i_row: int, i_col: int) -> 'DrawingTable':
        self.drawing_table.UnMergeCells(i_row, i_col)
        return self

    def __repr__(self):
        return f'DrawingTable(name="{self.name()}")'
