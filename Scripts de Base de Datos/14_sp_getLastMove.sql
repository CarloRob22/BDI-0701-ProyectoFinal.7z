USE GameManager;

DROP PROCEDURE IF EXISTS sp_getLastMove;

DELIMITER $$

CREATE PROCEDURE sp_getLastMove(
    OUT res JSON
    ) 
BEGIN      
    SELECT
        JSON_OBJECT('idMove', big_id , 'idMatch', big_match_FK) AS "response" INTO res
    FROM
        Movement
    GROUP BY
        big_id DESC
    LIMIT 1;
END $$
    
DELIMITER ; 