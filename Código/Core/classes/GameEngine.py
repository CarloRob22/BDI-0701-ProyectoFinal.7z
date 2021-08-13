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

    def updateStateMatch(self, lastTime, gameState):       
        self.user.updateStateMatch(lastTime, gameState)   
    
    def checkStateMatch(self):               
        return self.user.checkStateMatch(self.user.getIdUser())
    
    def successfulMatch(self, lastTime, gamestate):
        self.user.uppSuccessfulMatch(lastTime, gamestate)
        
    def addMovementMatch(self, time, move):
        self.user.addMovementMatch(time,move)
        
    def getFirstMove(self):
        return self.user.getFirstMove()
                
    def delMovement(self):
        self.user.delMovement()

    def setScore(self, movesTaken,gameId, time):
        self.user.setScore(movesTaken, gameId, time)
          
    def getAllDataUser(self):
        return self.user.getAllDataUser()   
    
    def deleteUser(self, idUser):
        self.user.deleteUser(idUser)       
        
    def fillTextboxUser(self, idUser):
        return self.user.fillTextboxUser(idUser)

    def insertUser(self,firsName,lastName,email,nickName, password):
        self.user.insertUser(firsName,lastName,email,nickName, password)
    
    def updateDataUser(self,idUser,firsName,lastName,email,nickName, password):
        self.user.updateDataUser(idUser,firsName,lastName,email,nickName, password)

    def restartGameMatchHold(self):
        return self.user.restartGameMatchHold()
        
    def getAllMovesMatch(self):
        return self.user.getAllMovesMatch()
    
    def getLastTime(self):
        return self.user.getLastTime()
    
    def updateJsonMoves(self, jsonMove):
        self.user.updateJsonMoves(jsonMove)

    def getUserScores(self):
        return self.user.getScores()