USE GameManager;

DROP PROCEDURE IF EXISTS sp_updateUser;

DELIMITER $$

CREATE PROCEDURE sp_updateUser(
    IN idUser BIGINT,
    IN fName VARCHAR(30),
    IN lName VARCHAR(30),
    IN email VARCHAR(60),
    IN nick VARCHAR(100),
    IN pass VARCHAR(255)
)
BEGIN
    UPDATE 
        User
    SET 
        var_firstName = fName,
        var_lastName = lName,
        var_email = email,
        var_nickname = nick,
        var_password = AES_ENCRYPT(pass,'salt')
    WHERE 
        big_id = idUser
    ;
END$$

DELIMITER ;