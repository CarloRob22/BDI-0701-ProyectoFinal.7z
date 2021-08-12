USE GameManager;

DROP TRIGGER IF EXISTS tg_scoreJournal;

DELIMITER $$
CREATE TRIGGER tg_scoreJournal
    AFTER INSERT
    ON Score FOR EACH ROW
BEGIN
    DECLARE nickname VARCHAR(30);
    DECLARE game VARCHAR(30);
    DECLARE userId BIGINT;

    SELECT User.var_nickname, User.big_id INTO nickname, userId
    FROM 
        GameMatch
    JOIN
        User ON GameMatch.big_user_FK = User.big_id
    WHERE  GameMatch.big_id = new.big_match_FK;

    SELECT Game.var_name INTO game
    FROM 
        GameMatch
    JOIN
        Game ON GameMatch.tin_game_FK = Game.tin_id
    WHERE GameMatch.big_id = new.big_match_FK;

    INSERT INTO Journal(var_action, big_user_FK) VALUES
        (CONCAT("El usuario ", nickname," registro un puntaje de ", new.dec_score," en el juego ", game), userId)
    ;
END $$

DELIMITER ;
