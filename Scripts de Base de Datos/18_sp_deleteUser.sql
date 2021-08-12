USE GameManager;

DROP PROCEDURE IF EXISTS sp_deleteUser;

DELIMITER $$

CREATE PROCEDURE sp_deleteUser(
    IN idSel BIGINT
    )
    BEGIN
        DELETE  FROM 
            User 
        WHERE
            big_id = idSel
        ;
    END $$

DELIMITER ;