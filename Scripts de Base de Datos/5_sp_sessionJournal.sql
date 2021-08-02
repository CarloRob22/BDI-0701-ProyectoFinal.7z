USE GameManager3;

DELIMITER $$

CREATE PROCEDURE sp_sesion (IN id INT, IN action VARCHAR(200))
BEGIN
    INSERT INTO Journal(int_id, var_action) VALUES(id, action);
END$$

DELIMITER ;