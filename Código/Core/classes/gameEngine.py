from Core.classes.userAdministrator import UserAdministrator
from Core.classes.userPlayer import UserPlayer

class MyGameEngine:
    
    def __init__(self, db):
        self.db = db
        self.user
        self.games = []
        self.gameStates = []

    def auth(self, email, password):
        
        self.db.select("CALL sp_auth('%s','%s',@res)" % (email, password))
        response = self.db.select("SELECT @res;")
    
        if len(response) > 0:
            return response[0][0]
        else:
            return 0
    
    def addUsers(self):
        pass

    def verifyRoleUser(self):
        pass

    def addGame(self):
        pass

    def addGameState(self):
        pass

    
