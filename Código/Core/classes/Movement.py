
import json

class Movement:
    def __init__(self, id, time, move, idMatch, db):
        self.id = id
        self.time = time
        self.move = move
        self.idMatch = idMatch
        self.db = db
        
    def getFirstMove(self):
        self.db.select("CALL sp_getFirstMove(@res);")
        response = self.db.select("SELECT @res;")
        print("response: {}".format(response))
        move = json.loads(response[0][0])
        print(move)
        return move
    
    def delMovement(self):
        self.db.select("CALL sp_getLastMove(@resfm);")
        response = self.db.select("SELECT @resfm;")
        lastmove = json.loads(response[0][0])
        self.db.update("CALL sp_delMoveMatch({},{});".format(lastmove["idMove"],lastmove["idMatch"]))