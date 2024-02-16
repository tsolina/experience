from experience.mecmod_interfaces import Factory
from experience.system import AnyObject

class InstanceFactory(Factory):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Factory
                |                         InstanceFactory
    """

    def __init__(self, com):
        super().__init__(com)
        self.instance_factory = com

    def instantiation_mode(self, i_instantation_mode_bstr: str) -> 'InstanceFactory':
        self.instance_factory.InstantiationMode = i_instantation_mode_bstr
        return self

    def add_instance(self, i_reference: AnyObject) -> AnyObject:
        return AnyObject(self.instance_factory.AddInstance(i_reference._com))

    def begin_instance_factory(self, i_name_of_reference: str, i_plm_external_id: str, iv_version: str) -> 'InstanceFactory':
        self.instance_factory.BeginInstanceFactory(i_name_of_reference, i_plm_external_id, iv_version)
        return self

    def begin_instantiate(self) -> 'InstanceFactory':
        self.instance_factory.BeginInstantiate()
        return self

    def end_instance_factory(self) -> 'InstanceFactory':
        self.instance_factory.EndInstanceFactory()
        return self

    def end_instantiate(self) -> 'InstanceFactory':
        self.instance_factory.EndInstantiate()
        return self

    def get_parameter(self, i_name: str) -> AnyObject:
        return AnyObject(self.instance_factory.GetParameter(i_name))

    def instantiate(self) -> AnyObject:
        return AnyObject(self.instance_factory.Instantiate())

    def put_input_data(self, i_name: str, i_input: AnyObject) -> 'InstanceFactory':
        self.instance_factory.PutInputData(i_name, i_input._com)
        return self

    def __repr__(self):
        return f'InstanceFactory(name="{self.name()}")'