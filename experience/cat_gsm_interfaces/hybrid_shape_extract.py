from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeExtract(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeExtract
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_extract = com

    def angular_threshold(self, value: float = None) -> Union['HybridShapeExtract', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract.AngularThreshold = value
            return self
        return self.hybrid_shape_extract.AngularThreshold

    def angular_threshold_activity(self, value: bool = None) -> Union['HybridShapeExtract', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract.AngularThresholdActivity = value
            return self
        return self.hybrid_shape_extract.AngularThresholdActivity

    def complementary_extract(self, value: bool = None) -> Union['HybridShapeExtract', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract.ComplementaryExtract = value
            return self
        return self.hybrid_shape_extract.ComplementaryExtract

    def curvature_threshold(self, value: float = None) -> Union['HybridShapeExtract', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract.CurvatureThreshold = value
            return self
        return self.hybrid_shape_extract.CurvatureThreshold

    def curvature_threshold_activity(self, value: bool = None) -> Union['HybridShapeExtract', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract.CurvatureThresholdActivity = value
            return self
        return self.hybrid_shape_extract.CurvatureThresholdActivity

    def distance_threshold(self, value: float = None) -> Union['HybridShapeExtract', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract.DistanceThreshold = value
            return self
        return self.hybrid_shape_extract.DistanceThreshold

    def distance_threshold_activity(self, value: bool = None) -> Union['HybridShapeExtract', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract.DistanceThresholdActivity = value
            return self
        return self.hybrid_shape_extract.DistanceThresholdActivity

    def elem(self, value: Reference = None) -> Union['HybridShapeExtract', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract.Elem = value._com
            return self
        return Reference(self.hybrid_shape_extract.Elem)

    def is_federated(self, value: bool = None) -> Union['HybridShapeExtract', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract.IsFederated = value
            return self
        return self.hybrid_shape_extract.IsFederated

    def propagation_type(self, value: int = None) -> Union['HybridShapeExtract', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract.PropagationType = value
            return self
        return self.hybrid_shape_extract.PropagationType

    def support(self, value: Reference = None) -> Union['HybridShapeExtract', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract.Support = value._com
            return self
        return Reference(self.hybrid_shape_extract.Support)

    def __repr__(self):
        return f'HybridShapeExtract(name="{ self.name }")'