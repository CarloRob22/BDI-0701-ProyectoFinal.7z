USE GameManager;

DROP PROCEDURE IF EXISTS sp_moveMatch;

DELIMITER $$

CREATE PROCEDURE sp_moveMatch(
    IN timeMovement TIME,
    IN move  JSON,
    IN idMatch INT
)
BEGIN
    INSERT INTO Movement(tim_timeMovement, jso_move, int_match_FK) VALUES (timeMovement,move,idMatch);
END$$
b   
DELIMITER ;