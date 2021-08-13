
import json
#Esta clase se instancia una vez por cada instancia de partida; corresponde a una clase abstracta la cual encapsula todas
#las funcionalidades relacionadas con la tabla Score, sin embargo, la instancia no corresponde a alguna entidad score en especifico.
class ScoreManager:

    def __init__(self, db):
        self.db = db

    def set(self, matchId, gameId, time, movesTaken):
        self.db.insert("CALL sp_addScore( {} ,{},'{}', {})".format(
            matchId, gameId, time, movesTaken
        ))

    def get(self, idUser):
        self.db.select("call sp_getUserScore({},@json);".format(idUser))
        scoresJson = self.db.select("SELECT @json")
        if scoresJson[0][0] is not None:
            scores = json.loads(scoresJson[0][0])
            return scores
        else:
            return scoresJson
        



