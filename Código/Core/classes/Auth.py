from Core.classes.AdministratorUser import AdministratorUser
from Core.classes.PlayerUser import PlayerUser

import json

class Auth:
    def __init__(self, db):
        self.db = db

    def auth(self, email, password):
        self.db.select("CALL sp_auth('%s','%s',@res)" % (email, password))
        response = self.db.select("SELECT @res;")
        if response[0][0] is not None:
            print(response[0][0])
            user = json.loads(response[0][0])
            self.authInJournal(user["nickname"],user["id"])
            return self.getRole(user["id"],user["firstName"],user["lastName"],user["email"],user["nickname"],user["tin_role"])        
        else:
            return None

    def getRole(self, id, firstName, lastName, email, nickName, role):
        if role == 2:
            return AdministratorUser(id, firstName, lastName, email, nickName, role)
        else:
            return PlayerUser(id, firstName, lastName, email, nickName, role)

    def authInJournal(self, nickname, id):
        action = "Usuario %s inicio sesión con exíto"%(nickname)
        self.db.insert("CALL sp_sessionJournal(%s, '%s');" %(id, action))