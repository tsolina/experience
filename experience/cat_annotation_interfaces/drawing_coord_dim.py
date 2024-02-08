from experience.system import AnyObject
# from experience.cat_annotation_interfaces import DrawingTextProperties

class DrawingCoordDim(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 DrawingTextRange
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_coord_dim = com

    def angle(self, value: float = None) -> float:
        if value is not None:
            self.drawing_coord_dim.Angle = value
            return self
        return self.drawing_coord_dim.Angle

    def text_properties(self) -> 'DrawingCoordDim':
        from experience.cat_annotation_interfaces import DrawingTextProperties
        return DrawingTextProperties(self.drawing_coord_dim.DrawingTextProperties())

    def x(self, value: float = None) -> float:
        if value is not None:
            self.drawing_coord_dim.x = value
            return self
        return self.drawing_coord_dim.x

    def y(self, value: float = None) -> float:
        if value is not None:
            self.drawing_coord_dim.y = value
            return self
        return self.drawing_coord_dim.y

    def get_coord_values(self, o_type: int, o_x: float, o_y: float, o_z: float) -> tuple:
        return self.drawing_coord_dim.GetCoordValues(o_type, o_x, o_y, o_z)

    def __repr__(self):
        return f'DrawingCoordDim()'
