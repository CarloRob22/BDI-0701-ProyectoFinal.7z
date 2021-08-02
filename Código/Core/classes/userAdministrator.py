from .user import User

class UserAdministrator(User):    
    def __init__(self, id, firstName, lastName, email, nickName, role):
        super().__init__(id, firstName, lastName, email, nickName, role)
        
    