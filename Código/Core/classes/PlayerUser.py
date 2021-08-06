from .User import User

class PlayerUser(User):
    def __init__(self, db, id, firstName, lastName, email, nickName, role):
        super().__init__(db, id, firstName, lastName, email, nickName, role)
        self.id = id
    
    def getIdUser(self):
        return self.id