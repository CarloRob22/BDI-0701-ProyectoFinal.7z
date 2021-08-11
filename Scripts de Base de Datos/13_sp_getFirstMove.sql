USE GameManager;

DROP PROCEDURE IF EXISTS sp_getFirstMove;

DELIMITER $$

CREATE PROCEDURE sp_getFirstMove(
    OUT res JSON
    ) 
BEGIN      
    SELECT
        JSON_UNQUOTE(JSON_EXTRACT(jso_move,'$.move')) AS "response" INTO res   
    FROM
        Movement
    GROUP BY
        int_id ASC
    LIMIT 1;
END$$
    
DELIMITER ; 