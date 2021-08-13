USE GameManager;

DROP PROCEDURE IF EXISTS sp_addScore;

DELIMITER $$

CREATE PROCEDURE sp_addScore(
    IN matchId BIGINT,
    IN gameId TINYINT,
    IN timeScore TIME, 
    IN movesTaken INT
)
    BEGIN

        DECLARE score DECIMAL(20,6);

        IF gameId = 1 THEN SET score = (SELECT fn_weighFloodItMatch(movesTaken, timeScore));
        ELSE SET score = (SELECT fn_weighDestroyDotsMatch(movesTaken, timeScore));
        END IF;

        INSERT INTO Score(dec_score, tim_timeScore, big_match_FK) VALUES
            (score, timeScore, matchId)
        ;
    END $$

DELIMITER ;