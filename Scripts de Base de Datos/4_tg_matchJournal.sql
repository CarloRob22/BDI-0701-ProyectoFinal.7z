USE GameManager;

DROP TRIGGER IF EXISTS tg_matchJournal;

DELIMITER $$
CREATE TRIGGER tg_sesion
    AFTER INSERT
    ON GameMatch FOR EACH ROW
BEGIN
    DECLARE nickname VARCHAR(30);
    DECLARE game VARCHAR(30);

    SELECT User.var_nickname INTO nickname
    FROM User
    WHERE  User.big_id = new.big_user_FK;

    SELECT Game.var_name INTO game
    FROM Game
    WHERE Game.tin_id = new.tin_game_FK;

    INSERT INTO Journal(var_action, big_user_FK) VALUES
        (CONCAT("El usuario ", nickname," inicio una partida del juego ", game), new.big_user_FK)
    ;
END $$

DELIMITER ;
