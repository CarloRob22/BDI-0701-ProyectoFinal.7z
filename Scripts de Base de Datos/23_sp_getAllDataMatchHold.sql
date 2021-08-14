USE GameManager;

DROP PROCEDURE IF EXISTS sp_getAllDataMatchHold;

DELIMITER $$

CREATE PROCEDURE sp_getAllDataMatchHold(
    IN idUser BIGINT,
    OUT jsonOfJsons JSON        
)
BEGIN
    DECLARE GameMatchHold INT DEFAULT 
        (SELECT  
            big_id 
        FROM
            GameMatch
        WHERE
            tin_gameState_FK = 2 AND
            big_user_FK = idUser    
        ORDER BY
            big_id DESC
        LIMIT 1)
    ;

    DECLARE state INT DEFAULT 0;
        
    DECLARE jsonMove JSON;

    DECLARE jsonCounter INT DEFAULT 1;

    DECLARE jsonKey VARCHAR(20);    

    DECLARE cu_mergeJsons CURSOR FOR 
        SELECT
        JSON_OBJECT( 'idMatch', GameMatch.big_id,
            'lastTime', GameMatch.tim_lastTime,
            'idGame', GameMatch.tin_game_FK,
            'idUser', GameMatch.big_user_FK,
            'stateMatch', GameMatch.tin_gameState_FK,        
            'jsonMove', Movement.jso_move ) AS dataMoves
        FROM
            Movement
        JOIN
            GameMatch ON Movement.big_match_FK = GameMatchHold      
        WHERE 
            GameMatch.big_user_FK = idUser AND
            GameMatch.tin_gameState_FK = 2     
        ;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET state = 1;

    OPEN cu_mergeJsons;

    jsons_loop: LOOP
        FETCH cu_mergeJsons INTO jsonMove;

        IF state = 1 THEN
            LEAVE jsons_loop;
        END IF;

        SET jsonKey = CONCAT("$.move",jsonCounter);

        IF jsonOfJsons IS NULL THEN
            SELECT JSON_ARRAY_APPEND('{}',jsonKey,jsonMove) INTO jsonOfJsons;
        END IF;

        IF jsonOfJsons IS NOT NULL AND jsonKey IS NOT NULL AND jsonMove IS NOT NULL THEN
            SELECT JSON_INSERT(jsonOfJsons,jsonKey,jsonMove) INTO jsonOfJsons;
        END IF;
        

        SET jsonCounter = jsonCounter +1;
    END LOOP;

    CLOSE cu_mergeJsons;   
    

END $$

DELIMITER ;