
USE GameManager;

DROP PROCEDURE IF EXISTS sp_updateJsonMoves;

DELIMITER $$

CREATE PROCEDURE sp_updateJsonMoves(
    IN idMatch BIGINT,
    IN jsonMove JSON
    )
    BEGIN
        UPDATE 
            Movement
        SET 
            jso_move = jsonMove
        WHERE 
            big_match_FK = idMatch
        ;
    END $$

DELIMITER ;