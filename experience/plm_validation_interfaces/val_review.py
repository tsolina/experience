from typing import TYPE_CHECKING
from experience.plm_modeler_base_interfaces.plm_entity import PLMEntity
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.plm_validation_interfaces import VALReviews, Markers, Slides

class VALReview(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         VALReview
    """

    def __init__(self, com):
        super().__init__(com)
        self.val_review = com

    def reviews(self) -> 'VALReviews':
        from experience.plm_validation_interfaces import VALReviews
        return VALReviews(self.val_review.Reviews)
    
    def get_factory(self, i_type: str) -> AnyObject:
        return AnyObject(self.val_review.GetFactory(i_type))
    
    def get_markers(self) -> 'Markers':
        from experience.plm_validation_interfaces import Markers
        return Markers(self.val_review.GetFactory('Markers'))

    def get_slides(self) -> 'Slides':
        from experience.plm_validation_interfaces import Slides
        return Slides(self.val_review.GetFactory('Slides'))