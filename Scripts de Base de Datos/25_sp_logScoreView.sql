USE GameManager;

DROP PROCEDURE IF EXISTS sp_logScoreView;

DELIMITER $$

CREATE PROCEDURE sp_logScoreView(IN userId BIGINT, IN nickname VARCHAR(50))
    BEGIN
        INSERT INTO Journal( var_action, big_user_FK ) VALUES
            (CONCAT("El usuario ", nickname," accedio a su tabla de puntajes"), userId)
        ;
    END $$

DELIMITER ;