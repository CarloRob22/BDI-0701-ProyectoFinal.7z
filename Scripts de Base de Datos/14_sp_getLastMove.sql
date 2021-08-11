USE GameManager;

DROP PROCEDURE IF EXISTS sp_getLastMove;

DELIMITER $$

CREATE PROCEDURE sp_getLastMove(
    OUT res JSON
    ) 
BEGIN      
    SELECT
        JSON_OBJECT('idMove', int_id , 'idMatch', int_match_FK) AS "response" INTO res
    FROM
        Movement
    GROUP BY
        int_id DESC
    LIMIT 1;
END$$
    
DELIMITER ; 