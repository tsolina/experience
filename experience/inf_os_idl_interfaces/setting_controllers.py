from typing import Iterator

from experience.system.collection import Collection
from experience.system.setting_controller import SettingController

class SettingControllers(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SettingControllers

    """

    def __init__(self, com):
        super().__init__(com, child=SettingController)
        self.setting_controllers = com

    def item(self, i_index: str) -> SettingController:
        return SettingController(self.setting_controllers.Item(i_index))

    def __getitem__(self, n: int) -> SettingController:
        if (n + 1) > self.count():
            raise StopIteration

        return SettingController(self.setting_controllers.item(n + 1))

    def __iter__(self) -> Iterator[SettingController]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'