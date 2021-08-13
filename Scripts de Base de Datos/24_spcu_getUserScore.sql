USE GameManager;

DROP PROCEDURE IF EXISTS sp_getUserScore;


DELIMITER $$

CREATE PROCEDURE sp_getUserScore(IN userId BIGINT, OUT jsonOfJsons JSON)
    BEGIN
        DECLARE state INT DEFAULT 0;
        
        DECLARE scoreJson JSON;

        DECLARE jsonCounter INT DEFAULT 1;

        DECLARE jsonKey VARCHAR(20);

        DECLARE cu_mergeJsons CURSOR FOR
            SELECT
                JSON_OBJECT(
                    'score',dec_score,
                    'time',tim_timeScore,
                    'date',Score.tim_dueDate,
                    'gameName',Game.var_Name
                ) AS scores
            FROM
                Score
            JOIN
                GameMatch ON Score.big_match_FK = GameMatch.big_id
            JOIN
                Game ON GameMatch.tin_game_FK = Game.tin_id
            WHERE
                GameMatch.big_user_FK = userId
            ORDER BY
                dec_score DESC
            LIMIT
                0,10
            ;

        DECLARE CONTINUE HANDLER FOR NOT FOUND SET state = 1;

        OPEN cu_mergeJsons;

        jsons_loop: LOOP
            FETCH cu_mergeJsons INTO scoreJson;

            IF state = 1 THEN
                LEAVE jsons_loop;
            END IF;

            SET jsonKey = CONCAT("$.score",jsonCounter);

            IF jsonOfJsons IS NULL THEN
                SELECT JSON_ARRAY_APPEND('{}',jsonKey,scoreJson) INTO jsonOfJsons;
            END IF;

            IF jsonOfJsons IS NOT NULL AND jsonKey IS NOT NULL AND scoreJson IS NOT NULL THEN
                SELECT JSON_INSERT(jsonOfJsons,jsonKey,scoreJson) INTO jsonOfJsons;
            END IF;
            

            SET jsonCounter = jsonCounter +1;
        END LOOP;

        CLOSE cu_mergeJsons;
    END $$

DELIMITER ;