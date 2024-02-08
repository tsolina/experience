from experience.system.any_object import AnyObject

class SystemConfiguration(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.system_configuration = com

    def operating_system(self) -> str:
        return self.system_configuration.OperatingSystem

    def product_count(self) -> int:
        return self.system_configuration.ProductCount

    def release(self) -> int:
        return self.system_configuration.Release

    def service_pack(self) -> int:
        return self.system_configuration.ServicePack

    def version(self) -> int:
        return self.system_configuration.version

    def get_product_names(self, io_product_names: tuple):
        return self.system_configuration.GetProductNames(io_product_names)

    def is_product_authorized(self, i_product_name) -> bool:
        return self.system_configuration.IsProductAuthorized(i_product_name)

    def __repr__(self):
        return f'SystemConfiguration(name="{self.name}")'
