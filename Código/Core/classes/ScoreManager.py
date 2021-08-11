
#Esta clase se instancia una vez por cada instancia de partida; corresponde a una clase abstracta la cual encapsula todas
#las funcionalidades relacionadas con la tabla Score, sin embargo, la instancia no corresponde a alguna entidad score en especifico.
class ScoreManager:

    def __init__(self, db):
        self.db = db

    def set(self, matchId, gameId, time, movesTaken):
        self.db.insert("CALL sp_addScore( {} ,{},'{}', {})".format(
            matchId, gameId, time, movesTaken
        ))



