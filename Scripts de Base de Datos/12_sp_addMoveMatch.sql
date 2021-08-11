USE GameManager;

DROP PROCEDURE IF EXISTS sp_addMoveMatch;

DELIMITER $$

CREATE PROCEDURE sp_addMoveMatch(
    IN timeMovement TIME,
    IN move  JSON,
    IN idMatch INT,
    OUT res JSON
)
BEGIN
    INSERT INTO 
        Movement(tim_timeMovement, jso_move, int_match_FK) 
    VALUES 
        (timeMovement,move,idMatch);

    SELECT     
        JSON_OBJECT('idMove', int_id, 'time', tim_timeMovement, 'move', jso_move, 'idMatch' ,int_match_FK) AS "response" INTO res
    FROM
        Movement
    ORDER BY 
        int_id DESC
    LIMIT 1;
END$$
  
DELIMITER ;