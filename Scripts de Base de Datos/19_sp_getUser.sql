USE GameManager;


DROP PROCEDURE IF EXISTS sp_getUser;

DELIMITER $$

CREATE PROCEDURE sp_getUser(
    IN idUser BIGINT,
    OUT res JSON
    )   
    BEGIN      
        SELECT
            

            JSON_OBJECT(
                'idUser', big_id,
                'firstName', var_firstName,
                'lastName', var_lastName,
                'email', var_email,
                'nickName', var_nickname,
                'password', CONVERT(AES_DECRYPT(var_password,'salt') USING utf8)
            ) INTO res            
        FROM
            User
        WHERE
            big_id = idUser
        ; 

    END $$
  
DELIMITER ;
    