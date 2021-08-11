USE GameManager;


DROP PROCEDURE IF EXISTS sp_delMoveMatch;

DELIMITER $$

CREATE PROCEDURE sp_delMoveMatch(
    IN idMove INT,
    IN idMatch INT
    )   
    BEGIN
        DELETE FROM 
            Movement 
        WHERE 
            int_id = idMove AND
            int_match_FK = idMatch
        ;        
    END$$
  
DELIMITER ;