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
        int_id = idMatch
    ;

    SELECT 
        JSON_OBJECT('idMatch', int_id, 'lastTime', tim_lastTime, 'gameId', tin_game_FK, 'userId', int_user_FK, 'gameStateId', tin_gameState_FK) AS "response" INTO res
    FROM
        GameMatch
    ORDER BY 
        int_id DESC
    LIMIT 1;

END$$

DELIMITER ;

