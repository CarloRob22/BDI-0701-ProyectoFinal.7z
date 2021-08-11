USE GameManager;


DROP PROCEDURE IF EXISTS sp_delMoveMatch;

DELIMITER $$

CREATE PROCEDURE sp_delMoveMatch(
    IN idMove BIGINT,
    IN idMatch BIGINT
    )   
    BEGIN
        DELETE FROM 
            Movement 
        WHERE 
            big_id = idMove AND
            big_match_FK = idMatch
        ;        
    END$$
  
DELIMITER ;