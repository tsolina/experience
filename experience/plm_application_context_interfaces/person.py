from experience.system import AnyObject

class Person(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Person
    """

    def __init__(self, com):
        super().__init__(com)
        self.person = com

    def collaborative_space_id(self) -> str:
        return self.person.CollaborativeSpaceID
    
    def organization_id(self) -> str:
        return self.person.OrganizationID
    
    def person_id(self) -> str:
        return self.person.PersonID
    
    def role_id(self) -> str:
        return self.person.RoleID