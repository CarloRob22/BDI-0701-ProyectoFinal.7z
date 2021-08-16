# -*- coding: utf-8 -*-
"""
    @author   roberto.duran@unah.hn, mruizq@unah.hn
    @version 0.1.0
    @date 2021/08/13
"""
import json

class Movement:
    def __init__(self, id, time, move, idMatch, db):
        self.id = id
        self.time = time
        self.move = move
        self.idMatch = idMatch
        self.db = db
        
    def getFirstMove(self, idMatch):        
        #idMatch -= 1        
        self.db.select("CALL sp_getFirstMove({}, @res);".format(idMatch))
        response = self.db.select("SELECT @res;")        
        move = json.loads(response[0][0])
        #print("primer move: {}".format(move))
        return move
    
    def delMovement(self):
        self.db.select("CALL sp_getLastMove(@resfm);")
        response = self.db.select("SELECT @resfm;")
        lastmove = json.loads(response[0][0])
        self.db.update("CALL sp_delMoveMatch({},{});".format(lastmove["idMove"],lastmove["idMatch"]))