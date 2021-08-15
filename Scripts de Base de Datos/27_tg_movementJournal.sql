USE GameManager;

DROP TRIGGER IF EXISTS tg_movementJournal;

DELIMITER $$
CREATE TRIGGER tg_movementJournal
    AFTER INSERT
    ON Movement FOR EACH ROW
BEGIN
    DECLARE userId BIGINT;
    DECLARE nickname VARCHAR(30);
    DECLARE game VARCHAR(30);
    DECLARE matchId BIGINT;
    DECLARE movementCount INT;

    SELECT User.big_id, User.var_nickname, Game.var_name, GameMatch.big_id INTO userId, nickname, game, matchId
    FROM 
        GameMatch
    JOIN
        Game ON GameMatch.tin_game_FK = Game.tin_id
    JOIN
        User ON GameMatch.big_user_FK = User.big_id 
    WHERE  GameMatch.big_id = new.big_match_FK;

    SELECT COUNT(big_id) INTO movementCount
    FROM Movement
    WHERE
        big_match_FK = matchId
    GROUP BY
        big_match_FK;

    INSERT INTO Journal(var_action, big_user_FK) VALUES
        (CONCAT("El usuario ", nickname," realizo un movimiento en ", game, " con un tiempo de ", new.tim_timeMovement), userId)
    ;

    INSERT INTO Journal(var_action, big_user_FK) VALUES
        (CONCAT("El usuario ", nickname," lleva un total de ", movementCount - 1," movimientos en el juego ", game), userId)
    ;
END $$

DELIMITER ;
