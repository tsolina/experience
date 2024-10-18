from typing import Union, TYPE_CHECKING

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces.vpm_reference import VPMReference

class VOCServices(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     VOCServices
    """

    def __init__(self, com):
        super().__init__(com)
        self.voc_services = com

    def compute_3d_cut(self, i_products_to_treat: list, i_product_reference: 'VPMReference', i_box_extremities: list, i_cut_type: int, i_border_types: int) -> 'VOCServices':
        self.voc_services.Compute3DCut(i_products_to_treat, i_product_reference._com, i_box_extremities, i_cut_type, i_border_types)
        return self
    
    def compute_a_silhouette(self, i_products_to_treat: list, i_product_reference: 'VPMReference', i_list_of_view_points: list, 
                             i_silhouette_acc: float, i_perform_simplification: bool, i_accuracy_for_simplification: float) -> 'VOCServices':
        self.voc_services.ComputeASilhouette(i_products_to_treat, i_product_reference._com, i_list_of_view_points, i_silhouette_acc, i_perform_simplification, i_accuracy_for_simplification)
        return self
    
    def compute_a_swept_volume(self, i_swept_able: AnyObject, i_products_to_treat: list, i_product_reference: 'VPMReference', i_filtering_parameter: float, 
                               i_perform_silhouete: bool, i_silhouette_accuracy: float, i_wrapping_grain: float, i_envelope_type: int,
                               i_offset_ratio: float, i_cubic: bool, i_perform_simplification: bool, i_simplification_accuracy: float) -> 'VOCServices':
        self.voc_services.ComputeASweptVolume(i_swept_able._com, i_products_to_treat, i_product_reference._com, i_filtering_parameter,
                                              i_perform_silhouete, i_silhouette_accuracy, i_wrapping_grain, i_envelope_type,
                                              i_offset_ratio, i_cubic, i_perform_simplification, i_simplification_accuracy)
        return self
    
    def compute_a_thickness(self, i_products_to_treat: list, i_product_reference: 'VPMReference', i_offset_value1: float, i_offset_value2: float,
                            i_use_constraints: bool, i_constraints: list) -> 'VOCServices':
        self.voc_services.ComputeAThickness(i_products_to_treat, i_product_reference, i_offset_value1, i_offset_value2, i_use_constraints, i_constraints)
        return self
    
    def compute_a_vibration_volume(self, i_products_to_treat: list, i_product_reference: 'VPMReference', i_file_path: str, i_accuracy: float,
                                   i_envelope_type: int, i_perform_simplification: bool, i_simplification_accuracy: float) -> 'VOCServices':
        self.voc_services.ComputeAVibrationVolume(self, i_products_to_treat, i_product_reference._com, i_file_path, i_accuracy,
                                                  i_envelope_type, i_perform_simplification, i_simplification_accuracy)
        return self
        
    def compute_a_vibration_volume_from_track(self, i_swept_able: AnyObject, i_products_to_treat: list, i_product_reference: 'VPMReference', i_accuracy: float,
                                              i_envelope_type: int, i_perform_simplification: bool, i_simplification_accuracy: float) -> 'VOCServices':
        self.voc_services.ComputeAVibrationVolumeFromTrack(i_swept_able._com, i_products_to_treat, i_product_reference._com, i_accuracy, i_envelope_type,
                                                           i_perform_simplification, i_simplification_accuracy)
        return self
    
    def compute_a_wrapping(self, i_products_to_treat: list, i_product_reference: 'VPMReference', i_wrapping_grain: float, i_envelope_type: int, i_offset_ratio: float,
                           i_cubic: bool, i_perform_simplification: bool, i_simplification_accuracy: float) -> 'VOCServices':
        self.voc_services.ComputeAWrapping(i_products_to_treat, i_product_reference._com, i_wrapping_grain, i_envelope_type, i_offset_ratio, i_cubic,
                                           i_perform_simplification, i_simplification_accuracy)
        return self
    
    def compute_an_offset(self, i_products_to_treat: list, i_product_reference: 'VPMReference', i_offset_value: float, i_use_constraings: bool, i_constraints: list) -> 'VOCServices':
        self.voc_services.ComputeAnOffset(i_products_to_treat, i_product_reference._com, i_offset_value, i_use_constraings, i_constraints)
        return self
    
    def create_free_space_in_box_area(self, i_products_to_treat: list, i_product_reference: 'VPMReference', i_free_space_grain: float, i_box_extremities: list) -> 'VOCServices':
        self.voc_services.CreateFreeSpaceInBoxArea(i_products_to_treat, i_product_reference._com, i_free_space_grain, i_box_extremities)
        return self
    
    def create_free_space_in_closed_area(self, i_products_to_treat: list, i_product_reference: 'VPMReference', i_free_space_grain: float, i_box_extremities: list,
                                         i_init_point: list) -> 'VOCServices':
        self.voc_services.CreateFreeSpaceInClosedArea(i_products_to_treat, i_product_reference._com, i_free_space_grain, i_box_extremities, i_init_point)
        return self
    
    def create_offset(self, i_products_to_treat: list, i_product_reference: 'VPMReference', i_offset_value: float) -> 'VOCServices':
        self.voc_services.CreateOffset(i_products_to_treat, i_product_reference._com, i_offset_value)
        return self
    
    def create_offset_along_fixed_vectors(self, i_products_to_treat: list, i_product_reference: 'VPMReference', i_vectors: list, i_offset_values: list) -> 'VOCServices':
        self.voc_services.CreateOffsetAlongFixedVectors(i_products_to_treat, i_product_reference._com, i_vectors, i_offset_values)
        return self
    
    def create_simplification(self, i_products_to_treat: list, i_product_reference: 'VPMReference', i_simplification_accuracy: float) -> 'VOCServices':
        self.voc_services.CreateSimplification(i_products_to_treat, i_product_reference._com, i_simplification_accuracy)
        return self
    
    def create_swept_volumes(self, i_swept_able: AnyObject, i_products_to_treat: list, i_product_reference: 'VPMReference', i_filtering_parameter: float) -> 'VOCServices':
        self.voc_services.CreateSweptVolumes(i_swept_able._com, i_products_to_treat, i_product_reference._com, i_filtering_parameter)
        return self
    
    def create_thickness(self, i_products_to_treat: list, i_product_reference: 'VPMReference', i_offset_value1: float, i_offset_value2: float) -> 'VOCServices':
        self.voc_services.CreateThickness(i_products_to_treat, i_product_reference._com, i_offset_value1, i_offset_value2)
        return self
    
    def create_wrapping(self, i_products_to_treat: list, i_product_reference: 'VPMReference', i_wrapping_grain: float, i_perform_simplification: bool,
                        i_simplification_accuracy: float) -> 'VOCServices':
        self.voc_services.CreateWrapping(i_products_to_treat, i_product_reference._com, i_wrapping_grain, i_perform_simplification, i_simplification_accuracy)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'