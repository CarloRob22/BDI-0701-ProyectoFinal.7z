from Core.classes.userAdministrator import UserAdministrator
from Core.classes.userPlayer import UserPlayer

class MyGameEngine:
    
    def __init__(self, db):
        self.db = db
        self.user = None
        self.games = []
        self.gameStates = []

    def auth(self, email, password):
        
        self.db.select("CALL sp_auth('%s','%s',@res)" % (email, password))
        response = self.db.select("SELECT @res;")
    
        if len(response) > 0:
            return response[0][0]
        else:
            return 0
    
    def addUser(self, id, firstName, lastName, email, nickName, role):
        if role == 2:
            self.user = UserAdministrator(id, firstName, lastName, email, nickName, role)
        else:
            self.user = UserPlayer(id, firstName, lastName, email, nickName, role)

    def sesionInJournal(self):
        action = "Usuario %s inicio sesión con exíto"%(self.user.nickname)
        
            
    def addGame(self):
        pass

    def addGameState(self):
        pass

    
