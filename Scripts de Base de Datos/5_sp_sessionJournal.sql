USE GameManager;

DROP PROCEDURE IF EXISTS sp_sessionJournal;

DELIMITER $$

CREATE PROCEDURE sp_sessionJournal (IN id INT, IN action VARCHAR(200))
BEGIN
    INSERT INTO Journal(int_user_FK, var_action) VALUES(id, action);
END$$

DELIMITER ;