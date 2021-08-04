USE GameManager;

DROP PROCEDURE IF EXISTS sp_insertGameMatch;

DELIMITER $$

CREATE PROCEDURE sp_insertGameMatch(
    IN lastTime TIME,
    IN game_FK TINYINT,
    IN user_FK INT,
    IN gameState_FK TINYINT,
    OUT res JSON
)
BEGIN

    INSERT INTO GameMatch (tim_lastTime, tin_game_FK, int_user_FK, tin_gameState_FK) VALUES
        (lastTime, game_FK, user_FK, gameState_FK);

    SELECT JSON_OBJECT('idMatch', int_id, 'lastTime', tim_lastTime, 'gameId', tin_game_FK, 'userId', int_user_FK, 'gameStateId', tin_gameState_FK) AS "response" INTO res
    FROM
        GameMatch
    ORDER BY int_id DESC
    LIMIT 1;

END$$

DELIMITER ;