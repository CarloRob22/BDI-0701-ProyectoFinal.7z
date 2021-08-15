USE GameManager;

DROP TRIGGER IF EXISTS tg_updateUserJournal;

DELIMITER $$
CREATE TRIGGER tg_updateUserJournal
    AFTER UPDATE
    ON User FOR EACH ROW
BEGIN
    DECLARE nickname VARCHAR(30);    

    SELECT 
        new.var_nickname INTO nickname
    FROM 
        User
    WHERE
        big_id = new.big_id     
    ;    

    INSERT INTO Journal(var_action, big_user_FK) VALUES
        (CONCAT("El administrador actualizó datos del usuario ", nickname), 1)
    ;
END $$

DELIMITER ;