USE GameManager;

DROP TRIGGER IF EXISTS tg_delUserJournal;

DELIMITER $$
CREATE TRIGGER tg_delUserJournal
    BEFORE DELETE
    ON User FOR EACH ROW
BEGIN
    DECLARE nickname VARCHAR(30);    

    SELECT 
        var_nickname INTO nickname
    FROM 
        User
    WHERE
        big_id = old.big_id     
    ;    

    INSERT INTO Journal(var_action, big_user_FK) VALUES
        (CONCAT("El administrador eliminó al usuario jugador ", nickname), 1)
    ;
END $$

DELIMITER ;