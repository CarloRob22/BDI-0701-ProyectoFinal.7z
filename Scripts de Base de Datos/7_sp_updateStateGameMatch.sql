USE GameManager;

DROP PROCEDURE IF EXISTS sp_updateStateGameMatch;

DELIMITER $$

CREATE PROCEDURE sp_updateStateGameMatch(
    IN idMatch BIGINT,
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


