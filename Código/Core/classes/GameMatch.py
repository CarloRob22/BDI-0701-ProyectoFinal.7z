import json

class GameMatch:
    def __init__(self, id, idState, lastTime, db):
        self.db = db
        self.id = id        
        self.idState = idState        
        self.lastTime = lastTime
        self.movements = None

    def updateState(self, gameState):
        self.db.update("CALL sp_updateStateGameMatch({},{},@res)".format(self.id, gameState))
        
    def addMovement(self,time,move):
        self.db.insert("CALL sp_moveMatch('%s','%s', %s);"%(time, move, self.id))
       

    def verifyState(self):
        pass
    
    def successfulMatch(self, lastTime, gamestate):
        self.db.update("CALL sp_updateGameMatch(%s,'%s',%s)" % (self.id,lastTime, gamestate))
       
    def getFirstMove(self):
        self.db.select("CALL sp_getFirstMove({},@res)".format(self.id))
        response = self.db.select("SELECT @res;")
        move = json.loads(response[0][0])
        print(move["move"])
        return move["move"]




    