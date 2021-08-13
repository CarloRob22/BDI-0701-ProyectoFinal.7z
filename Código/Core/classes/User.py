#from time import process_time_ns
from Core.classes.GameMatch import GameMatch
import json

class User:
    def __init__(self, db, id ,firstName, lastName, email, nickName, role):
        self.db = db
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.nickName = nickName
        self.role = role
        self.gamematch = None
        
    def startMatch(self, gameId):
        self.db.insert("CALL sp_insertGameMatch('%s',%s,%s,%s,@res)" % ("00:00:00", gameId, self.id, 1))
        response = self.db.select("SELECT @res;")
        if response[0][0] is not None:
            match = json.loads(response[0][0])
            print(match)      
        self.gameMatch = GameMatch(match["idMatch"], match["gameStateId"], match["lastTime"], self.db)
        
    def updateStateMatch(self, lastTime, gameState):
        self.gameMatch.updateState(lastTime, gameState)        
    
    #Mediante el siguiente Método se verifica si existe una partidad guardada en estado Hold(id=2).
    def checkStateMatch(self, idUser):               
        self.db.select("CALL sp_getHoldMatch({},@res);".format(idUser))
        response = self.db.select("SELECT @res;")        
        return response
    
    def uppSuccessfulMatch(self, lastTime, gamestate):
        self.gameMatch.successfulMatch(lastTime, gamestate)
              
        
    def addMovementMatch(self, time, move):
        self.gameMatch.addMovement(time, move)
    
    
    def getFirstMove(self):
        return self.gameMatch.getFirstMove()        
    
    def delMovement(self):
        self.gameMatch.delMovement()

    def setScore(self, movesTaken, gameId, time):
        self.gameMatch.setScore(movesTaken, gameId, time)
        
    def restartGameMatchHold(self):        
        data = self.db.select("CALL sp_getAllDataMatchHold({});".format(self.id))
        print(data[0][0], data[0][4], data[0][1])         
        self.gameMatch = GameMatch(data[0][0], data[0][4], data[0][1], self.db)            
        return data       
    
    def updateJsonMoves(self, jsonMove):
        self.gameMatch.updateJsonMoves(jsonMove)