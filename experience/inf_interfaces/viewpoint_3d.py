from experience.system import AnyObject

class Viewpoint3D(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Viewpoint3D
    """

    def __init__(self, com):
        super().__init__(com)
        self.viewpoint_3d = com

    def field_of_view(self, value: float = None) -> float:
        if value is not None:
            self.viewpoint_3d.FieldOfView = value
            return self
        return self.viewpoint_3d.FieldOfView

    def focus_distance(self, value: float = None) -> float:
        if value is not None:
            self.viewpoint_3d.FocusDistance = value
            return self
        return self.viewpoint_3d.FocusDistance

    def projection_mode(self, value: int = None) -> int:
        if value is not None:
            self.viewpoint_3d.ProjectionMode = value
            return self
        return self.viewpoint_3d.ProjectionMode

    def zoom(self, value: float = None) -> float:
        if value is not None:
            self.viewpoint_3d.Zoom = value
            return self
        return self.viewpoint_3d.Zoom

    def get_origin(self) -> tuple:
        vba_function_name = 'get_origin'
        vba_code = """
        Public Function get_origin(viewpoint_3d)
            Dim origin (2)
            viewpoint_3d.GetOrigin origin
            get_origin = origin
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_sight_direction(self) -> tuple:
        vba_function_name = 'get_sight_direction'
        vba_code = """
        Public Function get_sight_direction(viewpoint_3d)
            Dim oSight (2)
            viewpoint_3d.GetSightDirection oSight
            get_sight_direction = oSight
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_up_direction(self) -> tuple:
        vba_function_name = 'get_up_direction'
        vba_code = """
        Public Function get_up_direction(viewpoint_3d)
            Dim oUp (2)
            viewpoint_3d.GetUpDirection oUp
            get_up_direction = oUp
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_origin(self, origin: tuple) -> None:
        return self.viewpoint_3d.PutOrigin(origin)

    def put_sight_direction(self, o_sight: tuple) -> None:
        return self.viewpoint_3d.PutSightDirection(o_sight)

    def put_up_direction(self, o_up: tuple) -> None:
        return self.viewpoint_3d.PutUpDirection(o_up)

    def __repr__(self):
        return f'ViewPoint3D(name="{self.name}")'
