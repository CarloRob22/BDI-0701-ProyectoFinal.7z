USE GameManager;

DROP PROCEDURE IF EXISTS sp_updateStateGameMatch;

DELIMITER $$

CREATE PROCEDURE sp_updateStateGameMatch(
    IN idMatch INT,
    IN gameState TINYINT, 
    OUT res JSON
)
BEGIN
    UPDATE 
        GameMatch 
    SET 
        tin_gameState_FK = gameState 
    WHERE 
        big_id = idMatch
    ;

    SELECT 
        JSON_OBJECT('idMatch', big_id, 'lastTime', tim_lastTime, 'gameId', tin_game_FK, 'userId', big_user_FK, 'gameStateId', tin_gameState_FK) AS "response" INTO res
    FROM
        GameMatch
    ORDER BY 
        big_id DESC
    LIMIT 1;

END$$

DELIMITER ;


