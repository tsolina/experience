from experience.mecmod_interfaces import Shape
from experience.system  import AnyObject

class ShapeInstance(Shape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         ShapeInstance
                | 
                | The interface to access a CATIAShapeInstance.
    
    """

    def __init__(self, com):
        super().__init__(com)
        self.shape_instance = com

    def inputs_count(self) -> int:
        return self.shape_instance.InputsCount

    def outputs_count(self) -> int:
        return self.shape_instance.OutputsCount

    def parameters_count(self) -> int:
        return self.shape_instance.ParametersCount

    def get_input(self, i_name: str) -> AnyObject:
        return AnyObject(self.shape_instance.GetInput(i_name))

    def get_input_data(self, i_name: str) -> AnyObject:
        return self.shape_instance.GetInputData(i_name)

    def get_input_data_from_position(self, i_position: int) -> AnyObject:
        return self.shape_instance.GetInputDataFromPosition(i_position)

    def get_input_from_position(self, i_position: int) -> AnyObject:
        return AnyObject(self.shape_instance.GetInputFromPosition(i_position))

    def get_output(self, i_name: str) -> AnyObject:
        return AnyObject(self.shape_instance.GetOutput(i_name))

    def get_output_from_position(self, i_position: int) -> AnyObject:
        return AnyObject(self.shape_instance.GetOutputFromPosition(i_position))

    def get_parameter(self, i_name: str) -> AnyObject:
        return AnyObject(self.shape_instance.GetParameter(i_name))

    def get_parameter_from_position(self, i_position: int) -> AnyObject:
        return AnyObject(self.shape_instance.GetParameterFromPosition(i_position))

    def put_input(self, i_name: str, i_input: AnyObject) -> 'ShapeInstance':
        self.shape_instance.PutInput(i_name, i_input._com)
        return self

    def put_input_data(self, i_name: str, i_input: AnyObject) -> 'ShapeInstance':
        self.shape_instance.PutInputData(i_name, i_input._com)
        return self