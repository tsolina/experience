from typing import Union, Optional, TYPE_CHECKING

from experience.cat_part_interfaces import SurfaceBasedShape

class CloseSurface(SurfaceBasedShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         CATPartIDLItf.SurfaceBasedShape
                |                             CloseSurface

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.close_surface = com_object

    def __repr__(self):
        return f'CloseSurface(name="{self.name()}")'