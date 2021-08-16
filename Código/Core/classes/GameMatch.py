# -*- coding: utf-8 -*-
"""
    @author   roberto.duran@unah.hn, mruizq@unah.hn
    @version 0.1.0
    @date 2021/08/13
"""
import json
from .Movement import Movement
from .ScoreManager import ScoreManager

class GameMatch:
    def __init__(self, id, idState, lastTime, db):
        self.db = db
        self.id = id        
        self.idState = idState        
        self.lastTime = lastTime
        

    def updateState(self, lastTime, gameState):
        self.db.update("CALL sp_updateGameMatch(%s,'%s',%s)" % (self.id,lastTime, gameState))
        
    def addMovement(self,time,move):
        self.db.insert("CALL sp_addMoveMatch('%s','%s', %s, @res);"%(time, str(move), self.id))
        response = self.db.select("SELECT @res;")
        print(response)
        if response[0][0] is not None:
            movement = json.loads(response[0][0])            
        self.movement = Movement(movement["idMove"],movement["time"],movement["move"],movement["idMatch"], self.db)
        self.lastTime = time
    
    def restartGameMatch(self):     
        self.db.select("CALL sp_restartGameMatch({},{},@res)")
       
    def getFirstMove(self):
        return self.movement.getFirstMove(self.id)
        
    def delMovement(self):
        self.movement.delMovement()      
    
    def setScore(self, movesTaken, gameId, time):
        ScoreManager(self.db).set(self.id, gameId, time, movesTaken)
     
    def updateJsonMoves(self, jsonMove):
        self.db.update("CALL sp_updateJsonMoves({},{})".format(self.id, jsonMove))
        

    