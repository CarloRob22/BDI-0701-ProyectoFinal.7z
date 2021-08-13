USE GameManager;

DROP PROCEDURE IF EXISTS sp_getAllDataMatchHold;

DELIMITER $$

CREATE PROCEDURE sp_getAllDataMatchHold(
    IN idUser INT          
)
BEGIN
    SELECT
        GameMatch.big_id,
        GameMatch.tim_lastTime,
        GameMatch.tin_game_FK,
        GameMatch.big_user_FK,
        GameMatch.tin_gameState_FK,        
        Movement.jso_move        
    FROM
        GameMatch, 
        Movement
    WHERE 
        GameMatch.big_user_FK = idUser AND
        GameMatch.tin_gameState_FK = 2 
    LIMIT 1
    ;
END$$

DELIMITER ;