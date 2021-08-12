USE GameManager;

DROP PROCEDURE IF EXISTS sp_restartGameMatch;

DELIMITER $$

CREATE PROCEDURE sp_restartGameMatch(
    IN idUser_FK INT,    
    OUT res JSON
)
BEGIN
    SELECT 
        JSON_OBJECT('idMatch', int_id, 'lastTime', tim_lastTime, 'gameId', tin_game_FK, 'userId', int_user_FK, 'gameStateId', tin_gameState_FK) AS "response" INTO res
        
    FROM
        GameMatch,
    WHERE
        int_user_FK = idUser
        tin_gameState_FK = 2
    LIMIT 1;
END$$

DELIMITER ;