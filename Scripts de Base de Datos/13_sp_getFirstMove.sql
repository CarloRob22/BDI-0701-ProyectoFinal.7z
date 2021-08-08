USE GameManager;

DROP PROCEDURE IF EXISTS sp_getFirstMove;

DELIMITER $$

CREATE PROCEDURE sp_getFirstMove(
    IN idMatch INT,
    OUT firstMove JSON 
)
BEGIN   
    
    SELECT 
        jso_move INTO  firstMove
    FROM
        Movement
    WHERE
        int_match_FK = idMatch AND    
        JSON_UNQUOTE(JSON_EXTRACT(jso_move, '$.no')) = 0
    ;

END$$
    
DELIMITER ; 