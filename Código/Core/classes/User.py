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
        self.match = None
        

    def startMatch(self, gameId):
        self.db.insert("CALL sp_insertGameMAtch('%s',%s,%s,%s,@res)" % ("00:00:00", gameId, self.id, 1))
        response = self.db.select("SELECT @res;")
        if response[0][0] is not None:
            self.match = json.loads(response[0][0])
            print(self.match)

    def updateStateMatch(self, gameState):           
        self.gameMatch = GameMatch(self.match["idMatch"], self.match["gameStateId"], self.match["lastTime"], self.db)
        self.gameMatch.updateState(gameState)
    
        
        
        
        

    
    