USE GameManager;

DROP PROCEDURE IF EXISTS sp_auth;

DELIMITER $$

CREATE PROCEDURE sp_auth (
    IN email VARCHAR(60),
    IN pass VARCHAR(255),
    OUT res JSON 
)
BEGIN
    SELECT IF(tin_role_FK IS NOT NULL, JSON_OBJECT('id', big_id,'firstName',var_firstName, 'lastName',var_lastName,'email',var_email, 'nickname', var_nickname,'tin_role', tin_role_FK) , 0) AS "response" INTO res
    FROM User
    WHERE (var_email = email OR var_nickname = email) AND CONVERT(AES_DECRYPT(var_password,'salt') USING utf8) = pass;
END$$

DELIMITER ;
