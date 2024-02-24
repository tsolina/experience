from typing import Iterator

from experience.system import AnyObject, Collection
from experience.inf_interfaces import Reference
from experience.types import cat_variant
from experience.cat_tps_interfaces import TPSView, UserSurface

class UserSurfaces(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     UserSurfaces
    """

    def __init__(self, com):
        super().__init__(com)
        self.user_surfaces = com
        self._child = UserSurface

    def generate(self, i_support: Reference) -> UserSurface:
        return self.user_surfaces.Generate(i_support)

    def item(self, i_index: cat_variant) -> UserSurface:
        return UserSurface(self.user_surfaces.Item(i_index))
    
    def make_user_surface_node(self, i_first_user_surf: UserSurface, i_second_user_surf: UserSurface) -> UserSurface:
        return self.user_surfaces.MakeUserSurfaceNode(i_first_user_surf, i_second_user_surf)
    
    def make_user_surface_node2(self, i_list_of_user_surfaces: tuple) -> UserSurface:
        return self.user_surfaces.MakeUserSurfaceNode2(i_list_of_user_surfaces)

    def __getitem__(self, n: int) -> UserSurface:
        if (n + 1) > self.count():
            raise StopIteration

        return UserSurface(self.user_surfaces.item(n + 1))

    def __iter__(self) -> Iterator[UserSurface]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))