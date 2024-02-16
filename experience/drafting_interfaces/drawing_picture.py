from experience.system import AnyObject

class DrawingPicture(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingPicture
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_picture = com

    def display_at_true_depth(self, value: bool = None) -> bool:
        if value is not None:
            self.drawing_picture.DisplayAtTrueDepth = value
            return self
        return self.drawing_picture.DisplayAtTrueDepth

    def picture_type(self) -> int:
        return self.drawing_picture.PictureType

    #top, right, bottom, left
    def crop(self, value: tuple[float, float, float, float] = None) -> 'DrawingPicture':
        if value is not None:
            self.crop_top(value[0]).crop_right(value[1]).crop_bottom(value[2]).crop_left(value[3])
            return self
        return (self.crop_top(), self.crop_right(), self.crop_bottom(), self.crop_left())

    def crop_bottom(self, value: float = None) -> float:
        if value is not None:
            self.drawing_picture.cropBottom = value
            return self
        return self.drawing_picture.cropBottom

    def crop_left(self, value: float = None) -> float:
        if value is not None:
            self.drawing_picture.cropLeft = value
            return self
        return self.drawing_picture.cropLeft

    def crop_right(self, value: float = None) -> float:
        if value is not None:
            self.drawing_picture.cropRight = value
            return self
        return self.drawing_picture.cropRight

    def crop_top(self, value: float = None) -> float:
        if value is not None:
            self.drawing_picture.cropTop = value
            return self
        return self.drawing_picture.cropTop

    def format(self, value: int = None) -> int:
        if value is not None:
            self.drawing_picture.format = value
            return self
        return self.drawing_picture.format

    def height(self, value: float = None) -> float:
        if value is not None:
            self.drawing_picture.height = value
            return self
        return self.drawing_picture.height

    def ratio_lock(self, value: float = None) -> bool:
        if value is not None:
            self.drawing_picture.ratioLock = value
            return self
        return self.drawing_picture.ratioLock

    def width(self, value: float = None) -> float:
        if value is not None:
            self.drawing_picture.width = value
            return self
        return self.drawing_picture.width

    def x(self, value: float = None) -> float:
        if value is not None:
            self.drawing_picture.x = value
            return self
        return self.drawing_picture.x

    def y(self, value: float = None) -> float:
        if value is not None:
            self.drawing_picture.y = value
            return self
        return self.drawing_picture.y

    def get_original_height(self) -> float:
        return self.drawing_picture.GetOriginalHeight()

    def get_original_width(self) -> float:
        return self.drawing_picture.GetOriginalWidth()

    def __repr__(self):
        return f'DrawingPicture(name="{self.name()}")'
