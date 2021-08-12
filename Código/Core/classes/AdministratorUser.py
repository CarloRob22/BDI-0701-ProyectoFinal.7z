from .User import User

class AdministratorUser(User):    
    def __init__(self, db, id, firstName, lastName, email, nickName, role):
        super().__init__(db, id, firstName, lastName, email, nickName, role)
        self.id = id
        
    def getIdUser(self):
        return self.id
    
    def getAllDataUser(self):
        data = self.db.select("select * from vm_getAllDataUser;")
        print(data)