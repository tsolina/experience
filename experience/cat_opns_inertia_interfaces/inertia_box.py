from experience.system import AnyObject

class InertiaBox(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InertiaBox
    """

    def __init__(self, com):
        super().__init__(com)
        self.inertia_box = com

    def get_bounding_box(self) -> tuple[tuple[float, float, float], tuple[float, float, float]]:
        '''
        oBoundingBoxOrigin 
            The array of the bounding box origin: 
            oBoundingBoxOrigin(0) is the origin value with respect to the first principal axe of inertia 
            oBoundingBoxOrigin(1) is the origin value with respect to the second principal axe of inertia 
            oBoundingBoxOrigin(2) is the origin value with respect to the third principal axe of inertia 
        oBoundingBoxLengths 
            The array of the bounding box lengths: 
            oBoundingBoxLengths(0) is the length value with respect to the first principal axe of inertia 
            oBoundingBoxLengths(1) is the length value with respect to the second principal axe of inertia 
            oBoundingBoxLengths(2) is the length value with respect to the third principal axe of inertia 
        '''
        return self._get_safe_array_multi(self.inertia_box, "GetBoundingBox", [2, 2])

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'