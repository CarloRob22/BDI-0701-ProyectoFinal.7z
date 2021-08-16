USE GameManager;

DROP PROCEDURE IF EXISTS sp_deleteUser;

DELIMITER $$

CREATE PROCEDURE sp_deleteUser(
    IN userId BIGINT
    )
    BEGIN
        DECLARE state INT DEFAULT 0;

        DECLARE matchId BIGINT;

        DECLARE cu_deleteAllUserMatches CURSOR FOR
            SELECT
                GameMatch.big_id AS matches
            FROM
                User
            JOIN
                GameMatch ON User.big_id = GameMatch.big_user_FK
            WHERE
                GameMatch.big_user_FK = userId
            ;

        DECLARE CONTINUE HANDLER FOR NOT FOUND SET state = 1;

        OPEN cu_deleteAllUserMatches;

        matches_loop: LOOP
            FETCH cu_deleteAllUserMatches INTO matchId;

            IF state = 1 THEN
                LEAVE matches_loop;
            END IF;

            DELETE FROM Score WHERE big_match_FK = matchId;
            DELETE FROM Movement WHERE big_match_FK = matchId;


        END LOOP;

        CLOSE cu_deleteAllUserMatches;

        DELETE FROM Journal WHERE big_user_FK = userId;

        DELETE FROM GameMatch WHERE big_user_FK = userId;

        DELETE FROM User WHERE big_id = userId;
        
    END $$

DELIMITER ;