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
        return data
    
    def deleteUser(self, idUser):
        self.db.update("CALL sp_deleteUser({})".format(idUser))
        print("Usuario {} eliminado".format(idUser))
        
    def fillTextboxUser(self, idUser):
        self.db.select("CALL sp_getUser({}, @res)".format(idUser))
        response = self.db.select("SELECT @res;")
        return response
        
    def insertUser(self,firsName,lastName,email,nickName, password):
        self.db.insert("CALL sp_insertUser('{}','{}','{}','{}','{}')".format(firsName,lastName,email,nickName, password))
        
    def updateDataUser(self,idUser,firsName,lastName,email,nickName, password):
        self.db.update("CALL sp_updateUser({},'{}','{}','{}','{}','{}')".format(idUser, firsName,lastName,email,nickName, password));    
    
    def getJournalActions(self):
        actions = self.db.select("SELECT var_action FROM Journal;")
        return actions