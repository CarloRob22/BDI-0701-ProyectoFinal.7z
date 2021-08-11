USE GameManager;

DROP PROCEDURE IF EXISTS sp_updateGameMatch;

DELIMITER $$

CREATE PROCEDURE sp_updateGameMatch(
    IN idMatch INT,
    IN lastTime TIME,    
    IN gameState TINYINT    
    
)
BEGIN
    UPDATE 
        GameMatch 
    SET 
        tim_lastTime = lastTime,
        tin_gameState_FK = gameState
    WHERE 
        big_id = idMatch        
    ;
END$$

DELIMITER ;