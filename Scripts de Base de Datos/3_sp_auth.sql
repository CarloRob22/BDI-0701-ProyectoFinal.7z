USE GameManager2;

DROP PROCEDURE IF EXISTS sp_auth;

DELIMITER $$

CREATE PROCEDURE sp_auth (
    IN email VARCHAR(60),
    IN pass VARCHAR(20),
    OUT res INT
)
BEGIN
    SELECT IF(tin_role_FK IS NOT NULL, tin_role_FK , 0) AS "response" INTO res
    FROM User
    WHERE var_email = email AND var_password = pass;
END$$

DELIMITER ;