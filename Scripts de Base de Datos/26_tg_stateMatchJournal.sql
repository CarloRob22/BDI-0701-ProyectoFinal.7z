USE GameManager;

DROP TRIGGER IF EXISTS tg_stateMatchJournal;

DELIMITER $$
CREATE TRIGGER tg_stateMatchJournal
    AFTER UPDATE
    ON GameMatch FOR EACH ROW
BEGIN
    DECLARE nickname VARCHAR(30);
    DECLARE game VARCHAR(30);
    DECLARE userId BIGINT;
    DECLARE matchStateName VARCHAR(50);

    IF new.tin_gameState_FK = 1 THEN SET matchStateName = "en progreso";
        ELSEIF new.tin_gameState_FK = 2 THEN SET matchStateName = "en espera";
        ELSEIF new.tin_gameState_FK = 3 THEN SET matchStateName = "en pausa";
        ELSEIF new.tin_gameState_FK = 4 THEN SET matchStateName = "declaro en derrota";
        ELSE SET matchStateName = "finalizo exitosamente";
    END IF;

    SELECT User.var_nickname, User.big_id, Game.var_name INTO nickname, userId, game
    FROM 
        GameMatch
    JOIN
        User ON GameMatch.big_user_FK = User.big_id
    JOIN
        Game ON GameMatch.tin_game_FK = Game.tin_id
    WHERE  GameMatch.big_id = new.big_id;

    
    IF new.tin_gameState_FK = 4 THEN
        INSERT INTO Journal(var_action, big_user_FK) VALUES
            (CONCAT("El usuario ", nickname," se ", matchStateName," en el juego ", game), userId)
        ;
    ELSEIF new.tin_gameState_FK = 5 THEN
        INSERT INTO Journal(var_action, big_user_FK) VALUES
            (CONCAT("El usuario ", nickname," ", matchStateName," una partida en el juego ", game), userId)
        ;
    ELSE
        INSERT INTO Journal(var_action, big_user_FK) VALUES
            (CONCAT("El usuario ", nickname," cambio de estado a ", matchStateName," una partida en el juego ", game), userId)
        ;
    END IF;
END $$

DELIMITER ;
