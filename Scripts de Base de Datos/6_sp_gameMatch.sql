USE GameManager;

DROP PROCEDURE IF EXISTS sp_insertGameMatch;

DELIMITER $$

CREATE PROCEDURE sp_insertGameMatch(
    IN lastTime TIME,
    IN game_FK TINYINT,
    IN user_FK BIGINT,
    IN gameState_FK TINYINT,
    OUT res JSON
)
BEGIN

    INSERT INTO GameMatch (tim_lastTime, tin_game_FK, big_user_FK, tin_gameState_FK) VALUES
        (lastTime, game_FK, user_FK, gameState_FK);

    SELECT JSON_OBJECT('idMatch', big_id, 'lastTime', tim_lastTime, 'gameId', tin_game_FK, 'userId', big_user_FK, 'gameStateId', tin_gameState_FK) AS "response" INTO res
    FROM
        GameMatch
    ORDER BY big_id DESC
    LIMIT 1;

END$$

DELIMITER ;



