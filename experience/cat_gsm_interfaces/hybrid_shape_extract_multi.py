from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeExtractMulti(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeExtractMulti
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_extract_multi = com

    def add_constraint(self, i_constraint: Reference, i_type: int, i_complementaire: bool, i_is_federated: bool, i_crvtre_thsld: float, i_pos: int) -> 'HybridShapeExtractMulti':
        return self.hybrid_shape_extract_multi.AddConstraint(i_constraint._com, i_type, i_complementaire, i_is_federated, i_crvtre_thsld, i_pos)
        return self

    def add_constraint_tolerant(self, i_constraint: Reference, i_type: int, i_complementaire: bool,
                                i_is_federated: bool, i_distre_thsld: float, i_angtre_thsld: float,
                                i_crvtre_thsld: float, i_pos: int) -> 'HybridShapeExtractMulti':
        self.hybrid_shape_extract_multi.AddConstraintTolerant(i_constraint._com, i_type, i_complementaire,
                                                                     i_is_federated, i_distre_thsld, i_angtre_thsld,
                                                                     i_crvtre_thsld, i_pos)
        return self

    def get_list_of_constraints(self) -> tuple:
        ### need working vba example to make it work ###
        return self.hybrid_shape_extract_multi.GetListOfConstraints()

    def get_nb_constraints(self) -> int:
        return self.hybrid_shape_extract_multi.GetNbConstraints()

    def remove_element(self, i_position: int) -> 'HybridShapeExtractMulti':
        self.hybrid_shape_extract_multi.RemoveElement(i_position)
        return self

    def replace_element(self, i_extract_to_replace: Reference, i_new_extract: Reference, i_pos: int) -> 'HybridShapeExtractMulti':
        self.hybrid_shape_extract_multi.ReplaceElement(i_extract_to_replace._com, i_new_extract._com, i_pos)
        return self

    # def get_angular_threshold(self, i_pos: int) -> float:
    #     return self.hybrid_shape_extract_multi.GetAngularThreshold(i_pos)
    
    # def set_angular_threshold(self, i_pos: int, i_angtre_thsld: float) -> None:
    #     return self.hybrid_shape_extract_multi.SetAngularThreshold(i_pos, i_angtre_thsld)

    def angular_threshold(self, i_pos: int, value: float = None) -> Union['HybridShapeExtractMulti', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract_multi.SetAngularThreshold(i_pos, value)
            return self
        return self.hybrid_shape_extract_multi.GetAngularThreshold(i_pos)      

    # def get_angular_threshold_activity(self, i_pos: int) -> bool:
    #     return self.hybrid_shape_extract_multi.GetAngularThresholdActivity(i_pos)

    # def set_angular_threshold_activity(self, i_pos: int, i_angtre_thsld_activity: bool) -> None:
    #     return self.hybrid_shape_extract_multi.SetAngularThresholdActivity(i_pos, i_angtre_thsld_activity)
    
    def threshold_activity(self, i_pos: int, value: bool = None) -> Union['HybridShapeExtractMulti', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract_multi.SetAngularThresholdActivity(i_pos, value)
            return self
        return self.hybrid_shape_extract_multi.GetAngularThresholdActivity(i_pos)    

    # def get_complementary_extract_multi(self, i_pos: int) -> bool:
    #     return self.hybrid_shape_extract_multi.GetComplementaryExtractMulti(i_pos)

    # def set_complementary_extract_multi(self, i_pos: int, i_complementaire: bool) -> None:
    #     return self.hybrid_shape_extract_multi.SetComplementaryExtractMulti(i_pos, i_complementaire)
    
    def complementary_extract_multi(self, i_pos: int, value: bool = None) -> Union['HybridShapeExtractMulti', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract_multi.SetComplementaryExtractMulti(i_pos, value)
            return self
        return self.hybrid_shape_extract_multi.GetComplementaryExtractMulti(i_pos)    

    # def get_curvature_threshold(self, i_pos: int) -> float:
    #     return self.hybrid_shape_extract_multi.GetCurvatureThreshold(i_pos)

    # def set_curvature_threshold(self, i_pos: int, i_crvtre_thsld: float) -> None:
    #     return self.hybrid_shape_extract_multi.SetCurvatureThreshold(i_pos, i_crvtre_thsld)

    def curvature_threshold(self, i_pos: int, value: float = None) -> Union['HybridShapeExtractMulti', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract_multi.SetCurvatureThreshold(i_pos, value)
            return self
        return self.hybrid_shape_extract_multi.GetCurvatureThreshold(i_pos)     

    # def get_curvature_threshold_activity(self, i_pos: int) -> bool:
    #     return self.hybrid_shape_extract_multi.GetCurvatureThresholdActivity(i_pos)
    
    # def set_curvature_threshold_activity(self, i_pos: int, i_crvtre_thsld_activity: bool) -> None:
    #     return self.hybrid_shape_extract_multi.SetCurvatureThresholdActivity(i_pos, i_crvtre_thsld_activity)
    
    def curvature_threshold_activity(self, i_pos: int, value: bool = None) -> Union['HybridShapeExtractMulti', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract_multi.SetCurvatureThresholdActivity(i_pos, value)
            return self
        return self.hybrid_shape_extract_multi.GetCurvatureThresholdActivity(i_pos)    

    # def get_distance_threshold(self, i_pos: int) -> float:
    #     return self.hybrid_shape_extract_multi.GetDistanceThreshold(i_pos)

    # def set_distance_threshold(self, i_pos: int, i_distre_thsld: float) -> None:
    #     return self.hybrid_shape_extract_multi.SetDistanceThreshold(i_pos, i_distre_thsld)
    
    def distance_threshold(self, i_pos: int, value: float = None) -> Union['HybridShapeExtractMulti', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract_multi.SetDistanceThreshold(i_pos, value)
            return self
        return self.hybrid_shape_extract_multi.GetDistanceThreshold(i_pos)       

    # def get_distance_threshold_activity(self, i_pos: int) -> bool:
    #     return self.hybrid_shape_extract_multi.GetDistanceThresholdActivity(i_pos)

    # def set_distance_threshold_activity(self, i_pos: int, i_distre_thsld_activity: bool) -> None:
    #     return self.hybrid_shape_extract_multi.SetDistanceThresholdActivity(i_pos, i_distre_thsld_activity)
    
    def distance_threshold_activity(self, i_pos: int, value: bool = None) -> Union['HybridShapeExtractMulti', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract_multi.SetDistanceThresholdActivity(i_pos, value)
            return self
        return self.hybrid_shape_extract_multi.GetDistanceThresholdActivity(i_pos)    

    # def get_element(self, i_pos: int) -> Reference:
    #     return Reference(self.hybrid_shape_extract_multi.GetElement(i_pos))

    # def set_element(self, i_pos: int, i_elem: Reference) -> None:
    #     return self.hybrid_shape_extract_multi.SetElement(i_pos, i_elem.com)

    def element(self, i_pos: int, value: Reference = None) -> Union['HybridShapeExtractMulti', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract_multi.SetElement(i_pos, value._com)
            return self
        return Reference(self.hybrid_shape_extract_multi.GetElement(i_pos))    


    # def get_is_federated(self, i_pos: int) -> bool:
    #     return self.hybrid_shape_extract_multi.GetIsFederated(i_pos)
    
    # def set_is_federated(self, i_pos: int, i_is_federated: bool) -> None:
    #     return self.hybrid_shape_extract_multi.SetIsFederated(i_pos, i_is_federated)
    
    def is_federated(self, i_pos: int, value: bool = None) -> Union['HybridShapeExtractMulti', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract_multi.SetIsFederated(i_pos, value)
            return self
        return self.hybrid_shape_extract_multi.GetIsFederated(i_pos)

    # def get_propagation_type(self, i_pos: int) -> int:
    #     return self.hybrid_shape_extract_multi.GetPropagationType(i_pos)

    # def set_propagation_type(self, i_pos: int, i_type_propag: int) -> None:
    #     return self.hybrid_shape_extract_multi.SetPropagationType(i_pos, i_type_propag)

    def propagation_type(self, i_pos: int, value: int = None) -> Union['HybridShapeExtractMulti', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract_multi.SetPropagationType(i_pos, value)
            return self
        return self.hybrid_shape_extract_multi.GetPropagationType(i_pos)

    # def get_support(self, i_pos: int) -> Reference:
    #     return Reference(self.hybrid_shape_extract_multi.GetSupport(i_pos))

    # def set_support(self, i_pos: int, i_support: Reference) -> None:
    #     return self.hybrid_shape_extract_multi.SetSupport(i_pos, i_support.com)

    def support(self, i_pos: int, value: Reference = None) -> Union['HybridShapeExtractMulti', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extract_multi.SetSupport(i_pos, value._com)
            return self
        return Reference(self.hybrid_shape_extract_multi.GetSupport(i_pos))

    def __repr__(self):
        return f'HybridShapeExtractMulti(name="{self.name}")'