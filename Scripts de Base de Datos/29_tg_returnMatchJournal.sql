USE GameManager;

DROP TRIGGER IF EXISTS tg_returnMatchJounal;

DELIMITER $$
CREATE TRIGGER tg_returnMatchJounal
    AFTER UPDATE
    ON GameMatch FOR EACH ROW
BEGIN
    DECLARE nickname VARCHAR(30);
    DECLARE game VARCHAR(30);
    DECLARE userId BIGINT;    

    IF new.tin_gameState_FK = 1 AND new.tim_lastTime != "00:00:00" THEN             

        SELECT User.var_nickname, User.big_id, Game.var_name INTO nickname, userId, game
        FROM 
            GameMatch
        JOIN
            User ON GameMatch.big_user_FK = User.big_id
        JOIN
            Game ON GameMatch.tin_game_FK = Game.tin_id
        WHERE  GameMatch.big_id = new.big_id;

        
        INSERT INTO Journal(var_action, big_user_FK) VALUES
            (CONCAT("El usuario ", nickname," reanudó partida en espera del juego ", game), userId)
        ;
    END IF;
END $$

DELIMITER ;