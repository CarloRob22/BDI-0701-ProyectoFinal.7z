USE GameManager;

DROP TRIGGER IF EXISTS tg_newUserJournal;

DELIMITER $$
CREATE TRIGGER tg_newUserJournal
    AFTER INSERT
    ON User FOR EACH ROW
BEGIN
    DECLARE nickname VARCHAR(30);    

    SELECT 
        var_nickname INTO nickname
    FROM 
        User
    WHERE
        big_id = new.big_id
    ;

    INSERT INTO Journal(var_action, big_user_FK) VALUES
        (CONCAT("El administrador agrego el nuevo jugador ", nickname), 1)
    ;
END $$

DELIMITER ;