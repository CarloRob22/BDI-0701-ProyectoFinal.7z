USE GameManager;

DROP FUNCTION IF EXISTS fn_weighFloodItMatch;
DROP FUNCTION IF EXISTS fn_weighDestroyDotsMatch;

CREATE FUNCTION fn_weighFloodItMatch(
    int_countMovements INT,
    tim_timeScore_param TIME
) 
RETURNS DECIMAL(4,2)  DETERMINISTIC
    RETURN (25000-((int_countMovements-1)*1000))/TIME_TO_SEC(tim_timeScore_param)
;

CREATE FUNCTION fn_weighDestroyDotsMatch(
    int_countMovements INT,
    tim_timeScore_param TIME
)
RETURNS DECIMAL(4,2)  DETERMINISTIC
    RETURN 0.01*int_countMovements*TIME_TO_SEC(tim_timeScore_param)
;