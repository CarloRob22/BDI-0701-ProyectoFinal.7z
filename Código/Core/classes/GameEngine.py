from Core.classes.Auth import Auth
from Core.classes.GameMatch import GameMatch

class MyGameEngine:
    
    def __init__(self,db):        
        self.db = db
        self.view = None
        self.user = None 
        self.idUser = None  
        
    def authUser(self, email, password):
        self.user = Auth(self.db).auth(email, password)
        self.idUser = self.user.getIdUser()
        return self.user

    def startMatch(self, gameId):
        self.user.startMatch(gameId)    

    def updateStateMatch(self, gameState):       
        self.user.updateStateMatch(gameState)   
    
    def checkStateMatch(self):       
        return self.user.checkStateMatch(int(self.idUser))
    
    def successfulMatch(self, lastTime, gamestate):
        self.user.uppSuccessfulMatch(lastTime, gamestate)
        
        
                    


    
