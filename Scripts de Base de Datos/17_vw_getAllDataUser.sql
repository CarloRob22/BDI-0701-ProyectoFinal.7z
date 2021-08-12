USE GameManager;

DROP VIEW IF EXISTS vm_getAllDataUser;

CREATE VIEW vm_getAllDataUser AS 
    SELECT
        big_id,
        var_firstName,
        var_lastName,
        var_email,
        var_nickname,
        var_password
    FROM
        User
    ;