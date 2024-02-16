from experience.system import AnyObject
from experience.inf_interfaces import Reference

class UserSurface(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     UserSurface
    """

    def __init__(self, com):
        super().__init__(com)
        self.user_surfaces = com

    def add_reference(self, i_support: Reference) -> 'UserSurface':
        self.user_surfaces.AddReference(i_support)
        return self

    def add_user_surface(self, i_support: 'UserSurface') -> 'UserSurface':
        self.user_surfaces.AdduserSurface(i_support)
        return self

    def __repr__(self):
        return f'UserSurface(name="{self.name()}")'
