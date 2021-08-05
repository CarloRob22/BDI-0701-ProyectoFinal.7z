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
        
    def addMovement(self):
        pass

    def verifyState(self):
        pass




