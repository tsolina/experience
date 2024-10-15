from experience.system import AnyObject

class Inertia(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Inertia
    """

    def __init__(self, com):
        super().__init__(com)
        self.inertia = com

    def get_area(self) -> float:
        return self.inertia.GetArea()
    
    def get_cog_position(self) -> tuple[float, float, float]:
        '''
        cogX, cogY, cogZ
        '''
        return self._get_multi([self.inertia], ("Inertia", "GetCOGPosition"), ("Double", "Double", "Double"))

    def get_inertia_matrix(self) ->tuple[float, float, float, float, float, float, float, float, float]:
        '''
        ixxyz, iyxyz, izxyz
        '''
        return self._get_safe_array(self.inertia, "GetInertiaMatrix", 8)

    def get_mass(self) -> float:
        return self.inertia.GetMass()

    def get_principal_axis(self) ->tuple[float, float, float, float, float, float, float, float, float]:
        '''
        a123x, a123y, a123z
        '''
        return self._get_safe_array(self.inertia, "GetPrincipalAxes", 8)
    
    def get_principal_moments(self) -> tuple[float, float, float]:
        '''
        m1, m2, m3
        '''
        return self._get_safe_array(self.inertia, "GetPrincipalMoments", 2)
    
    def get_volume(self) -> float:
        return self.inertia.GetVolume()
    
    def only_main_body(self) -> 'Inertia':
        self.inertia.OnlyMainBody()
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'