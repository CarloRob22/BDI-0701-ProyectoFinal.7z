# -*- coding: utf-8 -*-
"""
    @author   roberto.duran@unah.hn, mruizq@unah.hn
    @version 0.1.0
    @date 2021/08/13
"""
#from time import process_time_ns
from Core.classes.GameMatch import GameMatch
from Core.classes.ScoreManager import ScoreManager
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
        if response[0][0] is not None:
            dataMatch = json.loads(response[0][0])                   
            return dataMatch
        else:
            return response[0][0]  
              
        
    def addMovementMatch(self, time, move):
        self.gameMatch.addMovement(time, move)
    
    
    def getFirstMove(self):
        return self.gameMatch.getFirstMove()        
    
    def delMovement(self):
        self.gameMatch.delMovement()

    def setScore(self, movesTaken, gameId, time):
        self.gameMatch.setScore(movesTaken, gameId, time)
        
    def restartGameMatchHold(self):        
        self.db.select("CALL sp_getAllDataMatchHold({},@res);".format(self.id))
        response = self.db.select("SELECT @res;")
        listMoves = []
        if response[0][0] is not None:
            dataMatch = json.loads(response[0][0])                     
            for move in dataMatch.values():
                #print(move["jsonMove"]["move"])
                listMoves.append(move["jsonMove"]["move"])
                lastTime = move["lastTime"]  
                idGame = move["idGame"]                 
        self.gameMatch = GameMatch(move["idMatch"], move["stateMatch"], move["lastTime"], self.db)
        return (lastTime,listMoves, idGame)  

         
    
    def updateJsonMoves(self, jsonMove):
        self.gameMatch.updateJsonMoves(jsonMove)

    def getScores(self):
        return ScoreManager(self.db).get(self.id)

    def logScoreView(self):
        self.db.insert("CALL sp_logScoreView({},'{}')".format(self.id, self.nickName))

    