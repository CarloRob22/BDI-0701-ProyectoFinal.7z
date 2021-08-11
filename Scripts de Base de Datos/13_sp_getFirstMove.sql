USE GameManager;

DROP PROCEDURE IF EXISTS sp_getFirstMove;

DELIMITER $$

CREATE PROCEDURE sp_getFirstMove(
    IN idMatch BIGINT,
    OUT res JSON
    ) 
BEGIN      
    SELECT
        JSON_UNQUOTE(JSON_EXTRACT(jso_move,'$.move')) AS "response" INTO res   
    FROM
        Movement
    WHERE
        big_match_FK = idMatch 
    ORDER BY
        big_id ASC
    LIMIT 1;
END$$
    
DELIMITER ; 