from experience.types.enum_string import EnumString

class PLMMarkerType(EnumString):
    Line2D = '2DLine'
    Pen2D = '2DPen'
    Circle2D = '2DCircle'
    Rectangle2D = '2DRectangle'
    Arrow2D = '2DArrow'
    Text2D = '2DText'
    Text3D = '3DText'
    Picture2D = '2DPicture'
    Picture3D = '3DPicture'
    Hyperlink2D = '2DHyperlink'
    Hyperlink3D = '3DHyperlink'
    Audio2D = '2DAudio'
    Audio3D = '3DAudio'

class PLMValidationType(EnumString):
    Product = 'Product'
    Simulation = 'Simulation'
    Image = 'Image'