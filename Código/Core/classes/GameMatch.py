import json
from .Movement import Movement

class GameMatch:
    def __init__(self, id, idState, lastTime, db):
        self.db = db
        self.id = id        
        self.idState = idState        
        self.lastTime = lastTime
        

    def updateState(self, gameState):
        self.db.update("CALL sp_updateStateGameMatch({},{},@res)".format(self.id, gameState))
        
    def addMovement(self,time,move):
        self.db.insert("CALL sp_addMoveMatch('%s','%s', %s, @res);"%(time, move, self.id))
        response = self.db.select("SELECT @res;")
        if response[0][0] is not None:
            movement = json.loads(response[0][0])
            print(movement)
        self.movement = Movement(movement["idMove"],movement["time"],movement["move"],movement["idMatch"], self.db)
        
    def verifyState(self):
        pass
    
    def getFirstMove(self):
        self.movement.getFirstMove()
        
    def delMovement(self):
        self.movement.delMovement()
    
    def successfulMatch(self, lastTime, gamestate):
        self.db.update("CALL sp_updateGameMatch(%s,'%s',%s)" % (self.id,lastTime, gamestate))
       
    




    