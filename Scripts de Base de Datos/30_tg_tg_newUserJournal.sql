USE GameManager;

DROP TRIGGER IF EXISTS tg_newUserJournal;

DELIMITER $$
CREATE TRIGGER tg_newUserJournal
    AFTER INSERT
    ON User FOR EACH ROW
BEGIN
    DECLARE nickname VARCHAR(30);    

    SELECT 
        new.var_nickname INTO nickname
    FROM 
        User
    ;

    INSERT INTO Journal(var_action, big_user_FK) VALUES
        (CONCAT("El administrador agrego el nuevo jugador ", nickname), new.big_id)
    ;
END $$

DELIMITER ;