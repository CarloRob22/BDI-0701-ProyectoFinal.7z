USE GameManager;

DROP PROCEDURE IF EXISTS sp_addMoveMatch;

DELIMITER $$

CREATE PROCEDURE sp_addMoveMatch(
    IN timeMovement TIME,
    IN move  BLOB,
    IN idMatch BIGINT,
    OUT res JSON
)
BEGIN

    INSERT INTO 
        Movement(tim_timeMovement, blo_move, big_match_FK) 
    VALUES 
        (timeMovement, AES_ENCRYPT(move,'salt'), idMatch);

    SELECT     
        JSON_OBJECT('idMove', big_id, 'time', tim_timeMovement, 'move', CAST(AES_DECRYPT(blo_move,'salt') AS CHAR), 'idMatch' ,big_match_FK) AS "response" INTO res 
    FROM
        Movement
    ORDER BY 
        big_id DESC
    LIMIT 1;
END$$
 
DELIMITER ;