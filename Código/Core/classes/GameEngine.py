from Core.classes.Auth import Auth
from Core.classes.GameMatch import GameMatch

class MyGameEngine:
    
    def __init__(self,db):        
        self.db = db
        self.view = None
        self.user = None   
        
    def authUser(self, email, password):
        self.user = Auth(self.db).auth(email, password)
        return self.user

    def startMatch(self, gameId):
        self.user.startMatch(gameId)    

    def updateStateMatch(self, gameState):       
        self.user.updateStateMatch(gameState)
                    


    
