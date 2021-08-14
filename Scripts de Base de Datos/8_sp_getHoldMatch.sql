USE GameManager;

DROP PROCEDURE IF EXISTS sp_getHoldMatch;

DELIMITER $$

CREATE PROCEDURE sp_getHoldMatch(
    IN idUser BIGINT,    
    OUT res JSON
)
BEGIN
    
    SELECT 
        JSON_OBJECT('idMatch', big_id, 'lastTime', tim_lastTime, 'gameId', tin_game_FK, 'userId', big_user_FK, 'gameStateId', tin_gameState_FK) AS "response" INTO res
    FROM
        GameMatch
    WHERE
        big_user_FK = idUser 
    ORDER BY
        big_id DESC
    LIMIT 1;

END$$

DELIMITER ;   


