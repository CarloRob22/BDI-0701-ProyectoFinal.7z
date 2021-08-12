USE GameManager;

DROP PROCEDURE IF EXISTS sp_insertUser;

DELIMITER $$

CREATE PROCEDURE sp_insertUser(    
    IN firstName VARCHAR(30),
    IN lastName VARCHAR(30),
    IN email VARCHAR(60),
    IN nickName VARCHAR(100),
    IN pass VARCHAR(20)    
)
BEGIN
    INSERT INTO 
        User(var_firstName, var_lastName, var_email, var_nickname, var_password, tin_role_FK ) 
    VALUES 
        (firstName, lastName, email, nickName, pass, 1);   
END$$
  
DELIMITER ;